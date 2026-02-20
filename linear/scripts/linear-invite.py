#!/usr/bin/env python3
"""Invite users to Linear workspace via GraphQL API."""

import os
import sys
import json
import urllib.request
import urllib.error

LINEAR_API = "https://api.linear.app/graphql"

def get_token():
    token = os.environ.get("LINEAR_API_KEY")
    if not token:
        print("Error: LINEAR_API_KEY environment variable not set")
        sys.exit(1)
    return token

def graphql(query, variables=None):
    """Execute a GraphQL query against Linear API."""
    token = get_token()

    data = json.dumps({
        "query": query,
        "variables": variables or {}
    }).encode('utf-8')

    req = urllib.request.Request(LINEAR_API, data=data, method='POST')
    req.add_header('Authorization', token)
    req.add_header('Content-Type', 'application/json')

    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        print(f"HTTP Error {e.code}: {error_body}")
        sys.exit(1)

def check_invite_mutation():
    """Check if organizationInviteCreate mutation exists."""
    query = """
    {
        __type(name: "Mutation") {
            fields {
                name
                args { name type { name kind ofType { name } } }
            }
        }
    }
    """
    result = graphql(query)

    if "errors" in result:
        print(f"Error: {result['errors']}")
        return None

    mutations = result.get("data", {}).get("__type", {}).get("fields", [])
    invite_mutations = [m for m in mutations if "invite" in m["name"].lower()]

    return invite_mutations

def invite_user(email, team_ids=None, role="user"):
    """Invite a user to the Linear workspace."""

    # Try organizationInviteCreate mutation
    query = """
    mutation InviteUser($input: OrganizationInviteCreateInput!) {
        organizationInviteCreate(input: $input) {
            success
            organizationInvite {
                id
                email
                createdAt
            }
        }
    }
    """

    variables = {
        "input": {
            "email": email,
            "role": role
        }
    }

    if team_ids:
        variables["input"]["teamIds"] = team_ids

    result = graphql(query, variables)
    return result

def list_pending_invites():
    """List pending organization invites."""
    query = """
    {
        organizationInvites {
            nodes {
                id
                email
                createdAt
                acceptedAt
            }
        }
    }
    """
    result = graphql(query)
    return result

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:")
        print("  linear-invite.py check              # Check if invite API is available")
        print("  linear-invite.py list               # List pending invites")
        print("  linear-invite.py <email> [role]     # Invite user (role: user, admin, guest)")
        print("")
        print("Examples:")
        print("  linear-invite.py check")
        print("  linear-invite.py andy@example.com")
        print("  linear-invite.py andy@example.com admin")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "check":
        print("Checking for invite-related mutations...")
        mutations = check_invite_mutation()
        if mutations:
            print(f"Found {len(mutations)} invite-related mutations:")
            for m in mutations:
                print(f"  - {m['name']}")
                for arg in m.get('args', []):
                    arg_type = arg['type'].get('name') or arg['type'].get('ofType', {}).get('name', 'unknown')
                    print(f"      {arg['name']}: {arg_type}")
        else:
            print("No invite mutations found or error occurred")

    elif cmd == "list":
        print("Listing pending invites...")
        result = list_pending_invites()
        if "errors" in result:
            print(f"Error: {result['errors']}")
        else:
            invites = result.get("data", {}).get("organizationInvites", {}).get("nodes", [])
            if invites:
                for inv in invites:
                    status = "accepted" if inv.get("acceptedAt") else "pending"
                    print(f"  {inv['email']} - {status}")
            else:
                print("  No pending invites")

    else:
        # Assume it's an email
        email = cmd
        role = sys.argv[2] if len(sys.argv) > 2 else "user"

        print(f"Inviting {email} as {role}...")
        result = invite_user(email, role=role)

        if "errors" in result:
            print(f"Error: {result['errors']}")
            print("")
            print("Note: Your API key may not have permission to invite users.")
            print("Try inviting manually at: https://linear.app/settings/members")
        else:
            data = result.get("data", {}).get("organizationInviteCreate", {})
            if data.get("success"):
                print(f"Successfully invited {email}!")
            else:
                print(f"Invite failed. Response: {result}")
