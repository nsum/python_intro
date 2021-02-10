"""
import flask from Flask - we would use for built-in libs like math
    for external libs we first have to install 
    them by typing below in TERMINAL.
    pip3 install flask
    -------------------
    when we import package it's called dependancy
    -------------------
    pip3 freeze - shows all installed packages
    -------------------
    Common practice is to save a list of all dependancies
    So when someone reuses the code they have a list
    of all the dependancies needed to run the code 
    we save a list by running below in terminal:

    pip3 freeze --local > requirements.txt
    Then it's easy to install all dependancies by going:
    pip3 install -r requirements.txt - and all dependancies
     listed in requirements install
"""