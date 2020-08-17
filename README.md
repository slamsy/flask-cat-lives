# 9Lives

Browser word game based on hangman but with cute cats instead. Built on Python in a Flask web framework. 
Current master is stable and playable. 

# Usage on FreeBSD

To run the game locally:

* Install Flask: http://flask.pocoo.org/docs/1.0/installation/
* Script to run that serves the game on any IP address, port 5000:
```sh
. venv/bin/activate # venv\Scripts\activate on Windows
export LC_ALL=en_CA.UTF-8 # probably only needed on BSD
export LANG=en_CA.UTF-8 # probably only needed on BSD
export FLASK_APP=catlives.py #set FLASK_APP=catlives.py on Windows
export FLASK_ENV=development #set FLASK_ENV=development on Windows
flask run --host=0.0.0.0 # probably only needed if serving from remote machine
```
*  for easy use add the script to a file, for example setup.sh inside the repo, then run ```./setup.sh```
