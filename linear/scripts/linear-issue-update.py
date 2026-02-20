#!/usr/bin/env python3
"""
Update Linear issue fields via GraphQL API.

The Linear CLI only supports `issue update --state`. This script handles
updating description, title, priority, and other fields.

Usage:
    python3 linear-issue-update.py TEAM-123 --description "New description"
    python3 linear-issue-update.py TEAM-123 --description-file /tmp/desc.md
    python3 linear-issue-update.py TEAM-123 --title "New title"
    python3 linear-issue-update.py TEAM-123 --priority 2
"""

import argparse
import json
import os
import sys
import urllib.request

API_URL = "https://api.linear.app/graphql"


def get_api_key():
    key = os.environ.get("LINEAR_API_KEY")
    if not key:
        print("Error: LINEAR_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)
    return key


def graphql_request(query, variables=None):
    api_key = get_api_key()

    payload = {"query": query}
    if variables:
        payload["variables"] = variables

    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "Authorization": api_key,
            "Content-Type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"API Error: {e.code} - {error_body}", file=sys.stderr)
        sys.exit(1)


def get_issue_uuid(issue_identifier):
    """Convert issue identifier (e.g., ARS-123) to UUID."""
    query = """
    query GetIssue($identifier: String!) {
        issue(id: $identifier) {
            id
            identifier
            title
        }
    }
    """

    # Try as identifier first (ARS-123 format)
    result = graphql_request(query, {"identifier": issue_identifier})

    if result.get("data", {}).get("issue"):
        issue = result["data"]["issue"]
        return issue["id"], issue["identifier"], issue["title"]

    # Check for errors
    if result.get("errors"):
        print(f"Error finding issue: {result['errors']}", file=sys.stderr)
        sys.exit(1)

    print(f"Issue {issue_identifier} not found", file=sys.stderr)
    sys.exit(1)


def update_issue(issue_uuid, updates):
    """Update issue fields via GraphQL."""
    mutation = """
    mutation UpdateIssue($id: String!, $input: IssueUpdateInput!) {
        issueUpdate(id: $id, input: $input) {
            success
            issue {
                identifier
                title
                description
            }
        }
    }
    """

    result = graphql_request(mutation, {"id": issue_uuid, "input": updates})

    if result.get("errors"):
        print(f"Error updating issue: {result['errors']}", file=sys.stderr)
        sys.exit(1)

    return result.get("data", {}).get("issueUpdate", {})


def main():
    parser = argparse.ArgumentParser(
        description="Update Linear issue fields (description, title, etc.)"
    )
    parser.add_argument("issue", help="Issue identifier (e.g., ARS-123)")
    parser.add_argument("--description", help="New description text")
    parser.add_argument("--description-file", help="Read description from file")
    parser.add_argument("--title", help="New title")
    parser.add_argument("--priority", type=int, choices=[0, 1, 2, 3, 4],
                        help="Priority: 0=none, 1=urgent, 2=high, 3=medium, 4=low")
    parser.add_argument("--estimate", type=int, help="Estimate (story points)")

    args = parser.parse_args()

    # Build updates dict
    updates = {}

    if args.description:
        updates["description"] = args.description

    if args.description_file:
        try:
            with open(args.description_file, "r") as f:
                updates["description"] = f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {args.description_file}", file=sys.stderr)
            sys.exit(1)

    if args.title:
        updates["title"] = args.title

    if args.priority is not None:
        updates["priority"] = args.priority

    if args.estimate is not None:
        updates["estimate"] = args.estimate

    if not updates:
        print("Error: No updates specified. Use --description, --title, etc.", file=sys.stderr)
        sys.exit(1)

    # Get issue UUID
    issue_uuid, identifier, current_title = get_issue_uuid(args.issue)
    print(f"Found issue: {identifier} - {current_title}")

    # Update issue
    result = update_issue(issue_uuid, updates)

    if result.get("success"):
        print(f"✓ Updated {identifier}")
        if "description" in updates:
            desc_preview = updates["description"][:100]
            if len(updates["description"]) > 100:
                desc_preview += "..."
            print(f"  Description: {desc_preview}")
        if "title" in updates:
            print(f"  Title: {updates['title']}")
        if "priority" in updates:
            print(f"  Priority: {updates['priority']}")
        if "estimate" in updates:
            print(f"  Estimate: {updates['estimate']}")
    else:
        print(f"Failed to update {identifier}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
