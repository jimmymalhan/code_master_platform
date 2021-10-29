# fizz buzz

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

def main():
    fizz_buzz = FizzBuzz(1, 100)
    fizz_buzz.fizz_buzz()

if __name__ == '__main__':
    main()