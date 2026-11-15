import json

# Read marketplace.json
with open('marketplace.json', 'r') as f:
    data = json.load(f)

# Create GitHub plugin entry
github_plugin = {
    "name": "github",
    "displayName": "GitHub MCP",
    "description": "GitHub MCP server support for Claude Code with OAuth and PAT fallback",
    "source": "plugins/github",
    "lspServers": {
        "github": {
            "command": "mcp",
            "args": ["github"],
            "extensionToLanguage": {
                ".github": "github"
            },
            "transport": "stdio",
            "initializationOptions": {
                "auth": "oauth",
                "fallbackToPAT": True
            }
        }
    },
    "strict": False
}

# Add GitHub plugin to the list
data["plugins"].append(github_plugin)

# Write back to marketplace.json
with open('marketplace.json', 'w') as f:
    json.dump(data, f, indent=2)

print("GitHub plugin added to marketplace.json")
