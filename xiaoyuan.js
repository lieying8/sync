/*******************************
 * 小猿 AI VIP 永久解锁
 * 适用于 Quantumult X
 * 作者: Shang
 *******************************/

[rewrite_local]

^https:\/\/xyks\.yuanfudao\.com\/leo-alchemy-account\/api\/vip\/user\/info\/v2 url script-response-body https://raw.githubusercontent.com/lieying8/sync/main/xiaoyuan.js

[mitm]

hostname = xyks.yuanfudao.com

*******************************/

// Quantumult X 脚本
var body = $response.body;
var obj = JSON.parse(body);

// 设置 VIP 标识为 true
obj.vipSymbol = true;

// 修改 VIP 过期时间（2099-12-31）
if (obj.userVIPInfo) {
    obj.userVIPInfo.endTime = 4102444799000; // 2099-12-31
}

// 修改 VIP 课程权限
if (obj.studyGroupRightInfo) {
    obj.studyGroupRightInfo.rightStatus = 1;
    obj.studyGroupRightInfo.rightEndTime = 4102444799000; // 2099-12-31
}

// 解锁 VIP 动画课
if (obj.userMathAnimationEndTime !== undefined) {
    obj.userMathAnimationEndTime = 4102444799000; // 2099-12-31
}

// 处理可能缺失的字段，避免 App 崩溃
if (!obj.userVIPInfo) {
    obj.userVIPInfo = {
        "endTime": 4102444799000,  // 确保 VIP 过期时间
        "createTime": 1741862056812, // 创建时间保持不变
        "monthly": false
    };
}

$done({body: JSON.stringify(obj)});
