from requests_html import HTML

# Read the HTML file and print the results

def Solution():
    file = open("simple.html", "rt")
    print(file.read())

if __name__ == "__main__":
    Solution()
