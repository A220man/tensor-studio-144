# Claude Plugins Official Marketplace — Ryan Vo

> Work in progress. This checkpoint may be incomplete or fail tests. See PLAN.md and STATUS.md before use.


Official, Anthropic-managed directory of high quality Claude Code Plugins.

## Structure

```
.
├── marketplace.json          # Marketplace manifest
├── plugins/                  # Plugin source directories
│   ├── typescript-lsp/       # TypeScript/JavaScript LSP plugin
│   │   ├── .lsp.json         # LSP server configuration
│   │   └── README.md         # Plugin documentation
│   ├── vue-volar-lsp/        # Vue.js LSP plugin (Volar)
│   │   ├── .lsp.json         # LSP server configuration
│   │   └── README.md         # Plugin documentation
│   ├── pyright-lsp/          # Python LSP plugin
│   │   ├── .lsp.json         # LSP server configuration
│   │   └── README.md         # Plugin documentation
│   ├── gopls-lsp/            # Go LSP plugin
│   │   ├── .lsp.json         # LSP server configuration
│   │   └── README.md         # Plugin documentation
│   ├── rust-analyzer-lsp/    # Rust LSP plugin
│   │   ├── .lsp.json         # LSP server configuration
│   │   └── README.md         # Plugin documentation
│   ├── clangd-lsp/           # C/C++ LSP plugin
│   │   ├── .lsp.json         # LSP server configuration
│   │   └── README.md         # Plugin documentation
│   ├── php-lsp/              # PHP LSP plugin
│   │   ├── .lsp.json         # LSP server configuration
│   │   └── README.md         # Plugin documentation
│   ├── swift-lsp/            # Swift LSP plugin
│   │   ├── .lsp.json         # LSP server configuration
│   │   └── README.md         # Plugin documentation
│   ├── kotlin-lsp/           # Kotlin LSP plugin
│   │   ├── .lsp.json         # LSP server configuration
│   │   └── README.md         # Plugin documentation
│   ├── csharp-lsp/           # C# LSP plugin
│   │   ├── .lsp.json         # LSP server configuration
│   │   └── README.md         # Plugin documentation
│   ├── jdtls-lsp/            # Java LSP plugin
│   │   ├── .lsp.json         # LSP server configuration
│   │   └── README.md         # Plugin documentation
│   └── lua-lsp/              # Lua LSP plugin
│       ├── .lsp.json         # LSP server configuration
│       └── README.md         # Plugin documentation
└── README.md                 # This file
```

## Available Plugins

| Plugin | Description | LSP Server |
|--------|-------------|------------|
| `typescript-lsp` | TypeScript/JavaScript language server support | `typescript-language-server` |
| `vue-volar-lsp` | Vue.js language server support via Volar | `vue-language-server` (@vue/language-server) |
| `pyright-lsp` | Python language server support | `pyright-langserver` |
| `gopls-lsp` | Go language server support | `gopls` |
| `rust-analyzer-lsp` | Rust language server support | `rust-analyzer` |
| `clangd-lsp` | C/C++ language server support | `clangd` |
| `php-lsp` | PHP language server support | `phpactor` |
| `swift-lsp` | Swift language server support | `sourcekit-lsp` |
| `kotlin-lsp` | Kotlin language server support | `kotlin-language-server` |
| `csharp-lsp` | C# language server support | `csharp-lsp` (OmniSharp) |
| `jdtls-lsp` | Java language server support | `jdtls` |
| `lua-lsp` | Lua language server support | `lua-language-server` |

## Plugin Format

Each plugin lives in its own directory under `plugins/` and must contain:

- `.lsp.json` - LSP server configuration (required for LSP plugins)
- `README.md` - Plugin documentation

The `marketplace.json` follows this schema:

```json
{
  "schemaVersion": 1,
  "name": "marketplace-name",
  "displayName": "Display Name",
  "description": "Marketplace description",
  "plugins": [
    {
      "name": "plugin-name",
      "displayName": "Plugin Display Name",
      "description": "Plugin description",
      "source": "plugins/plugin-name",
      "lspServers": { ... },
      "strict": false
    }
  ]
}
```

## License

Apache-2.0

Maintainer: Ryan Vo <ryandtvo@gmail.com>
