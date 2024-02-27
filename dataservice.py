from flask import Flask
import time

app = Flask(__name__)

def main():
    while True:
        time.sleep(1)
        with open('input.txt', 'r') as file:
            data = file.read()
            if data == "":
                file.close()
                continue
            file.close()
        with open('input.txt', 'w') as file:
            file.write('')
        with open('db.txt', 'a') as file:
            file.write(data)
            file.write("\n")
            file.close()

if __name__ == "__main__":
    app.run()
    main()