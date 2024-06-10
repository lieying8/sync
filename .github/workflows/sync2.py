# sync2.py
import requests

# 请求A网站的内容
response = requests.get('https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2')
html_content = response.text

# 创建一个保存到B网站的链接，使用WebDAV
webdav_url = 'http://2.9qaz.com/vvv.txt'

# 通过PUT请求将新内容保存到B网站
response = requests.put(webdav_url, data=html_content)

# 检查请求是否成功
if response.status_code == 200:
    print('File successfully updated.')
else:
    print('Error updating file:', response.status_code)
2
