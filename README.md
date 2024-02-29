# Data Request:
The data service checks every 1 second for new data in input.txt and clears it when processed.<br>
To send data to the service, write the data to input.txt

Python example
```
with open('input.txt', 'w') as file:
  data = "Hello World!"
  file.write(data)
  file.close()
```

# Receiving Data:
The output data is appended to db.txt which can be read to retrieve the input data.

Python example
```
with open('db.txt', 'r') as file:
  data = file.read()

  # process data here ...

  file.close()
```

#UML Diagram
![image](https://github.com/Hayden-Johnston/data-manager/assets/103093070/4bec1598-4a48-48eb-b7e6-45ccd5ecd7cb)
