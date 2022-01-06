# Notes on that Project
|Question|Answer|
|---|---|
|Why?|build a portfolio for job applications and learn/deepen data engineering skills (80/20)|
|When?|start with year 2022, every sunday after workout, first work together in one room|
|Importance|only uni and other responsabilities are more importent. The rest (girls, bad mood, ...) will not be exepted. (Maybe we need some punishment? XD)
|How much time?|5h per week (on that sunday)|
|Finished project| __We first need a more precise idea of what we do before we can decide on when we're done__|
# Project ideas:
## Emotion of news:
Many people state that they don't listen to the news b/c it makes them unhappy. So a collection of news that make one feel happy or are presented in a pleasing way have a better chance to be seen. So the idea is to create a dataset of some current news, and predict its emotion. Topic and reliability is not that important for now. 

So the rough structure would be:
- Find some source for the data (maybe even first an already existing API). __Audio files__
- Create a dataset/warehouse/__I don't know anything about the details here__ (local,cloud,?)
- Use [this](https://huggingface.co/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition) speech-emotion-recognition network to make a prediction about the emotion of the speaker.


### Some techniques/languages/skills we wish to apply/learn:
- Data warehousing
- databank post gres (?)
- SQL (what is it, when to use it/when not, who uses it, when and why using alternatives)
- Kubernets
- Azure(Microsoft Cloud) / AWS (Cloud services in general)
- **Docker** (e.g. server-deployment/ application deployment if seperated)
- **CI/CD (Testing!)**
# Open Questions:
- How to set up Web server based on Apache/ PHP8 / MySQL in linux [here](https://dev.to/aitorsol/wsl2-windows-linux-subsystem-a-guide-to-install-a-local-web-server-ubuntu-20-04-apache-php8-y-mysql8-3bbk)[alternative](https://www.makeuseof.com/tag/build-linux-web-server-computer-part-1/)
- shell application vs. webpage
- can one create multiple github.io web sites or just one per account?
- should we use an API or build on ourself?
- How much data science/ML should we apply here?
- in git: what is the difference between `fetch` and `pull`?
- Organization repository or normal account?
- How does `diff` in github work? (I tried to check the difference between my local main and the main on github, but didn't get any message. Anyway, I need something to check this.)
- Webscrapping (LEGAL?)
- Why cloudstorage instead of local?
- Which cloud storage?
# Answered Questions:
## Webscraping tool we will use:
- BeautifulSoup (guide: https://towardsdatascience.com/super-simple-way-to-scrape-bbc-news-articles-in-python-5fe1e6ee82d9)

## Storage/Computation
- Cloud Services can provide servers, storage, databases, networking, software, analytics, and intelligence—over the Internet.
- Raspery Pi Server (https://airflow.apache.org/docs/)
