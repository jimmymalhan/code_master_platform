# Read the HTML file and print the results
from requests_html import HTML, HTMLSession
# importing HTML for parsing local HTML file
# importing HTMLSession for parsing HTML from website 

import csv

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
    
        """
        Note: 
        
        first=True is replace by index [0] to use that as default to pick up ""div"" instead of returning the list of ""div"s"
        """
    
        # find only the block title and not the whole list
        # match = html.find('title', first=True)

    # Find the "footer"
        # match = html.find('#footer', first=True) 
        # print(match.text)
    # Contains the contents of "div"(first) and shows the contents of headline and summary
        # article = html.find('"div".article', first=True) 
        # print(article.text)
    # Separate the contents first "div" to show headline and summary
        # article = html.find('"div".article', first=True) 
        # headline = article.find('h2', first=True).text
        # summary = article.find('p', first=True).text
        # print(headline)
        # print(summary)
    
# IN-USE (uncomment me)| Returing the list of all articles in "div" by    removing first=True
        articles = html.find('div.article')
        for article in articles:
            headline = article.find('h2', first=True).text
            summary = article.find('p', first=True).text
            print(headline)
            print(summary)
            print() # empty print spread out the ouput
    
    def website():
        
        """
        ########
        # Method 1 - For first Article ONLY

        Function contains - 
            1. Article
            2. Headline
            3. Summary/Description(paragraph)
            4. YoutubeLink 
                a) YoutubeID
                b) Creates new Youtube link with the above fetched ID.
        """
        ########
        # Method 1 - For first Article ONLY
        ########
        # session = HTMLSession()
        # response = session.get('https://coreyms.com/')

        # # 1) Article # Output of the website in HTML for first article because "first=True"
        # article = response.html.find('article', first=True)
        # # print(article.html) # file is created for referenc for first article ONLY- first_article_from_website.html
        
        # # 2) Headline # In the article > header > Under H2 class shows > headline class "entry-title-link"
        # """
        # Note:  You can use headline class "entry-title-link" in this manner -> ".entry-title-link"
        # """
        # # headline = response.html.find('.entry-title-link', first=True).text
        # # or
        # headline = article.find('.entry-title-link', first=True).text
        # #print(headline)
        
        # """
        # Note:  You can use paragraph class "entry-title-link" in this manner -> ".entry-title-link"
        # """
        # # 3) Summary/Description - (paragraph)
        # summary = article.find('.entry-content p', first=True).text
        # #print(summary)
        
        # # 4) YoutubeLink and Youtube ID (z0gguhEmWiY?)
        
        # # Method 1
        # # video_src = article.find('iframe', first=True)
        # # # print(video_src.html)
        # # # print(video_src.attrs) # accessing attributes
        # # print(video_src.attrs['src']) # accessing attributes in source dictionary
        # # or 

        # # Method 2
        # video_src = article.find('iframe', first=True).attrs['src']
        # # print(video_src) # accessing attributes in source dictionary

        # # 4.a) Youtube ID
        # # video_id = video_src.split('/') # splitting the video URL(list) based on / to output as Dictionary
        # video_id = video_src.split('/')[4].split('?')[0] # splitting at 4th Index and splitting again at '?' to fetch index 0
        
        # # print(video_id) # shows Youtube video_id

        # # b) Creates new Youtube link with the above fetched ID.
        # youtubeLink = f'https://youtube.com/watch?v={video_id}'
        # print(youtubeLink) # open the output link and it should redirect and works

        """
        ########
        # Method 2 - Loop through ALL the articles and creates following:

            1. Article
            2. Headline
            3. Summary/Description(paragraph)
            4. YoutubeLink 
                a) YoutubeID
                b) Creates new Youtube link with the above fetched ID.
            5. CSV
                a) Parse the contents to CSV
                b) Add the contents to CSV
        """
        # 5a) Parse the contents to CSV
        csv_file = open('html_parse.csv', 'w')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Headline', 'Summary', 'Video']) # headers of the file

        session = HTMLSession()
        response = session.get('https://coreyms.com/')

        # 1) Article # Loop through the article
        articles = response.html.find('article')
        for article in articles:
            headline = article.find('.entry-title-link', first=True).text
            print(headline)

            summary = article.find('.entry-content p', first=True).text
            print(summary)
            
            try:
                video_src = article.find('iframe', first=True).attrs['src']
                video_id = video_src.split('/')[4].split('?')[0] # splitting at 4th Index and splitting again at '?' to fetch index 0

                youtubeLink = f'https://youtube.com/watch?v={video_id}'

            except Exception as e:
                youtubeLink = None # if the video link doesn't exist outputs 'None'
            
            # print(video_src) # accessing attributes in source dictionary
            print(youtubeLink) # open the output link and it should redirect and works
            print() # separating out the outputs
        
        # 5b) Add the contents to CSV
            csv_writer.writerow([headline, summary, youtubeLink])

        csv_file.close()

if __name__ == "__main__":
    # parsingHTMLfrom.file() # parsing HTML from local file
    parsingHTMLfrom.website() # parsing HTML from website