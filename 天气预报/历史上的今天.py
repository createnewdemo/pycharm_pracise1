import requests
import json


def history():
    url = 'http://api.63code.com/history/api.php?format=json'
    while True:
        try:
            r = requests.get(url)
            contents = r.json()['content']
            # print(contents)
            contents = "\n".join(str(i) for i in contents)
            return contents
            break
        except:
            continue


def a():
    b = history()
    # print(b)
    I = "\n".join(str(i) for i in b)
    print(I)


a()
# while True:
#     try:
#         x=int(input("Please enter a number:"))
#         break
#     except ValueError:
#         print("Oops,that was no valid number. Try again ...")
