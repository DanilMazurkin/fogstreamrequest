import requests
import json

url_get = 'http://httpbin.org/'
url_post = 'http://httpbin.org/post'
url_json = 'https://httpbin.org/json'
url_image = 'https://httpbin.org/image/jpeg'

HEADER_GET = {
    'Host': 'httpbin.org',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0)' 
                  'Gecko/20100101 Firefox/84.0',
    'Accept': 'text/html,application/xhtml+xml,application/'
              'xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

HEADER_POST = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Content-Length": "0",
    "Host": "httpbin.org",
    "Origin": "moz-extension://e01df379-8eab-4dba-bdf0-0403b3376a20",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "X-Amzn-Trace-Id": "Root=1-6011204f-64465e20539b0bc55227be6a"
}

HEADER_JSON = {
    'Host': 'httpbin.org',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0)' 
                  'Gecko/20100101 Firefox/84.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;'
               'q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers'
}

HEADER_IMAGE = {
    'Host': 'httpbin.org',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0)' 
                  'Gecko/20100101 Firefox/84.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;'
              'q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers'
}

response_get = requests.get(url_get, headers=HEADER_GET)
response_post = requests.post(url_post, headers=HEADER_POST)
response_json = requests.get(url_json, headers=HEADER_JSON)
response_image = requests.get(url_image, headers=HEADER_IMAGE)


page_content = response_get.text
post_content = response_post.json()

with open("sample_image.png", "wb") as file_image:
    file_image.write(response_image.content)

with open('file.json', "w") as file_json:
    json.dump(response_json.json(), file_json, indent=5)
