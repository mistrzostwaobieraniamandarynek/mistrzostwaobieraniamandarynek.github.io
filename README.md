# The Official MOM website

This website was created and is currently maintained by Jakub Ćwikowski aka. [Jerry-BloodBerry](https://github.com/Jerry-BloodBerry).
It is a set of static webpages made for MOM to advertise the MOM event.

## Facebook scraper

The project also contains a web scraping tool for updating the news feed on the main page. Inserting a post was automated using python language alongside with
some of its modules sych as: bs4, requests, json. The script is making use of Facebook's GRAPH API to fetch data. In order to use the script you need to create a
.env file containing two values: ```ACCESS_TOKEN``` and ```PAGE_ID```. The first one is the access_token you get in graph explorer, the second one is the id
of the facebook page that you want to scrape.
