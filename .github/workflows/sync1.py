# https://github.com/freefq/free  
# https://raw.fastgit.org/freefq/free/master/v2
import requests
# 禁用 SSL 证书验证
requests.packages.urllib3.disable_warnings()

response = requests.get('https://raw.fastgit.org/freefq/free/master/v2', verify=False)
html_content = response.text

with open('.github/workflows/vvv.txt', 'w') as f:
    f.write(html_content)

