# Data Request:
To store data with the micro service, perform a POST request where the body contains the data to be stored.

Python example
```
import requests, json

url = 'http://localhost:3000/'
score = {'1': 'score 1'}

json_score = json.dumps(score)
response = requests.post(url, json=json_score)
return response
```

# Receiving Data:
The stored data is accessed by a GET request to the url.

Python example
```
import requests, json

url = 'http://localhost:3000/'
out = requests.get(url)
return out
```

# UML Diagram
![image](https://github.com/Hayden-Johnston/data-manager/assets/103093070/33e19c65-9a1b-4d81-8fc7-4562cfec9ac7)

