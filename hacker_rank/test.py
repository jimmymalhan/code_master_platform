# can someone please explain - Nested loop concept with an example for below
#     for i in range(n):
#         for j in range(i + 1, n):


# lets say n = 7 
# range(7) is an iterator that produces 0, 1, 2, 3, 4, 5, 6 in that order.
# range(3, 7) is an iterator that produces 3, 4, 5, 6
# so now you could just print this out to see some output like

# n = 7
# for i in range(n):
#     for j in range(i, n):
#         print(i, j)


a=[1,2,3,h,7,4,9]

for i in range(O, len(a)):
    if(a[i].isalpha()):
        print(a[i+1])