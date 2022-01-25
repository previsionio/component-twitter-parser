# Twitter listener 

A component that get tweet from a list of twitter username

## Pre-req

You need a twitter dev account ( or ask for a token )

## Setup

local dev :

```
python3.8 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

(*Warning : use python 3.8 because this component use dataclasses*)


Launch your script to test

```
python src/main.py  --src politics_account.csv --dst output.csv --token <YOUR_TWITTER_TOKEN>
```

if everything is ok you should have an `output.csv` file with a `speech` column. You can now proceed on installing your component   