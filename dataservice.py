import time

def main():
    while True:
        with open('input.txt', 'r') as file:
            data = file.read()
            if data == "":
                file.close()
                time.sleep(1)
                continue
            file.close()
        with open('input.txt', 'w') as file:
            file.write('')
            file.close()
        with open('db.txt', 'a') as file:
            file.write(data)
            file.write("\n")
            file.close()

if __name__ == "__main__":
    main()