# Legal Innovation Lab Wales - Swansea University Expertise Directory 

This project is a web application that collates the "Areas of Expertise" that live on individual staff member profiles 
into a single page and allows them to be filtered with a free text box and department dropdown.

It is made up of a collection of web scraping python scripts which are run daily by a GitHub Action, this generates a 
JSON file. The updated file is picked up by Netlify which hosts the website.

The front end is a React web application that pulls the data out of the JSON into an HTML table.

## Limitations 

There are quite a few limitations to this work. As it is a web scraper it is dependent on the Swansea University 
website for its information, if the website structure changes it will stop working.  

At the moment it only covers the Hillary Rodham Clinton School of Law, the College of Science and the College of Arts
and Humanities, the other colleges display their staff profiles in a different structure and so will need to be added 
in time. 

---
### Build

To build this project you will need to have [Node.js](https://nodejs.org/en/) and npm installed (should come bundled 
with node). You will also  need to have [Python 3](https://www.python.org/download/releases/3.0/) installed to run 
the data scraping scripts along with a number of libraries that can be installed with pip (should come bundled with 
python).

```pip install flake8 pytest requests beautifulsoup4 datetime tqdm```

You can then run the data scraping scripts from the ```scripts``` folder using ```python scrape_data.py```.

Once the script has run a new JSON file called ```new-expertise.json``` will be generated in the projects root folder,
to use this file in your  local deployment you will need to move it to the ```public``` folder and rename it 
```expertise.json```. You can do this from the ```scripts``` folder using 
```mv ../new-expertise.json ../public/expertise.json```

With the JSON file generated you can generate the web application using ```npm install```, once all the requisite
dependencies are installed you can start the application using ```npm start```. This will launch the application at
```http://localhost:3000```.