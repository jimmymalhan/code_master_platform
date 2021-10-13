from requests_html import HTML

# Read the HTML file and print the results
class MyClass:
    def Solution():
        # file = open("simple.html", "rt")
        # print(file.read())
        # or
        
        with open("simple.html") as html_file:
            source = html_file.read()
            html = HTML(html=source)
        print(html.html)

if __name__ == "__main__":
    MyClass.Solution()
