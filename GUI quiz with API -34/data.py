import requests

parameters={
    "amount":10,
    "type": "boolean"
}

data=requests.get("https://opentdb.com/api.php?amount=10&type=boolean",params=parameters)
#print(data.raise_for_status())
data=data.json()
question_data=data["results"]