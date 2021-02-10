# BASH commands
- ls lists files in directory
- cd "space minus" goes back one folder up in dir tree
- pip3 install "package_name" to install packages
- pip3 freeze shows all installed dependancies
- pip3 freeze --local > requirements.txt puts all dependancies in that filename
    - so later on someone else can easily install all dependancies by: 
        - pip3 install -r requirements.txt 



## Styling the pages
- base.html is used so we don't repeat too much code. 
    All html shared between all pages can be in base.html, which
    is basically like a template for templates
    - we use block content / endblock (e.g. base.html) to create an area 
    where we can inject page specific content

- static folder is used for all things that don't change like js, images, css - we called it assets until now

## Using Bootstrap Theme
- to download bootstrap theme:
    - copy the link for the theme
    - create "static" folder and navigate to it in BASH
    - use wget "link" - this will download the theme in zip format to our static folder
    - to unzip use: unzip "filename"
    - move folder one level up (directly in static folder), and delete the main folder containing all other files
- add css link to base.html (using jinja method (same as links in nav))
- go to theme page and view source code on github
    - copy all important code like link to bootstrap (in vendor folder)
    - you can copy body as well 
        - make sure to change all the script and link links to jinja format:
            - {{ url_for('static', filename= 'filepath+name')}}
            - "{{ url_for ('index') }}" - where index is the name of the function in run.py
            - all our internal links need to be formatted in above way
                - pages like e.g.1 & files like e.g.2


