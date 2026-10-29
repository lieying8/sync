
/******************************

脚本名称：PiP Translate
脚本功能：RevenueCat 会员接口测试
脚本版本：v0.1
适用工具：Quantumult X
测试目标：验证会员响应是否可以被重写

******************************

[rewrite_local]

^https:\/\/api\.revenuecat\.com\/v1\/subscribers\/ url script-response-body https://raw.githubusercontent.com/lieying8/sync/main/ceshi.js

[mitm]

hostname = api.revenuecat.com

******************************/


// PiP Translate v0.1
// JavaScript 响应测试代码

var body = $response.body;

try {
    var objc = JSON.parse(body);

    console.log("PiP Translate 接口命中");

    if (objc.subscriber) {
        console.log("会员字段读取成功");

        var entitlements =
            objc.subscriber.entitlements || {};

        console.log(
            "权益名称：" +
            Object.keys(entitlements).join(", ")
        );

        $notify(
            "PiP Translate v0.1",
            "会员接口测试成功",
            "已成功读取 RevenueCat 响应"
        );
    }

    $done({body: JSON.stringify(objc)});

} catch (e) {
    console.log("接口响应无法解析：" + e);
    $done({body: body});
}
