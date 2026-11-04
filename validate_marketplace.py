#!/usr/bin/env python3
"""Validate marketplace.json consistency with plugin directories."""

import json
import os
import sys


def validate_marketplace():
    repo_root = "/var/lib/alan-portfolio/workspaces/ryan/tensor-studio-144"
    marketplace_path = os.path.join(repo_root, "marketplace.json")
    plugins_dir = os.path.join(repo_root, "plugins")

    errors = []
    warnings = []

    # Load marketplace.json
    try:
        with open(marketplace_path) as f:
            marketplace = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"marketplace.json is invalid JSON: {e}")
        return 1

    # Check schemaVersion
    if marketplace.get("schemaVersion") != 1:
        errors.append(f"Expected schemaVersion 1, got {marketplace.get('schemaVersion')}")

    # Get plugin directories
    plugin_dirs = [
        d for d in os.listdir(plugins_dir)
        if os.path.isdir(os.path.join(plugins_dir, d)) and d.endswith("-lsp")
    ]

    marketplace_plugins = {p["name"]: p for p in marketplace.get("plugins", [])}

    # Check each plugin directory has .lsp.json and README.md
    for plugin_dir in plugin_dirs:
        lsp_path = os.path.join(plugins_dir, plugin_dir, ".lsp.json")
        readme_path = os.path.join(plugins_dir, plugin_dir, "README.md")

        if not os.path.exists(lsp_path):
            errors.append(f"Missing .lsp.json: {plugin_dir}")
        if not os.path.exists(readme_path):
            errors.append(f"Missing README.md: {plugin_dir}")

        # Check marketplace entry exists
        if plugin_dir not in marketplace_plugins:
            errors.append(f"Plugin directory {plugin_dir} not found in marketplace.json")
        else:
            # Compare lspServers
            mkt_servers = set(marketplace_plugins[plugin_dir].get("lspServers", {}).keys())
            try:
                with open(lsp_path) as f:
                    lsp_config = json.load(f)
                lsp_servers = set(lsp_config.get("lspServers", {}).keys())
                if mkt_servers != lsp_servers:
                    errors.append(f"lspServers mismatch for {plugin_dir}: marketplace={mkt_servers}, .lsp.json={lsp_servers}")
            except json.JSONDecodeError as e:
                errors.append(f"Invalid .lsp.json for {plugin_dir}: {e}")

    # Check for marketplace entries without plugin directories
    for name in marketplace_plugins:
        if name not in plugin_dirs:
            warnings.append(f"Marketplace entry {name} has no corresponding plugin directory")

    # Report
    for w in warnings:
        print(f"Warning: {w}", file=sys.stderr)

    for e in errors:
        print(f"Error: {e}", file=sys.stderr)

    if not errors and not warnings:
        print("Validation passed: marketplace.json is consistent with plugin directories")
        return 0
    elif not errors:
        print("Validation passed with warnings (see above)")
        return 0
    else:
        print(f"\nValidation failed: {len(errors)} error(s)", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(validate_marketplace())
