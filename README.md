# Swansea Uni Expertise Directory 

This project is a website which collates the Areas of Expertise that live on individual staff profiles into one page and allowing them to be filtered with a free text box. 

It is made up of a web scraping python script which is run daily by a GitHub Action, this generates a JSON file. The updated file is picked up by Netlify which hosts the website.  

The front end is a basic HTML site with a bit of JS to pull the data out of the JSON into a HTML table. 

## Limitations 

There are quite a few limitations to this work. As it is a web scraper it is dependent on the Swansea University website for its information. 

If the website structure changes it will stop working.  

At the moment it only works for the School of Law, this was the initial priority, and the other schools display their staff profiles in a different way. 
