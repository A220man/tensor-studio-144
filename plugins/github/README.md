# GitHub Plugin

Provides GitHub MCP (Model Context Protocol) server support for Claude Code.

## Features

- GitHub API integration for Claude
- OAuth authentication support
- Personal Access Token (PAT) fallback authentication
- Repository operations, issues, pull requests, and more

## Installation

This plugin is part of the official Claude Plugins marketplace and is automatically installed when using the marketplace.

## Configuration

The GitHub plugin uses the `mcp` command with `github` arguments. It supports:
- OAuth authentication (preferred): Automatic OAuth flow via Claude's authentication system
- PAT (Personal Access Token) fallback: Provide a Personal Access Token when OAuth is not available

## Requirements

- GitHub account with appropriate permissions
- For PAT fallback: generate a Personal Access Token with required scopes

## Authentication

The plugin supports two authentication methods:
1. OAuth (preferred): Automatic OAuth flow via Claude's authentication system
2. PAT (fallback): Provide a Personal Access Token when OAuth is not available

For more details on authentication, see the plugin's implementation and error handling.
