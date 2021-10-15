# Read the HTML file and print the results
from requests_html import HTML, HTMLSession
# importing HTML for parsing local HTML file
# importing HTMLSession for parsing HTML from website 

class parsingHTMLfrom:
    def file():
    # Method 1
        # file = open("simple.html", "rt")
        # print(file.read())
        # or
 
# IN-USE (uncomment me) | Method 2
        with open("simple.html") as html_file:
            source = html_file.read()
            html = HTML(html=source)
        print(html.text) # shows the text without tags taken out

    # Find the "title"
    # Method 1
        # match = html.find('title')
        # print(match) # shows the whole block for Title
        # print(match[0]) # shows the contents of the block
        # print(match[0].html) # shows the block for html
        # print(match[0].text) # only shows the the text

    # or Method 2
    
    # """Note: 
    
    # first=True is replace by index [0] to use that as default to pick up ""div"" instead of returning the list of ""div"s"
    # """
    
        # find only the block title and not the whole list
        # match = html.find('title', first=True)

    # Find the "footer"
        # match = html.find('#footer', first=True) 
        # print(match.text)
    # Contains the contents of "div"(first) and shows the contents of headline and summary
        # article = html.find('"div".article', first=True) 
        # print(article.text)
    # Seperate the contents first "div" to show headline and summary
        # article = html.find('"div".article', first=True) 
        # headline = article.find('h2', first=True).text
        # summary = article.find('p', first=True).text
        # print(headline)
        # print(summary)
    
# IN-USE (uncomment me)| Returing the list of all articles in "div" by      removing first=True
        articles = html.find('div.article')
        for article in articles:
            headline = article.find('h2', first=True).text
            summary = article.find('p', first=True).text
            print(headline)
            print(summary)
            print() # empty print spread out the ouput
    
    def website():
        # Grabbing - Headline, Summary, YoutubeLink in this function
        session = HTMLSession()
        response = session.get('https://coreyms.com/')

        # 1) Article # Output of the website in HTML for first article because "first=True"
        article = response.html.find('article', first=True)
        # print(article.html) # file is created for referenc for first article ONLY- first_article_from_website.html
        
        # 2) Headline # In the article > header > Under H2 class shows > headline class "entry-title-link"
        # headline = response.html.find('.entry-title-link', first=True).text
        # or
        headline = article.find('.entry-title-link', first=True).text
        print(headline)
        # To Do:
            # - Summary
            # - YoutubeLink

if __name__ == "__main__":
    # parsingHTMLfrom.file() # parsing HTML from local file
    parsingHTMLfrom.website() # parsing HTML from website