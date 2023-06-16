# your_script.py
import requests

response = requests.get('https://raw.githubusercontent.com/freefq/free/master/v2')
html_content = response.text

with open('.github/workflows/vv.txt', 'w') as f:
    f.write(html_content)

