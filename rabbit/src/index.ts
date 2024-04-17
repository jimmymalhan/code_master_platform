// src/index.ts
// Demonstrates optimized data fetching using memoization to prevent redundant backend calls.

import { memoizeAsync } from './memoizeAsync';
import { expensiveFunction } from './expensiveFunction';

async function run() {
    const controller = new AbortController();  // Utilizes AbortController to manage fetch signals.
    const memoizedExpensiveFunction = memoizeAsync(expensiveFunction);

    // Demonstrates memoization: fetches data once and uses cache for subsequent call.
    console.log(await memoizedExpensiveFunction(controller.signal));  // First call, fetches data.
    console.log(await memoizedExpensiveFunction(controller.signal));  // Second call, returns cached data.
}

run();
