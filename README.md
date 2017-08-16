# anchorloans
Test solution

How to install?
===============
Just clone this repository and install flask, I recomend [virtualenv]('http://docs.python-guide.org/en/latest/dev/virtualenvs/')

How to run?
===========
As is said on [Flask doc page](http://flask.pocoo.org/docs/0.12/quickstart/):
Go to repository root directory and follow this steps:

To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

$ export FLASK_APP=app.py
$ flask run
 * Running on http://127.0.0.1:5000/
If you are on Windows you need to use set instead of export.

Alternatively you can use python -m flask:

$ export FLASK_APP=app.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/


