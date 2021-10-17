# Check if Numbers Are Ascending in a Sentence

class Solution:
    def __init__(self, s: str):
        self.s = s

    def areNumbersAscending(self):
        letter = [int(i) for i in self.s.split() if i.isdigit()]
        for i in range(len(letter)):
            for j in range(i + 1, len(letter)):
                if letter[i] >= letter[j]:
                    return False
        return True


def main():
    givenArray1 = Solution("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s")
    print(givenArray1.areNumbersAscending())
    givenArray2 = Solution("hello world 5 x 5")
    print(givenArray2.areNumbersAscending())
    givenArray3 = Solution("36 claim 37 38 39 39 41 hire final 42 43 twist shift young 44 miss 45 46 sad 47 48 dig 49 50 green 51 train 52 broad 53")
    print(givenArray3.areNumbersAscending())

if __name__ == '__main__':
    main()