# HOW TO BUILD WWW.OPENCHANGE.ORG #

## Short Instructions ##

Run the build script, from the same directory as this file:

    python scripts/build.py

This generates the directory `./out`, which is the fully built site.

The included `scripts/micro-httpd.py` script is helpful for testing
the site on your own machine. Running it will start up a tiny HTTP
server that you can hit to test changes in a browser:

    cd ./out
    HTTP_PORT=8080 python ../scripts/micro-httpd.py

### Markdown ###
Markdown is a very simple markup format for plain-text that converts it to
decent HTML. Useful docs:
http://daringfireball.net/projects/markdown/syntax

OpenChange provides embeds its own version of the python markdown
package (2.0.3) which allows embedding markdown code within `div`
tags.

### Contents Included in Box ###

Build system:

    scripts/    tools to generate the site along with helpers scripts

Necessary source files include:

    src/        individual page content in markdown format
    templates/  templates for page content
    api/	sphynx API documentation

and the following content which is copied directly:

    assets/     stylish things that make the page look pretty
    assets/js	javascript code used on the site
    images/     exactly what it sounds like

### Structure of Site Source ###

The build script assumes that
- Every .md file under src/ is an individual page in markdown format.
- Each directory under src/ is a tab of www.openchange.org and contains its
  particular sidebar (see `templates/header` and `src/assets/main.css` file).  
- Please use .md if possible (because this will pick up the global site CSS
  and layout.) But the build.py script will indeed copy arbitrary files to the
  output dir, so it is possible to simply place .html, .pdf, and similar files
  to the src/ tree and they will be copied directly to ./out.
- python-sphinx python-sphinxcontrib-httpdomain packages are installed

## Stylish Guide ##

### News ###

Only the 2 or 3 most recent news MUST appear on src/index.md main
page. Older news must be moved from main page to their archives -
classified by year - within src/about/news_YYYY.md where YYYY is the
year of the news publication.

New archived news must be added to the top of news_YYYY.md file.


News template looks like the following code snipset:


<div class="news" style="width:90%;">
  <h2>News title here</h2>
  <div class="date">Date of news </div>
  <img border="0" width="96" height="96" style="border: 0pt none; margin: -5px 5px
   5px; float: left;" alt="" src="/images/icon_openchange_logo.png" />

Sample text here

</div>


### Code Listing ###

The listing script will take an input file and output a markdown
version with numbered lines. Use this script to produce listing you
push on the website.

