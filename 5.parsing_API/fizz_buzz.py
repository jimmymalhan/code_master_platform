# fizz buzz

# O(n) time complexity and O(1) space complexity
class FizzBuzz:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def fizz_buzz(self):
        for i in range(self.start, self.end + 1):
            if i % 15 == 0:
                print('FizzBuzz')
            elif i % 3 == 0:
                print('Fizz')
            elif i % 5 == 0:
                print('Buzz')
            else:
                print(i)
    
    def fizz_buzz_v2(self):
        for i in range(self.start, self.end + 1):
            print(('FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i))

def main():
    fizz_buzz = FizzBuzz()
    # fizz_buzz.fizz_buzz()
    fizz_buzz.fizz_buzz_v2()

if __name__ == '__main__':
    main()