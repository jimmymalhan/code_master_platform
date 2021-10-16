class Solution:
    def __init__(self, array):
        self.array = array

    # O(n^2) time | O(n) space - where n in the length of the array
    def arrayOfProducts1(self):
        products = [1 for _ in range(len(self.array))]

        for i in range(len(self.array)):
            runningProduct = 1
            for j in range(len(self.array)):
                if i != j:
                    runningProduct *= self.array[j]
            products[i] = runningProduct
        return products
    
    # O(n) time | O(n) space - where n in the length of the array
    def arrayOfProducts2(self):
        products = [1 for _ in range(len(self.array))]
        leftProducts = [1 for _ in range(len(self.array))]
        rightProducts = [1 for _ in range(len(self.array))]

        leftRunningProduct = 1
        for i in range(len(self.array)):
            leftProducts[i] = leftRunningProduct
            leftRunningProduct *= self.array[i]
        
        rightRunningProduct = 1
        for i in reversed(range(len(self.array))):
            rightProducts[i] *= rightRunningProduct
            rightRunningProduct *= self.array[i]
        
        for i in range(len(self.array)):
            products[i] = leftProducts[i] * rightProducts[i]
        
        return products

    # O(n) time | O(n) space - where n in the length of the array
    def arrayOfProducts3(self):
        products = [1 for _ in range(len(self.array))]

        leftRunningProduct = 1
        for i in range(len(self.array)):
            products[i] = leftRunningProduct
            leftRunningProduct *= self.array[i]
        
        rightRunningProduct = 1
        for i in reversed(range(len(self.array))):
            products[i] *= rightRunningProduct
            rightRunningProduct *= self.array[i]
        
        return products

def main():
    givenArray = Solution([5,1,4,2])
    # print(givenArray.arrayOfProducts1())
    # print(givenArray.arrayOfProducts2())
    print(givenArray.arrayOfProducts3())

if __name__ == '__main__':
    main()