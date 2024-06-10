# https://github.com/freefq/free  
# https://raw.fastgit.org/freefq/free/master/v2
import requests

response = requests.get('https://raw.githubusercontent.com/chengaopan/AutoMergePublicNodes/master/list.txt')
html_content = response.text

with open('.github/workflows/vvv.txt', 'w') as f:
    f.write(html_content)

