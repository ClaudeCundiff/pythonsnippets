import sys
import requests

def main():
    url = 'https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python'

    r = requests.get(url)

    # header_keys = r.headers.keys()

    status_code = r.status_code
    response_body = r.text

if __name__ == '__main__':
    main()
