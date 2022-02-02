# New orientation:
We switched the focus to creating a database storing metadata scratching from the hub.
- We switched b/c the last didn't let to the possibility for developing a nice data warehouse. Mostly b/c the data was to simple and there was not enough of it. The interessting stuff happens when there is messyness going on with data and simple solutions (like using .csv or pickel) reaches its limitations. It gets even more interessting when you have multiple things going on that have no easy solution for the communication between them!
# Main Objective:
- __Downloading as much data as possible.__ Kategories, Tags, title, everything that we can scratch instantly
- Regularly revisit videos for creating a history of their views
- check apache spark (than decide which technology to use, b/c spark uses multiple technologies)
### libraries of use:
- [This](https://github.com/sskender/pornhub-api) for ratings, duration, link and [this](https://github.com/Derfirm/pornhub-api) for tags, kathegories.
### possible next projects:
- create database based on measured data (video of street, audio recording of whatever, maybe even some bluetooth mobile tracking thing)
- [Common Crawl](http://commoncrawl.org/) is a provider of LOOTTSSS of data to play with. [Here](https://vdocuments.mx/reader/full/introduction-to-common-crawl) is a presentation collectiong some basic stuff from them. (One might also check the [wiki](https://en.wikipedia.org/wiki/Common_Crawl)). [Here](https://github.com/haydenhw/commoncrawl-emr-tutorial) is also a nice project using it (and even some basic AWS for 50 cents of so, so something we could also try!)
