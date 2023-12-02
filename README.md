# my-first-app-inclass-2023




## Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```


Install packages:

```sh
pip install -r requirements.txt
```

Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).

Follow the [setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) to create an account, verify your account, setup a single sender, and obtain an API Key.

Create a ".env" file and paste in the following contents:

```sh

# this goes in your the ".env" file...

ALPHAVANTAGE_API_KEY="_________"

SENDGRID_API_KEY="_________"
SENDER_ADDRESS="example.gmail.com"
```

## Usage

Run the example script:

```sh
python -m app.my_script
```

Run the unemployment report:

```sh
python -m app.unemployment
```

Send an example email:

```sh
python -m app/email_service.py
```


## Testing

Run tests:

```sh
pytest
```

## Running a web app
set FLASK_app = web_app in your .env file

Run on localhost:
```sh
flask run
```