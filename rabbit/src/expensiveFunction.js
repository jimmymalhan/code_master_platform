"use strict";
// src/expensiveFunction.ts
// Purpose: Defines an asynchronous function to fetch data from a URL.
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
exports.expensiveFunction = void 0;
// Fetches data from a URL and handles abort signals.
function expensiveFunction(signal) {
    return __awaiter(this, void 0, void 0, function* () {
        console.log('Fetching data...');
        try {
            const response = yield fetch("https://example.com/data", { signal });
            if (!response.ok) {
                throw new Error(`Failed to fetch: ${response.statusText}`);
            }
            return response.text();
        }
        catch (error) {
            console.error('Fetch error:', error.message); // Type assertion to Error
            throw error;
        }
    });
}
exports.expensiveFunction = expensiveFunction;
