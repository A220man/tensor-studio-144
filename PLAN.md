# Product development plan

Each round completes one feature or repair. Future items are planned, not implemented claims.

## Current round

vue-volar-lsp

## Roadmap

### marketplace-skeleton — Marketplace skeleton with plugin directory structure

Status: done

Acceptance:
- Repository has plugins/ directory with at least one example plugin
- marketplace.json exists with valid schema
- README.md documents the marketplace structure

Implementation: `plugins/typescript-lsp/.lsp.json`, `plugins/typescript-lsp/README.md`, `marketplace.json`, `README.md`

### vue-volar-lsp — Add Vue/Volar LSP plugin

Status: done

Acceptance:
- plugins/vue-volar-lsp/.lsp.json exists with Volar configuration
- marketplace.json includes vue-volar-lsp entry
- Plugin installs and provides LSP for .vue files

Implementation: `plugins/vue-volar-lsp/.lsp.json`, `plugins/vue-volar-lsp/README.md`, `marketplace.json`

### lsp-json-fix — Fix missing .lsp.json for existing LSP plugins

Status: done

Acceptance:
- All 11 existing LSP plugins have .lsp.json files
- marketplace.json lspServers configs match .lsp.json files
- Plugins provide LSP functionality when installed

Implementation: `plugins/gopls-lsp/.lsp.json`, `plugins/gopls-lsp/README.md`, `plugins/rust-analyzer-lsp/.lsp.json`, `plugins/rust-analyzer-lsp/README.md`, `plugins/clangd-lsp/.lsp.json`, `plugins/clangd-lsp/README.md`, `plugins/php-lsp/.lsp.json`, `plugins/php-lsp/README.md`, `plugins/swift-lsp/.lsp.json`, `plugins/swift-lsp/README.md`, `plugins/kotlin-lsp/.lsp.json`, `plugins/kotlin-lsp/README.md`, `plugins/csharp-lsp/.lsp.json`, `plugins/csharp-lsp/README.md`, `plugins/jdtls-lsp/.lsp.json`, `plugins/jdtls-lsp/README.md`, `plugins/lua-lsp/.lsp.json`, `plugins/lua-lsp/README.md`, `marketplace.json`

