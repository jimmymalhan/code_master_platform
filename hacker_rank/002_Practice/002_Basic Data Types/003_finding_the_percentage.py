# marks key:value pairs
#'alpha':[20, 30, 40]
#'beta':[30, 50, 70]
# query_name = 'beta'
# query_name in beta average score (30 + 50 + 70)/3 = 50.0

# Constraints:
# 2 <= n <= 10
# 0 <= marks[i] <= 100
# length of marks arrays = 3

#Output
# print one line that average of the marks obtained 
# by the particular student correct to 2 decimal places

# Sample input:
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# Sample Output
# 56.00

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
# enter your code here
query_scores = student_marks[query_name]
print('{0:.2f}'.format(sum(query_scores)/len(query_scores)))