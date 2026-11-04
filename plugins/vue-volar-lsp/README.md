# Vue/Volar LSP Plugin

Provides Language Server Protocol support for Vue.js Single File Components (`.vue` files) using the Volar language server (`@vue/language-server`).

## Features

- Go-to-definition in `.vue` files
- Hover information for components and props
- Find references across SFC (Single File Components)
- TypeScript integration in `<script lang="ts">` blocks

## Installation

```bash
npm install -g @vue/language-server
```

## Configuration

The plugin uses `vue-language-server` with stdio transport. It requires TypeScript to be available in the project (via `node_modules/typescript/lib`) for full TypeScript support in Vue SFCs.

## Requirements

- Node.js
- `@vue/language-server` installed globally
- TypeScript installed in the project for `<script lang="ts">` support