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
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Advertising/Advertising.list",
        "https://raw.githubusercontent.com/NobyDa/Script/master/Surge/AdRule.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/AdGuardSDNSFilter/AdGuardSDNSFilter.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Hijacking/Hijacking.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Privacy/Privacy.list",
        "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyGFWlist.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Global/Global.list",
        "https://raw.githubusercontent.com/VirgilClyne/GetSomeFries/main/ruleset/ASN.China.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/China/China.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/WeChat/WeChat.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/OpenAI/OpenAI.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Apple/Apple.list"
    ],
    "rewrite_remote": [
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/script/zheye/zheye.snippet",
        "https://raw.githubusercontent.com/ddgksf2013/Rewrite/master/AdBlock/Applet.conf",
        "https://raw.githubusercontent.com/ddgksf2013/Rewrite/master/AdBlock/YoutubeAds.conf",
        "https://raw.githubusercontent.com/fmz200/wool_scripts/main/QuantumultX/rewrite/chongxie.txt",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rewrite/QuantumultX/Advertising/Advertising.conf",
        "https://raw.githubusercontent.com/ddgksf2013/Rewrite/master/AdBlock/XiaoHongShu.conf",
        "https://raw.githubusercontent.com/zZPiglet/Task/master/UnblockURLinWeChat.conf",
        "https://raw.githubusercontent.com/chavyleung/scripts/master/box/rewrite/boxjs.rewrite.quanx.conf",
        "https://raw.githubusercontent.com/89996462/Quantumult-X/main/ycdz/cubox.js",
        "https://raw.githubusercontent.com/lieying8/sync/main/lw2.js",
        "https://raw.githubusercontent.com/lieying8/sync/main/lw.js",
        "https://raw.githubusercontent.com/89996462/Quantumult-X/main/ycdz/smqnw.js",
        "https://raw.githubusercontent.com/89996462/Quantumult-X/main/ycdz/Notability.js",
        "https://raw.githubusercontent.com/89996462/Quantumult-X/main/ycdz/bdwk.js",
        "https://raw.githubusercontent.com/89996462/Quantumult-X/main/ycdz/mtxx.js",
        "https://raw.githubusercontent.com/89996462/Quantumult-X/main/ycdz/zmzjz.js",
        "https://raw.githubusercontent.com/89996462/Quantumult-X/main/ycdz/gear.js",
        "https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/config/QX.snippet"
    ],
    "task_local": [
        "https://raw.githubusercontent.com/KOP-XIAO/QuantumultX/master/Scripts/streaming-ui-check.js",
        "https://raw.githubusercontent.com/evilbutcher/Quantumult_X/master/check_in/ssq/ssq.js",
        "https://raw.githubusercontent.com/chavyleung/scripts/master/feng/feng.js",
        "https://github.com/sub-store-org/Sub-Store/releases/latest/download/cron-sync-artifacts.min.js"
    ],
    "misc": [
        "https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country.mmdb",
        "https://github.com/Hackl0us/GeoIP2-CN/raw/release/Country.mmdb"
    ]
}

print("Tencent COS Configuration:")
print(f"Secret ID: {secret_id}")
print(f"Region: {region}")
print(f"Bucket: {bucket}")

for folder, links in file_links.items():
    os.makedirs(folder, exist_ok=True)
    for link in links:
        try:
            # 使用部分链接路径作为文件名
            file_name = link.replace("https://", "https_").replace("/", "_")
            file_path = os.path.join(folder, file_name)
            print(f"Downloading {link} to {file_path}")
            response = requests.get(link)
            if response.status_code == 200:
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded {file_path} successfully")
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
