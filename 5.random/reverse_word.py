string = 'foo bar'

###### reverse every 2nd word ######
# string = 'foo bar'
# print(string[1]) # prints o
# print(string[:1]) # prints f
# print(string[::1]) # prints foo bar (whole string)
# words = string.split()
# for i in range(len(string)):
#     print(words[i]) # print the items in the word (list)

# 1) convert string to list 
# 2) count the elements in the list 
# 3) divide the list elements for odd index numbers and reverse them
# 4) join the list and print it


# words = string.split()
# reverse = []
# i = 0
# while i < len(words):
#     if i % 2 == 1:
#         reverse.append(words[i][::-1])
#     else:
#         reverse.append(words[i])
#     i += 1
# print(" ".join(reverse))

words = string.split()
reverse = []
for i in range(len(words)):
    if i % 2 == 1:
        reverse.append(words[i][::-1])
    else:
        reverse.append(words[i])
print(" ".join(reverse))

########## reverse all the words ##############
# def reverse_whole_string(string):
#     words = string.split(" ")
#     words = list(reversed(words))
#     return " ".join(words)

# print(reverse_whole_string(string))
# or 
# r = ' '.join(reversed(string.split(' ')))
# print(r)

####### reverse each word in a sentence #######
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