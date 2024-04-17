// tests/expensiveFunction.test.ts
// Tests to verify that the expensiveFunction only fetches data once when memoized.

import { expensiveFunction } from '../src/expensiveFunction';
import { memoizeAsync } from '../src/memoizeAsync';

describe('expensiveFunction', () => {
    it('fetches data only once when memoized', async () => {
        const mockFunction = jest.fn(expensiveFunction);
        const controller = new AbortController();
        const memoizedFunction = memoizeAsync(mockFunction);

        try {
            await memoizedFunction(controller.signal);
            await memoizedFunction(controller.signal);
        } catch (error) {
            console.log('Handled fetch error in test:', error);
        }

        expect(mockFunction).toHaveBeenCalledTimes(1);
    });
});
