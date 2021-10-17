class Solution:
    def __init__(self, string: str):
        self.string = string

    def toQuestion(self):
        pass
            
def main():
    givenString1 = Solution("enter_string")
    print(givenString1.toQuestion())

    givenString2 = Solution("enter_2nd_string")
    print(givenString2.toQuestion())

if __name__ == '__main__':
    main()