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
- {{ }} and {% %} are very useful

## Deploying to Heroku
- reason we use Heroku is because although we can push to gitHub, we can't deploy our site to github pages because it doesn't work with python
- npm install -g heroku : installs heroku (-g is needed in order to install heroku system wide)
- heroku login -i : login in to heroku in terminal
- heroku apps : shows list of all created apps on heroku
    - to rename app: heroku apps:rename old-name --app new-name
### Pushing directly to heroku from CLI
- to push to Heroku we need to:
    - create new app on heroku
    - connect GIT remote to Heroku
    - create requirements.txt with all dependancies
    - create a Heroku proCfile
#### Connect git remote to Heroku
- go to heroku apps settings and copy "Heroku GIT url"
- git remote add heroku(this is just a name?) and paste copied link
- git remote -v : you can see remote repos (heroku and github)
- before pushing the project we need to create requirements.txt otherwise push will fail
- git remote rm heroku will remove heroku git if we need to remove it
#### Creating requirements.txt
- pip3 freeze --local > requirements.txt : will create txt file with all dependancies listed inside
#### Pushing to Heroku
- git push -u heroku master (just first push?) 
- git push origin master is used to push to github
#### Creating proCfile
- procfile tells heroku how to run our project
- echo web: python run.py > Procfile
    - echo creates a file
- it basically says it's gonna be web project and the command to run it is python run.py
- git add / commit / push (you can use just push without -u heroku master...)

## Heroku
- heroku logs --tail --app app-name :shows app logs, this is where our errors will shows
- it's also available in heroku site under more-view logs
    - e.g error because secret key in form submit is gitignored and heroku doesn't have it
- to add any hidden environ variables go to heroku settings - reveal config variables
    - for our current app vars we need to add are (IP,PORT and ref env.py for third one)
