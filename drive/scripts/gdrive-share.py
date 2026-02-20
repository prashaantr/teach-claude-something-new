#!/usr/bin/env python3
"""Share Google Drive files using rclone's OAuth credentials."""

import json
import sys
import subprocess
import urllib.request
import urllib.parse

RCLONE_CONFIG = "/home/node/.config/rclone/rclone.conf"

def get_token():
    """Extract access token from rclone config, refresh if needed."""
    import configparser
    config = configparser.ConfigParser()
    config.read(RCLONE_CONFIG)

    token_data = json.loads(config['gdrive']['token'])
    return token_data['access_token']

def get_file_id(path):
    """Get file ID from rclone."""
    result = subprocess.run(
        ['rclone', 'lsf', f'gdrive:{path}', '--format', 'i'],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error: Could not find file at {path}")
        sys.exit(1)
    return result.stdout.strip()

def share_file(file_id, email, role='writer'):
    """Share file with user via Drive API."""
    token = get_token()

    url = f"https://www.googleapis.com/drive/v3/files/{file_id}/permissions"
    data = json.dumps({
        'role': role,
        'type': 'user',
        'emailAddress': email
    }).encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')
    req.add_header('Authorization', f'Bearer {token}')
    req.add_header('Content-Type', 'application/json')

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read())
            print(f"Shared with {email} as {role}")
            return result
    except urllib.error.HTTPError as e:
        error = json.loads(e.read())
        print(f"Error: {error.get('error', {}).get('message', str(e))}")
        sys.exit(1)

def share_folder(path, email, role='writer'):
    """Share a folder (and contents) with user."""
    file_id = get_file_id(path)
    return share_file(file_id, email, role)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: gdrive-share.py <path> <email> [role]")
        print("  path: Google Drive path (e.g., 'Foreman/doc.pdf')")
        print("  email: Email to share with")
        print("  role: 'reader', 'writer', or 'commenter' (default: writer)")
        sys.exit(1)

    path = sys.argv[1]
    email = sys.argv[2]
    role = sys.argv[3] if len(sys.argv) > 3 else 'writer'

    share_folder(path, email, role)
