```bash
# create the venv and activate it
python3 -m venv venv
. venv/bin/activate

# Install the requirements and the hfo module into the venv
pip install -e .

# Run the hfo flask app (Mac/Linux)
export FLASK_APP=hf1
export FLASK_ENV=development
flask run

# Run the hfo flask app (Windows Powershell)
$env:FLASK_APP = "hf1"
$env:FLASK_ENV = "development"
python -m flask run
```

The database is create in the instance directory. The following command line options are available:
```bash
# create a new database
flask init-db

# Recreate the database and fill with some demo data
flask fill-db
```

The app can be configure using an config.cfg file in the instance directory.
```python
APP_VERSION='0.1poc'
SECRET_KEY='my_secret'
```

## Instruction on how to use VS Code

* Install Visual Studio Code https://code.visualstudio.com/Download
* Install the pyhton extension: Python
* Select the Python venv (bottom left task bar)
* Select the debug icon (left task bar)
* Select the debug settings (right to the green play button)
* Select Python->Flask->hf1 and a the flask config is added

VS Code can now debug your flask web application.
