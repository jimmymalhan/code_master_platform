"use strict";
// src/memoizeAsync.ts
// Memoizes async functions, particularly for repeated HTTP calls to optimize performance.
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
exports.memoizeAsync = void 0;
/**
 * Memoizes an asynchronous function to optimize repeated calls with the same parameters.
 * Ensures that each function call is made only once per unique input.
 * Handles abort signals to cancel ongoing operations.
 *
 * @template T The type of the result of the asynchronous function.
 * @param {(signal: AbortSignal) => Promise<T>} fn - The asynchronous function to memoize.
 * @returns {(signal: AbortSignal) => Promise<T>} The memoized function.
 */
function memoizeAsync(fn) {
    const cache = new Map();
    return (signal) => __awaiter(this, void 0, void 0, function* () {
        const key = signal.toString(); // Generate a unique key for the signal.
        if (signal.aborted) {
            console.error('Operation was aborted.');
            throw new Error('Fetch aborted');
        }
        if (!cache.has(key)) {
            const resultPromise = fn(signal).catch(error => {
                cache.delete(key);
                throw error;
            });
            cache.set(key, resultPromise);
            signal.addEventListener('abort', () => {
                cache.delete(key);
                console.error('Operation aborted, cache cleared.');
            });
            return resultPromise;
        }
        return cache.get(key);
    });
}
exports.memoizeAsync = memoizeAsync;
