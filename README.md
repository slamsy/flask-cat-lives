# Usage on FreeBSD

* Install Flask: http://flask.pocoo.org/docs/1.0/installation/
* Script to run that serves the game on any IP address, port 5000:
```sh
. venv/bin/activate
export LC_ALL=en_CA.UTF-8 # probably only needed on BSD
export LANG=en_CA.UTF-8 # probably only needed on BSD
export FLASK_APP=catlives.py
export FLASK_ENV=development
flask run --host=0.0.0.0 # probably only needed if serving from remote machine
```
*  for easy use add the script to a file, for example setup.sh inside the repo, then run ```./setup.sh```
