
import requests
from bs4 import BeautifulSoup as bs

#BeaufifulSoup functions
"""
find(element_tag, attribute) #return first matching item
find_all(element_tag, attribute) #return list of matching items
"""

class BBC:
    def __init__(self, url:str):
        article = requests.get(url)
        self.soup = bs(article.content, "html.parser")
        self.body = self.get_body()
        self.title = self.get_title()
        
    """    
    def get_body(self) -> list:
        body = self.soup.find(property="articleBody")
        return [p.text for p in body.find_all("p")]
    """
    
    def get_title(self) -> str:
        body = self.soup.find(class_=v_class).text
        return [p.text for p in body.find_all("p")]

    
    
if __name__ == "__main__":
    url = "https://www.bbc.com/news/world-africa-59850904"; #Webside URL
    v_class = "ssrcss-1mc1y2-ArticleWrapper e1nh2i2l6"      #Innermost html element class which encapsulates content of interest (Can also be html property)
    
    bbc = BBC(url)
    s = get_bbc_text(url)
    
    
# file = open("test_scratch.txt", "w")
# file1.write(s)
