## Web Scrapping

#### How do you automate web scrapping without having to check manually every time? 
- In the case of BBC, each article uses the same HTML class to mark up the text-content-body. So it is possible to just scarp articles just by knowing the URL.

- To not allert the server about to much traffic, include a delay in your loop. e.g. sleep(2).. Waits 2 Seconds

- Since we are focusing us on the html elements of a webpage when scrapping, we may want to disable js and css.
  - To disable js open inspection window in your browser, press ctrl+shift+p and enter javascript. Find end execute "DISABLE JAVASCRIPT"


## Database

#### Choosing wether to use the plain file-system or database-system.\

Use Database if:
1. there is only a very large amount of files to save.
2. Meta data is required for indexing and search oprations.
3. The files have to be updated regulary.

#### In our case options 1 & 2 apply. Option 3 only for metadata.
1. We want to scrap a many arcticles over a long period of time.
2. "" search for data based on different criteria (e.g. Publication , Category (Sport, Politics, Science), ...) 
3. "" Meta data has to be updated if new categories of articles are uploaded.

We want our data to be stored in JSON format:\
e.g.

```json
{
    "id":1,
    "heading":"Florida man seduced crocodile",
    "content": ["Text body1", "Text body2"]
    "date":"01.01.2200",
    "category":"Reality Check"
}
```

## log:

## 23.01.2022

Determined some technologies of interest. Some of them should be applied in this project.
- Spark, Dask, Pandas, TensorFlow 
- **Python**, Java oder Scala
- NLP, Feature Engineering, Text Mining, Computer Vision, Artificial Intelligence, Deep Learning oder Modellbildung (oder)
- Spark, Kafka, Hadoop, PostgreSQL, HBase, Cassandra, Elasticsearch, Azure, AWS oder GCP
- Linux Shell, SSH, Git

## 24.01.2022

- Added first Usage of hub-api, and how to update already loaded files. (Because HUB always gets new content/old content is deleted, order of videos changes)

## 27.01.2022

- Visual studio code problems when trying to access the virtual enviroment inside WSL. VS itself is connected to it and executes projects inside it. But after activating the venv, python and pip are still referencing the base interpreter instead of the venv.
