#!/usr/bin/python3

'''Use the urllib to fetch https://intranet.hbtn.io/status'''


if __name__ == '__main__':
    import requests

    req = requests.get('https://intranet.hbtn.io/status')
    out = 'Body response:\n\t- type: {}\n\t- content: {}'

    print(out.format(type(req.text), req.text))
