"use strict";
// src/index.ts
// Demonstrates optimized data fetching using memoization to prevent redundant backend calls.
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const memoizeAsync_1 = require("./memoizeAsync");
const expensiveFunction_1 = require("./expensiveFunction");
function run() {
    return __awaiter(this, void 0, void 0, function* () {
        const controller = new AbortController(); // Utilizes AbortController to manage fetch signals.
        const memoizedExpensiveFunction = (0, memoizeAsync_1.memoizeAsync)(expensiveFunction_1.expensiveFunction);
        // Demonstrates memoization: fetches data once and uses cache for subsequent call.
        console.log(yield memoizedExpensiveFunction(controller.signal)); // First call, fetches data.
        console.log(yield memoizedExpensiveFunction(controller.signal)); // Second call, returns cached data.
    });
}
run();
