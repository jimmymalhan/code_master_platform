class Solution:
    def __init__(self,s: str):
        self.s = s

    def areNumbersAscending(self):
        letter = [int(i) for i in self.s.split() if i.isdigit()]
        if sorted(letter):
            return True
        return False
        # for i in range(len(letter)):
        #     for j in range(len(letter)):
        #         if letter[j] < letter[j+1]:
        #             return True
        #     return False

def main():
    givenArray = Solution("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s")
    print(givenArray.areNumbersAscending())

if __name__ == '__main__':
    main()