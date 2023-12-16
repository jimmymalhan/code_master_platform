"""
Example Dataset:{
"titles": {
"Stranger Things": 300,
"The Crown": 200,
"Black Mirror": 180,
"Money Heist": 300,
"Bojack Horseman": 150,
"The Witcher": 300,
"Ozark": 180,
"The Umbrella Academy": 200,
"Narcos": 150,
"Dark": 180
"k": 3

Expected Output:
Based on the dataset, your algorithm should return the top 3 titles based on viewership. In this case, the output might be ["Stranger Things", "Money Heist", "The Witcher"], as each of these shows has 300 views

Constraints- 
if the duplicate counts, return any top 3 counts
"""
import heapq

def get_top_k_shows(shows, k):
    # Use a heap to keep track of top-k elements.
    # The heap has -viewership as key because heapq is a min-heap and we want max-viewership shows.
    # For example, if shows = {"Stranger Things": 300, "The Crown": 200, "Black Mirror": 180},
    # then top_k_heap = [(-300, "Stranger Things"), (-200, "The Crown"), (-180, "Black Mirror")]
    
    top_k_heap = [(-viewership, show) for show, viewership in shows.items()]
    
    # Transform the list into a heap in O(n) time
    # 
    heapq.heapify(top_k_heap)
    
    # Extract show names from the heap in O(k log n) time
    # top_k_heap = [(-300, "Stranger Things"), (-200, "The Crown"), (-180, "Black Mirror")]
    top_k_shows = [heapq.heappop(top_k_heap)[1] for _ in range(k)]
    
    # Reverse because they're in increasing order of viewership
    #     top_k_shows.reverse() = ["Stranger Things", "Money Heist", "The Witcher"]
    top_k_shows.reverse()

    return top_k_shows


if __name__ == '__main__':
    shows = {
        "Stranger Things": 300,
        "The Crown": 200,
        "Black Mirror": 180,
        "Money Heist": 300,
        "Bojack Horseman": 150,
        "The Witcher": 300,
        "Ozark": 180,
        "The Umbrella Academy": 200,
        "Narcos": 150,
        "Dark": 180
    }
    k = 3
    print(get_top_k_shows(shows, k)) # ["Stranger Things", "Money Heist", "The Witcher"]