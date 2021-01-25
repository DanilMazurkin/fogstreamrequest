import requests

url_get = 'http://httpbin.org/'
url_post = 'http://httpbin.org/post'
url_json = 'https://httpbin.org/json'
url_image = 'https://httpbin.org/image/jpeg'

response_get = requests.get(url_get)
response_post = requests.post(url_post)
response_json = requests.get(url_json)
response_image = requests.get(url_image)


page_content = response_get.text
post_content = response_post.json()


file_image = open("sample_image.png", "wb")
file_image.write(response_image.content)
file_image.close()

file_json = open('file.json', "wb")
file_json.write(response_json.content)
file_json.close()