#!/usr/bin/env python3
"""Create and manage Linear custom views via GraphQL API."""

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

def list_views():
    """List all custom views."""
    query = """
    {
        customViews(first: 50) {
            nodes {
                id
                name
                description
                shared
                team {
                    key
                    name
                }
                owner {
                    name
                }
                createdAt
            }
        }
    }
    """
    result = graphql(query)
    return result

def get_view(view_id):
    """Get details of a specific view."""
    query = """
    query GetView($id: String!) {
        customView(id: $id) {
            id
            name
            description
            shared
            filterData
            team {
                key
                name
            }
            owner {
                name
            }
        }
    }
    """
    result = graphql(query, {"id": view_id})
    return result

def create_view(name, filters=None, team_id=None, description=None, shared=True):
    """Create a new custom view."""
    query = """
    mutation CreateView($input: CustomViewCreateInput!) {
        customViewCreate(input: $input) {
            success
            customView {
                id
                name
                description
                shared
            }
        }
    }
    """

    input_data = {
        "name": name,
        "shared": shared
    }

    if description:
        input_data["description"] = description

    if team_id:
        input_data["teamId"] = team_id

    if filters:
        input_data["filterData"] = filters

    result = graphql(query, {"input": input_data})
    return result

def delete_view(view_id):
    """Delete a custom view."""
    query = """
    mutation DeleteView($id: String!) {
        customViewDelete(id: $id) {
            success
        }
    }
    """
    result = graphql(query, {"id": view_id})
    return result

def get_teams():
    """Get all teams to help with team IDs."""
    query = """
    {
        teams {
            nodes {
                id
                key
                name
            }
        }
    }
    """
    result = graphql(query)
    return result

# Pre-built filter templates
# Priority: 0=none, 1=urgent, 2=high, 3=medium, 4=low
FILTER_TEMPLATES = {
    "high-priority": {
        "priority": {"lte": 2, "neq": 0}
    },
    "urgent": {
        "priority": {"eq": 1}
    },
    "due-this-week": {
        "dueDate": {"lt": "P1W"}
    },
    "overdue": {
        "dueDate": {"lt": "P0D"}
    },
    "unassigned": {
        "assignee": {"null": True}
    },
    "bugs": {
        "labels": {"name": {"containsIgnoreCase": "bug"}}
    },
    "in-progress": {
        "state": {"type": {"eq": "started"}}
    },
    "blocked": {
        "labels": {"name": {"containsIgnoreCase": "blocked"}}
    }
}

def print_usage():
    print("Usage:")
    print("  linear-view.py list                              # List all views")
    print("  linear-view.py view <view_id>                    # Get view details")
    print("  linear-view.py create <name> [options]           # Create a view")
    print("  linear-view.py delete <view_id>                  # Delete a view")
    print("  linear-view.py teams                             # List teams (for team IDs)")
    print("  linear-view.py templates                         # Show filter templates")
    print("")
    print("Create options:")
    print("  --team <team_id>          Team ID to scope the view")
    print("  --desc <description>      View description")
    print("  --filter <json>           Custom filter JSON")
    print("  --template <name>         Use a pre-built filter template")
    print("  --private                 Make view private (default: shared)")
    print("")
    print("Examples:")
    print("  linear-view.py create 'Urgent Issues' --template urgent")
    print("  linear-view.py create 'My Bugs' --template bugs --team TEAM_ID")
    print("  linear-view.py create 'Custom' --filter '{\"priority\": {\"number\": {\"eq\": 1}}}'")
    print("")
    print("Templates: " + ", ".join(FILTER_TEMPLATES.keys()))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "list":
        print("Listing custom views...")
        result = list_views()
        if "errors" in result:
            print(f"Error: {result['errors']}")
        else:
            views = result.get("data", {}).get("customViews", {}).get("nodes", [])
            if views:
                for v in views:
                    team = v.get("team", {})
                    team_str = f" [{team.get('key')}]" if team else " [workspace]"
                    shared_str = "shared" if v.get("shared") else "private"
                    print(f"  {v['name']}{team_str} ({shared_str})")
                    print(f"    ID: {v['id']}")
                    if v.get("description"):
                        print(f"    Desc: {v['description']}")
            else:
                print("  No custom views found")

    elif cmd == "view":
        if len(sys.argv) < 3:
            print("Error: view_id required")
            sys.exit(1)
        view_id = sys.argv[2]
        print(f"Getting view {view_id}...")
        result = get_view(view_id)
        if "errors" in result:
            print(f"Error: {result['errors']}")
        else:
            v = result.get("data", {}).get("customView")
            if v:
                print(f"Name: {v['name']}")
                print(f"ID: {v['id']}")
                print(f"Description: {v.get('description', 'N/A')}")
                print(f"Shared: {v.get('shared', False)}")
                print(f"Filters: {json.dumps(v.get('filterData', {}), indent=2)}")
            else:
                print("View not found")

    elif cmd == "create":
        if len(sys.argv) < 3:
            print("Error: name required")
            sys.exit(1)

        name = sys.argv[2]
        team_id = None
        description = None
        filters = None
        shared = True

        # Parse options
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--team" and i + 1 < len(sys.argv):
                team_id = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--desc" and i + 1 < len(sys.argv):
                description = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--filter" and i + 1 < len(sys.argv):
                filters = json.loads(sys.argv[i + 1])
                i += 2
            elif sys.argv[i] == "--template" and i + 1 < len(sys.argv):
                template_name = sys.argv[i + 1]
                if template_name in FILTER_TEMPLATES:
                    filters = FILTER_TEMPLATES[template_name]
                else:
                    print(f"Unknown template: {template_name}")
                    print(f"Available: {', '.join(FILTER_TEMPLATES.keys())}")
                    sys.exit(1)
                i += 2
            elif sys.argv[i] == "--private":
                shared = False
                i += 1
            else:
                print(f"Unknown option: {sys.argv[i]}")
                sys.exit(1)

        print(f"Creating view '{name}'...")
        if filters:
            print(f"  Filters: {json.dumps(filters)}")

        result = create_view(name, filters=filters, team_id=team_id, description=description, shared=shared)

        if "errors" in result:
            print(f"Error: {result['errors']}")
        else:
            data = result.get("data", {}).get("customViewCreate", {})
            if data.get("success"):
                view = data.get("customView", {})
                print(f"Successfully created view!")
                print(f"  ID: {view.get('id')}")
                print(f"  Name: {view.get('name')}")
            else:
                print(f"Failed to create view. Response: {result}")

    elif cmd == "delete":
        if len(sys.argv) < 3:
            print("Error: view_id required")
            sys.exit(1)
        view_id = sys.argv[2]
        print(f"Deleting view {view_id}...")
        result = delete_view(view_id)
        if "errors" in result:
            print(f"Error: {result['errors']}")
        else:
            data = result.get("data", {}).get("customViewDelete", {})
            if data.get("success"):
                print("Successfully deleted view!")
            else:
                print(f"Failed to delete view. Response: {result}")

    elif cmd == "teams":
        print("Listing teams...")
        result = get_teams()
        if "errors" in result:
            print(f"Error: {result['errors']}")
        else:
            teams = result.get("data", {}).get("teams", {}).get("nodes", [])
            for t in teams:
                print(f"  {t['key']}: {t['name']} (ID: {t['id']})")

    elif cmd == "templates":
        print("Available filter templates:")
        for name, filters in FILTER_TEMPLATES.items():
            print(f"  {name}:")
            print(f"    {json.dumps(filters)}")

    else:
        print(f"Unknown command: {cmd}")
        print_usage()
        sys.exit(1)
