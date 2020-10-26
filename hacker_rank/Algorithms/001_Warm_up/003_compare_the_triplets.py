# a = (a[0], a[1], a[2]) = (5,6,7) #alice
# b = (b[0], b[1], b[2]) = (3,6,10) # bob

# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point. 

# a[0] > b[0], so Alice receives 1 point
# a[1] = b[1], so nobody receives a point
# a[2] < b[2], so Bob receives 1 point

def compareTriplets(a, b):
    a_score, b_score = 0, 0
    for i in range(3):
        a_score += a[i] > b[i]
        b_score += a[i] < b[i]
    return [a_score, b_score]