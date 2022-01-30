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
