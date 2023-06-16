# your_script.py
import requests

response = requests.get('http://file.966a.cn/')
html_content = response.text

with open('.github/workflows/vvv.txt', 'w') as f:
    f.write(html_content)

