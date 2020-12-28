string = 'foo bar'

# Make list of string then go to alternate words then reverse those words itself in that list
words = string.split(" ")
for i in words:
    print(i, i+1, end=' ')
# print( " ".join(words))

# print(string[1]) # prints o
# print(string[:1]) # prints f
# print(string[::1]) # prints foo bar (whole string)


# reverse all the words
# def reverse_whole_string(string):
#     words = string.split(" ")
#     words = list(reversed(words))
#     return " ".join(words)

# print(reverse_whole_string(string))
# or 
# r = ' '.join(reversed(string.split(' ')))
# print(r)

# # reverse each word in a sentence
# def reverseWordSentence(string): 
#     words = string.split(" ") 
#     newWords = [word[::-1] for word in words] 
#     newSentence = " ".join(newWords) 
#     return newSentence 

# print(reverseWordSentence(string)) 

# def reverse_every_second_word(string):
#     words = string.split("/n")
#     print([word[::1]])
# print(reverse_every_second_word(string))