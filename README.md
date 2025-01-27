# Onlineschool SPA
This project serves as an online education platform designed for interactive learning experiences. It leverages modern front-end and back-end technologies to deliver a user-friendly and efficient system.

## Recommended IDE Setup
[VSCode](https://code.visualstudio.com/) with the following extensions:
   
  1. [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) for Vue 3 support.
  2. [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) for linting.
  3. [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) for code formatting.


## Type Support for `.vue` Imports in TypeScript

By default, TypeScript doesn't fully support type information for `.vue` imports. To address this, we use the `vue-tsc` CLI instead of tsc for type checking. Additionally, in editors, the [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.volar) is required to enable the TypeScript language service to recognize `.vue ` files.

For better performance, Volar offers a [Take Over Mode](https://github.com/johnsoncodehk/volar/discussions/471#discussioncomment-1361669), which can be enabled by following these steps:

### 1. Disable the built-in TypeScript Extension:
     1) Run `Extensions: Show Built-in Extensions` from VSCode's command palette
     2) Find `TypeScript and JavaScript Language Features`, right click and select `Disable (Workspace)`
### 2. Reload the VSCode window:
   Use the command palette to run `Developer: Reload Window`

## Project Setup
To set up the project, follow these steps:

### Install dependencies
Run the following command to install all necessary dependencies:
```sh
pnpm install
```

### Compile and Hot-Reload for Development
Run the development server:
```sh
pnpm dev
```

### Type-Check, Compile, and Minify for Production
Build the project for production:
```sh
pnpm build
```

### Lint with [ESLint](https://eslint.org/)
Run linting to check for code quality issues:
```sh
pnpm lint
```
