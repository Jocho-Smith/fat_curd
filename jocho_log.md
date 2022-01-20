## Next step:
- write a function (with comments, tests, proper format for python, ...) that takes the concatinated list thing from BeautifulSoup and returns a pandas file that saves the calculates label
## Informative stuff:
- Read [this](https://www.astera.com/type/blog/what-is-data-warehousing/) and write a short summary
- Go through the lecture slides and write a short summary
- Check [this](https://www.dataengineering.academy/pipeline-data-engineering-academy-blog/the-data-engineering-portfolio-project) site and its projects (ecpacially the one with the hiphop recommendation thing)
. Watch an introductino about AWS (What are the gains of using cloud based servises? What do everybody mean with 'learn cloud computing'? If it's just storing data remotely we can also mimic it for this project).
- html5 reinziehen for proper web scraping. [These](https://www.w3schools.com/) guys do a good job for the first contact! Also for php, js, css, ... So maybe I could check out all of it XD (also [here](https://codepen.io/) is a nice tool for testing html,css,js stuff)
- Create a seperate venv for this project! (For now I just use my default one!)
- Do a custom `git qcommit` command for easy generated commit messages (like github is doing that as default)

## log:
### (28.12.21) 
- started today, not clear what exactly to work on. So first research about basics and possible projects. 
- learned about 'git config --global credential.helper store' and '$PS1' today
### (02.01.22)
- Here are the two networks we might use (from Hugging Face): [Sentiment analysis for text](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis) and [Speech Emotion Recognition](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis). ([Here](file:///C:/Users/MONTAP~1/AppData/Local/Temp/kisang.pdf) some rough overview over the technique and [Here](https://ai.facebook.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/) a facebook post on the network.)
### (03.01.22)
- For the first time (finaly) a got a conflict in git b/c of merging the `README.md`. I fixed it with `git mergetool` and than used git merge. However, this went not perfectly fine, b/c I created some strange `README.md.orign` file that I had to delete afterwards. So It's not perfectly understood, but I'll continue working on it.
- I also checked if there is the possibility to make easy commit messages (like github is doing them autimaticaly), but I've only found customizations that have a fixed text instead of some variables that already contain keywords like the action (e.g. 'delete') or the filename that it acted on. So I'll just continue doing that for now. (Update: there is a way of thing it with I could deepen my knowledge of unix bash scripting, grep, sed. Check it out [here](https://stackoverflow.com/questions/35010953/how-to-automatically-generate-commit-message)).
### (09.01.22)
- confusion with transformers pretrained networks (huggingface) and the `pysentimento` library. Non of them worked. Maybe I should set up everything from the beginning. Especially b/c I install many things that take up much space, but don't know how to delete it afterwards... So maybe I should take care of that as well. 
- It however worked out with the pipelines on theiy main page (So a model that is not the same as the one I've found in the first place!)
- (checking out the disk space afterwards it seams like that stuff is stored in some cashe b/c I got my 1GB back!)
