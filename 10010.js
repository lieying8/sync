# 打开 APP , 进入签到页面, 系统提示: 获取刷新链接: 成功,然后手动签到 1 次, 系统提示: 获取Cookie: 成功 (每日签到)
# 首页>天天抽奖, 系统提示 2 次: 获取Cookie: 成功 (登录抽奖) 和 获取Cookie: 成功 (抽奖次数)
# 把获取 Cookie 的脚本注释掉
# 运行一次脚本, 如果提示重复签到, 那就算成功了!

[rewrite_local]
# 注意获取Cookie有两条脚本
^https?:\/\/act.10010.com\/SigninApp\/signin\/querySigninActivity.htm url script-request-header https://raw.githubusercontent.com/chavyleung/scripts/master/10010/10010.cookie.js
^https?:\/\/act.10010.com\/SigninApp(.*?)\/signin\/daySign url script-request-header https://raw.githubusercontent.com/chavyleung/scripts/master/10010/10010.cookie.js
^https?:\/\/m.client.10010.com\/dailylottery\/static\/(textdl\/userLogin|active\/findActivityInfo) url script-request-header https://raw.githubusercontent.com/chavyleung/scripts/master/10010/10010.cookie.js

[mitm]

hostname = act.10010.com, m.client.10010.com

