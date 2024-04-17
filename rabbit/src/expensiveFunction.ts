// src/expensiveFunction.ts
// Purpose: Defines an asynchronous function to fetch data from a URL.

// Fetches data from a URL and handles abort signals.
export async function expensiveFunction(signal: AbortSignal): Promise<string> {
    console.log('Fetching data...');
    try {
        const response = await fetch("https://example.com/data", { signal });
        if (!response.ok) {
            throw new Error(`Failed to fetch: ${response.statusText}`);
        }
        return response.text();
    } catch (error) {
        console.error('Fetch error:', (error as Error).message); // Type assertion to Error
        throw error;
    }
}