# print max(dictionary.values())
class Solution:
    def minimum_value(self, dictionary):
        return min(dictionary.values())

    def maximum_value(self, dictionary):
        return max(dictionary.values())


def main():
    dictionary = {'a': 11, 'b': 2, 'c': 3}
    print(Solution().minimum_value(dictionary))
    print(Solution().maximum_value(dictionary))

if __name__ == '__main__':
    main()