import requests # HTML package
from bs4 import BeautifulSoup as bs # Webscrapping package
import pickle as pkl# Save/Load data package
#import urllib # Fetch url's
import time

"""
find(element_tag, attribute) #return first matching item
find_all(element_tag, attribute) #return list of matching items
"""

url_list = ["https://www.bbc.com/news/world-australia-59926777", "https://www.bbc.com/news/world-africa-59850904"]

article_class = "ssrcss-1mc1y2-ArticleWrapper e1nh2i2l6" # HTML class which contains the text-body.



def get_bbc_text(url: str) -> list:
    """Parse url article and return heading, text as list of strings"""

    article = requests.get(url)
    soup = bs(article.content, "html.parser")
    heading = soup.find(id="main-heading").text
    body = soup.find(class_=article_class)
    text = [p.text for p in body.find_all("p")]
    return heading, text


content_list = []

for website in url_list:
    heading, text = get_bbc_text(website)
    content_list.append([heading, text]) # Appends the contents of the webpage as [[...], [[heading], [text1, text2,..]]]
    time.sleep(2)

with open("scratch_test.txt", "wb") as file:
    pkl.dump(content_list, file)


with open("scratch_test.txt", "rb") as file:
    contents_loaded = pkl.load(file)
