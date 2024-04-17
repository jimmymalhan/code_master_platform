// src/memoizeAsync.ts
// Memoizes async functions, particularly for repeated HTTP calls to optimize performance.


/**
 * Memoizes an asynchronous function to optimize repeated calls with the same parameters.
 * Ensures that each function call is made only once per unique input.
 * Handles abort signals to cancel ongoing operations.
 *
 * @template T The type of the result of the asynchronous function.
 * @param {(signal: AbortSignal) => Promise<T>} fn - The asynchronous function to memoize.
 * @returns {(signal: AbortSignal) => Promise<T>} The memoized function.
 */
export function memoizeAsync<T>(fn: (signal: AbortSignal) => Promise<T>): (signal: AbortSignal) => Promise<T> {
    const cache = new Map<string, Promise<T>>();

    return async (signal: AbortSignal): Promise<T> => {
        const key = signal.toString();  // Generate a unique key for the signal.

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
        return cache.get(key)!;
    };
}
