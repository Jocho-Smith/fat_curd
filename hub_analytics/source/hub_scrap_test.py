#%% Baisc usage of pornhub-api-package
## Scraps the first 10 videos from page 2

import pornhub
client = pornhub.PornHub()

videos_data_raw = client.getVideos(10, page=2) # Get first 10 videos from page 2

videos_data = [vid for vid in videos_data_raw]        # videos_data_raw is a generator_type? which can be iterated via for loop. (But not indexed directly)


#%% How to get updated data for a already existing video file via URL using BeatuifulSoup-library
# TODO: Extend the pornhub-api repository with functionality to scrap url
import requests # HTML package
from bs4 import BeautifulSoup as bs # Webscrapping package

video_url = videos_data[0]['url']

def get_views_count(url: str) -> int:
    """Parse url article and return curernt view count of video"""

    article = requests.get(url)               # returns the html-code of URL
    soup = bs(article.content, "html.parser") # creates BeatifulSoup-Object from the html-code
    views = soup.find(class_='count').text    # Searches for 'count'-class-describtion inside html-code & transforms into string
# TODO: Slice string: K->1000. M-> 10^6 usw.
    return views

views_updated = get_views_count(video_url)
