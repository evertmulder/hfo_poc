```
# create the venv and activate it
python3 -m venv venv
. venv/bin/activate

# Install the requirements and the hfo module into the venv
pip install -e .

# Run the hfo flask app
export FLASK_APP=hfo
export FLASK_ENV=development
flask run

```


https://github.com/achiku/sample-flask-sqlalchemy