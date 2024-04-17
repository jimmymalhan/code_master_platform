"use strict";
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
const memoizeAsync_1 = require("../src/memoizeAsync");
jest.mock('../src/expensiveFunction', () => ({
    expensiveFunction: jest.fn()
}));
describe('expensiveFunction', () => {
    it('fetches data only once when memoized', () => __awaiter(void 0, void 0, void 0, function* () {
        const mockFunction = jest.fn(() => Promise.resolve('Mocked data'));
        const controller = new AbortController();
        const memoizedFunction = (0, memoizeAsync_1.memoizeAsync)(mockFunction);
        const firstCall = yield memoizedFunction(controller.signal);
        const secondCall = yield memoizedFunction(controller.signal);
        expect(firstCall).toBe('Mocked data');
        expect(secondCall).toBe('Mocked data');
        expect(mockFunction).toHaveBeenCalledTimes(1);
    }));
});
