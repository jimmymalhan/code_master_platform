// custom_types/index.d.ts
/// <reference types="node" />

declare module "node:abort-controller" {
    export { AbortController, AbortSignal } from "abort-controller";
  }