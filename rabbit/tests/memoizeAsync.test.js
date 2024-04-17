"use strict";
// tests/expensiveFunction.test.ts
// Tests to verify that the expensiveFunction only fetches data once when memoized.
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
const expensiveFunction_1 = require("../src/expensiveFunction");
const memoizeAsync_1 = require("../src/memoizeAsync");
describe('expensiveFunction', () => {
    it('fetches data only once when memoized', () => __awaiter(void 0, void 0, void 0, function* () {
        const mockFunction = jest.fn(expensiveFunction_1.expensiveFunction);
        const controller = new AbortController();
        const memoizedFunction = (0, memoizeAsync_1.memoizeAsync)(mockFunction);
        try {
            yield memoizedFunction(controller.signal);
            yield memoizedFunction(controller.signal);
        }
        catch (error) {
            console.log('Handled fetch error in test:', error);
        }
        expect(mockFunction).toHaveBeenCalledTimes(1);
    }));
});
