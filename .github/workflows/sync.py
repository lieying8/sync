# your_script.py
import requests

response = requests.get('https://raw.fastgit.org/freefq/free/master/v2')
html_content = response.text

with open('index.html', 'w') as f:
    f.write(html_content)

