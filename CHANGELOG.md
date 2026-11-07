# Changelog

## 1.1.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.0.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

All notable changes to this marketplace will be documented in this file.

## [Unreleased]

### Added
- Initial marketplace skeleton with `marketplace.json`, `README.md`, and plugin directory structure
- TypeScript LSP plugin (`typescript-lsp`) using `typescript-language-server`
- Vue/Volar LSP plugin (`vue-volar-lsp`) using `@vue/language-server` per issue #232
- Python LSP plugin (`pyright-lsp`) using `pyright-langserver`
- Go LSP plugin (`gopls-lsp`) using `gopls`
- Rust LSP plugin (`rust-analyzer-lsp`) using `rust-analyzer`
- C/C++ LSP plugin (`clangd-lsp`) using `clangd`
- PHP LSP plugin (`php-lsp`) using `phpactor`
- Swift LSP plugin (`swift-lsp`) using `sourcekit-lsp`
- Kotlin LSP plugin (`kotlin-lsp`) using `kotlin-language-server`
- C# LSP plugin (`csharp-lsp`) using `csharp-lsp` (OmniSharp)
- Java LSP plugin (`jdtls-lsp`) using `jdtls` (Eclipse JDT Language Server)
- Lua LSP plugin (`lua-lsp`) using `lua-language-server`

### Fixed
- All 12 LSP plugins now include `.lsp.json` configuration files (fixes issue #379)
- `marketplace.json` `lspServers` configurations match `.lsp.json` files for all plugins

### Added
- Marketplace validation script (`validate_marketplace.py`) to verify consistency

## [1.0.0] - 2026-10-31
Initial release of the official Claude Code Plugins marketplace with 12 LSP plugins.

