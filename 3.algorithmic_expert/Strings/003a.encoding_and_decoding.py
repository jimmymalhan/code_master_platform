# compress and decompress string in python
# input: aaabbbbccc 
# output: a3b4c3 
# and decompress it

class Solution:
    def __init__(self):
        self.dic = {}
        self.count = 0
        self.compressed = ''
        self.decompressed = ''

    def compress(self, s):
        self.count = 0
        self.dic = {}
        for i in range(len(s)): # i is the index of s
            if s[i] not in self.dic: # if s[i] is not in dic
                self.dic[s[i]] = 1 # add s[i] to dic
            else:
                self.dic[s[i]] += 1 # if s[i] is in dic, add 1 to the value
        for key in self.dic: # for each key in dic
            if self.dic[key] == 1: # if the value of key is 1
                self.compressed += key # add key to compressed
            else: # if the value of key is not 1
                self.compressed += key + str(self.dic[key]) # add key and value to compressed
        return self.compressed

    def decompress(self, s):
        #input: a3b4c3
        #output: aaabbbbccc
        start = 0
        end = 0
        while end < len(s): # while end is less than the length of s
            while end < len(s) and not s[end].isdigit(): # if s[end] is not a digit
                end += 1 # add 1 to end
            self.decompressed += s[start:end] * int(s[end]) # add s[start:end] * int(s[end]) to decompressed # s[end] is a digit
            start = end + 1 # start is the index of s after end
            end = start # end is the index of s after start
        return self.decompressed



def main():
    s = Solution()
    print(s.compress('aaabbbbccc'))
    print(s.decompress('a3b4c3'))

if __name__ == '__main__':
    main()