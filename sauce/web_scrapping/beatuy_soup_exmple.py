
import requests
from bs4 import BeautifulSoup as bs

"""
find(element_tag, attribute) #return first matching item
find_all(element_tag, attribute) #return list of matching items
"""

url = "https://www.bbc.com/news/world-africa-59850904";
v_class = "ssrcss-1mc1y2-ArticleWrapper e1nh2i2l6"

def get_bbc_text(url:str) -> list:
    """Parse bbc article and return text in list of strings"""
    
    article = requests.get(url)
    soup = bs(article.content, "html.parser")
    body = soup.find(class_=v_class)
    text = [p.text for p in body.find_all("p")] 
    return text
    
    
s = get_bbc_text(url)
    

# file = open("test_scratch.txt", "w")
# file1.write(s)