from flask import Flask, request, jsonify
import json, os

json_file = 'db.json'

if not os.path.exists(json_file):
    with open(json_file, 'w') as file:
        json.dump([], file)
        file.close()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handledata():
    if request.method == 'GET':
        with open(json_file, 'r') as file:
            output_data = json.load(file)
        return jsonify(output_data)
    if request.method == 'POST':
        request_data = request.json
        with open(json_file, 'r') as file:
            data = json.load(file)
        with open(json_file, 'w') as file:
            data.append(eval(request_data))
            json.dump(data, file)
        print(f"Successful data input: {request_data}")
        return f"Successful data input: {request_data}"
    

if __name__ == "__main__":
    app.run(port=3000)