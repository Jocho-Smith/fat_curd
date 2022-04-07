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
### (23.01.22)
- relational und nicht relational: relational bedeutet, dass mein verschiedene unterklassen einer hauptklasse hat die unabhaenig von einander sind. (Also fuer personen, die kunden sind nicht viele 'null Werte' in zeilen wo attribute fuer angestellte stehen.) bei nicht relationalen ist man freier. 
- streng(SQL) > streng(non-SQL) > streng(nicht-relational) 
- focus switch zu konzepten auf die Thomas bock hat.

# Zwischenbilanz(07.04.22)
Questions to answer:
- What happened so far? (What code was written, what was the goal, motivation, )
- What will hapen this semester (SS22)?
- What will happen next and how can we apply the following points (7SS) in future projects?
	- Community (Network)
	- Support
	- Guidance
	- Accountability
	- Credentials
	- Feedback
	- Content

## What happened so far?
- We had 3 meetings or so and than other stuff was more important (health, job, vacation) $->$ This lets me conclude that didn't had enough motivation or reason to work on the project. Which is perfectly right regarding the messiness and lack of many things (7SS).
- The code can be seen in github, but it's just copy paste from blog posts so nothing fancy happening here
- We evelulated a lot about the concepts we want to familarize ourself with, why that is (who is interessted in that), and how we could 'playfully' incoorperate it into our small procjects. Some examples:
	- Cloud servises. And instead of 'learning' AWS we planed to use an RPi to implement some remotely controlled device. 
	- Data Warehouse technologies (SQL, pipelines)
	- Crash coursing front-/backend development (Building some web interface for our RPi application, whatever this might be)
- We thought about possible projects and considered the value for potential employers (credentials/portfolio)

## What will hapen this semester (SS22)?
Nothing. At least from my side. Maybe Thomas will play with the RPi. 
- I still would call this project (so far) a success, b/c we investigated in currently relevent technologies and both of us were be abel to find a job in that regions. So we will continue learning about these topics and also getting paied for it. 

## What will happen next and how can we apply 7SS in future projects
### Community 
- Maybe it would be nice to contribute to a challange or hackerthon that requires our knowledge. That way we could team up to do something others can evaluate
### Support
- Find someone with more experience who can help us during the process (maybe Markus). This does not mean that he will 'correct' our code like a tutor is supposed to do. But more in anwsering the question 'hey, would you solve that promlem like that too?' 
### Guidance
- It may also be enough to first just work through some tutorials 'together' to learn about tools better. For example some udemy course/zlibrary cookbook/online study platform about basic frontend (html,css,js) and backend (django). 
- I honestly have no experience with being guided while exploring on my own? I didn't learn that in the physics bachelor thesis, but may learn it during my master thesis. 
- We might guide ourselfs as soon as we have enough experience of how the single steps will look like, that will bring us to our result.
### Accountability
- That's a tough one. We could try to enduce some suffering or so to our meetings or have some more people in the boad to make the pressure higher. This is a bit superficial though. The ideal would be that we continue doing it b/c we enjoy it, but this will not always be the case. 
- I don't know how Thomas usualy handels this issue and I'm not sure if I can guide him to do that. I know though that when the recourses are available to me,  I can addopt the efford according to stress level and time available and the task is clear/motivating/interessting I will scaduele it and make it a habit!
### Credentials
- This does not have to be a portfolie or webpage. It could also be a "I've worked through this book" or I've modified this code/application.
- I have the feeling that we thought about this too early too much, so for the next step be a bit more chill and realistic about this
### Feedback
- Here again some more eperienced opinion (Markus?, Thomas info kollegen?). Not that easy go get though
- As soon it becomes an application we can talk to users, but this is not in reach so far, and should also not be the main objective in my opinion, b/c that we would start to do basics slopy which is not in my interesst at the moment. 
- Here again some book/course with 'solutions' could be the feedback. 
- We may give the feedback to ourselfs! For that if might be benificial to learn how to give proper feedback and how to properly ask for it.
### Content
- Finding the rough objective was easy in the past, but converging to the concrete steps reaching it was a bigger problem. Here again maybe do some projects in the end of educational books first.  Like the python software engineering book.
- In the case of a course/book this is not a problem. 
## Quick summary 
- Check if you can find some educational recourse (book, ...) that can provide us with a nice introduction into one of the topics of interesst (see the readmes of the both ideas we had.)
- Forget about the stuff you have done sofar. Don't try to force it's completion. Keep it's development as dynamic as possible. 
- Stay with regular meetings! At least a phone call once a week talking about what was done. If nothing was done, fine. Think about another reorientation or be just fine with it, but don't force time into a dead boring project. 
