# https://github.com/freefq/free
import requests

response = requests.get('https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub')
html_content = response.text

with open('vv.txt', 'w') as f:
    f.write(html_content)

