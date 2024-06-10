import os
import requests
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

# 获取环境变量
secret_id = os.getenv('TENCENT_SECRET_ID')
secret_key = os.getenv('TENCENT_SECRET_KEY')
region = os.getenv('TENCENT_REGION')
bucket = os.getenv('TENCENT_BUCKET')

# 配置腾讯云 COS 客户端
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)

# 定义文件链接和对应的文件夹
file_links = {
    "general": [
        "https://cdn.jsdelivr.net/gh/KOP-XIAO/QuantumultX@master/Scripts/resource-parser.js",
        "https://raw.githubusercontent.com/Orz-3/Orz-3/master/QuantumultX/IP.js"
    ],
    "filter_remote": [
        "https://raw.githubusercontent.com/Cats-Team/AdRules/main/qx.conf",
        "https://raw.githubusercontent.com/RuCu6/QuanX/main/Rules/MyBlockAds.list",
        # 省略其他链接...
    ],
    "rewrite_remote": [
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/script/zheye/zheye.snippet",
        # 省略其他链接...
    ],
    "task_local": [
        "https://raw.githubusercontent.com/KOP-XIAO/QuantumultX/master/Scripts/streaming-ui-check.js",
        # 省略其他链接...
    ],
    "misc": [
        "https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country.mmdb",
        "https://github.com/Hackl0us/GeoIP2-CN/raw/release/Country.mmdb",
        "https://static.itsnebula.net/apple/noota/17.mobileconfig"
    ]
}

for folder, links in file_links.items():
    # 创建文件夹，如果不存在
    os.makedirs(folder, exist_ok=True)
    for link in links:
        try:
            file_name = link.split('/')[-1]
            response = requests.get(link)
            if response.status_code == 200:
                file_path = os.path.join(folder, file_name)
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded {file_path} successfully")
                # 上传文件到腾讯云 COS
                response = client.upload_file(
                    Bucket=bucket,
                    LocalFilePath=file_path,
                    Key=f"{folder}/{file_name}"
                )
                print(f"Uploaded {file_path} to COS bucket with response: {response}")
            else:
                print(f"Failed to download {link}, status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading {link}: {e}")
