#!/usr/bin/env python3
"""
Validate a project YAML file for the assembly instructions generator.

Checks structure, required fields, component references, wiring consistency,
and step ordering.

Usage:
    python3 validate_project.py project.yaml
"""

import sys
import yaml
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from components import COMPONENTS

VALID_ACTIONS = {'place', 'attach', 'insert', 'wire', 'flip', 'test'}
VALID_TOOLS = {
    'phillips_screwdriver', 'hex_wrench', 'wire_strippers',
    'soldering_iron', 'drill', 'pliers', 'multimeter'
}
VALID_WIRE_COLORS = {'red', 'black', 'yellow', 'green', 'blue', 'white', 'orange', 'purple'}
VALID_SHAPES = {'rect', 'l_bracket', 'standoff', 'enclosure_box'}


def validate(yaml_path):
    """Validate project YAML. Returns (is_valid, errors, warnings)."""
    errors = []
    warnings = []

    # Load
    try:
        with open(yaml_path, 'r') as f:
            project = yaml.safe_load(f)
    except Exception as e:
        return False, [f"Cannot parse YAML: {e}"], []

    if not isinstance(project, dict):
        return False, ["Root must be a YAML mapping"], []

    # Project section
    if 'project' not in project:
        errors.append("Missing required 'project' section")
    elif 'name' not in project['project']:
        errors.append("Missing required 'project.name'")

    # Parts section
    parts = project.get('parts', {})
    all_part_ids = set()

    # Structural parts
    for i, part in enumerate(parts.get('structural', [])):
        pid = part.get('id')
        if not pid:
            errors.append(f"structural[{i}]: missing 'id'")
        elif pid in all_part_ids:
            errors.append(f"structural[{i}]: duplicate id '{pid}'")
        else:
            all_part_ids.add(pid)

        if not part.get('name'):
            errors.append(f"structural[{i}]: missing 'name'")

        shape = part.get('shape', '')
        if shape and shape not in VALID_SHAPES:
            warnings.append(f"structural[{i}]: shape '{shape}' not in component library")

    # Hardware parts
    for i, part in enumerate(parts.get('hardware', [])):
        pid = part.get('id')
        if not pid:
            errors.append(f"hardware[{i}]: missing 'id'")
        elif pid in all_part_ids:
            errors.append(f"hardware[{i}]: duplicate id '{pid}'")
        else:
            all_part_ids.add(pid)

        if not part.get('name'):
            errors.append(f"hardware[{i}]: missing 'name'")
        if not part.get('quantity'):
            warnings.append(f"hardware[{i}]: missing 'quantity' (defaulting to 1)")

        hw_type = part.get('type', '')
        if hw_type and hw_type not in COMPONENTS:
            warnings.append(f"hardware[{i}]: type '{hw_type}' not in component library")

    # Electronic parts
    for i, part in enumerate(parts.get('electronic', [])):
        pid = part.get('id')
        if not pid:
            errors.append(f"electronic[{i}]: missing 'id'")
        elif pid in all_part_ids:
            errors.append(f"electronic[{i}]: duplicate id '{pid}'")
        else:
            all_part_ids.add(pid)

        if not part.get('name'):
            errors.append(f"electronic[{i}]: missing 'name'")

        comp = part.get('component', '')
        if comp and comp not in COMPONENTS:
            warnings.append(f"electronic[{i}]: component '{comp}' not in library. "
                          f"Available: {', '.join(sorted(k for k in COMPONENTS.keys() if not k.startswith(('screw','nut','wall','cable','adhesive','rect','l_br','stand','encl'))))}")

    # Tools
    for tool in project.get('tools', []):
        if tool not in VALID_TOOLS:
            warnings.append(f"Unknown tool '{tool}' — will show as generic tool icon")

    # Wiring
    electronic_ids = {p['id'] for p in parts.get('electronic', [])}
    for i, wire in enumerate(project.get('wiring', [])):
        from_part = wire.get('from', {}).get('part', '')
        to_part = wire.get('to', {}).get('part', '')

        if from_part and from_part not in electronic_ids:
            errors.append(f"wiring[{i}]: 'from.part' '{from_part}' not found in electronic parts")
        if to_part and to_part not in electronic_ids:
            errors.append(f"wiring[{i}]: 'to.part' '{to_part}' not found in electronic parts")

        color = wire.get('color', '')
        if color and color not in VALID_WIRE_COLORS:
            warnings.append(f"wiring[{i}]: color '{color}' not standard. "
                          f"Use: {', '.join(sorted(VALID_WIRE_COLORS))}")

    # Steps
    steps = project.get('steps', [])
    if not steps:
        errors.append("Missing required 'steps' section (need at least 1 step)")

    for i, step in enumerate(steps):
        if 'step' not in step:
            warnings.append(f"steps[{i}]: missing 'step' number (will auto-number)")

        action = step.get('action', '')
        if action and action not in VALID_ACTIONS:
            warnings.append(f"steps[{i}]: unknown action '{action}'. "
                          f"Valid: {', '.join(sorted(VALID_ACTIONS))}")

        # Check part references in steps
        for pid in step.get('parts', []):
            if pid not in all_part_ids:
                errors.append(f"steps[{i}]: references unknown part '{pid}'")
        for hid in step.get('hardware', []):
            if hid not in all_part_ids:
                errors.append(f"steps[{i}]: references unknown hardware '{hid}'")

    return len(errors) == 0, errors, warnings


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_project.py project.yaml")
        sys.exit(1)

    yaml_path = sys.argv[1]
    if not os.path.exists(yaml_path):
        print(f"❌ File not found: {yaml_path}")
        sys.exit(1)

    valid, errors, warnings = validate(yaml_path)

    if warnings:
        print("⚠️  Warnings:")
        for w in warnings:
            print(f"   • {w}")
        print()

    if errors:
        print("❌ Errors:")
        for e in errors:
            print(f"   • {e}")
        print(f"\n❌ Validation FAILED ({len(errors)} errors, {len(warnings)} warnings)")
        sys.exit(1)
    else:
        with open(yaml_path, 'r') as f:
            project = yaml.safe_load(f)
        n_parts = (len(project.get('parts', {}).get('structural', []))
                   + len(project.get('parts', {}).get('hardware', []))
                   + len(project.get('parts', {}).get('electronic', [])))
        n_steps = len(project.get('steps', []))
        n_wires = len(project.get('wiring', []))
        print(f"✅ Valid project: {project['project']['name']}")
        print(f"   {n_parts} parts, {n_steps} steps, {n_wires} wiring connections")
        if warnings:
            print(f"   ({len(warnings)} warnings — see above)")


if __name__ == "__main__":
    main()
