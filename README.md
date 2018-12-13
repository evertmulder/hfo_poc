```bash
# create the venv and activate it
python3 -m venv venv
. venv/bin/activate

# Install the requirements and the hfo module into the venv
pip install -e .

# Run the hfo flask app
export FLASK_APP=hf1
export FLASK_ENV=development
flask run
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

When using VS Code, you can debug the app with the follwing ```launch.json```
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "hf1",
                "FLASK_ENV": "development"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true
        }
    ]
}
```