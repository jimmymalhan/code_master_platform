// tests/expensiveFunction.test.ts
// Tests to ensure that the expensiveFunction only fetches data once when memoized.
import { expensiveFunction } from '../src/expensiveFunction';
import { memoizeAsync } from '../src/memoizeAsync';

jest.mock('../src/expensiveFunction', () => ({
    expensiveFunction: jest.fn()
}));

describe('expensiveFunction', () => {
    it('fetches data only once when memoized', async () => {
        const mockFunction = jest.fn(() => Promise.resolve('Mocked data'));
        const controller = new AbortController();
        const memoizedFunction = memoizeAsync(mockFunction);

        const firstCall = await memoizedFunction(controller.signal);
        const secondCall = await memoizedFunction(controller.signal);

        expect(firstCall).toBe('Mocked data');
        expect(secondCall).toBe('Mocked data');
        expect(mockFunction).toHaveBeenCalledTimes(1);
    });
});
