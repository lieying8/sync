/*******************************
 * 小猿 AI VIP 永久解锁
 * 适用于 Quantumult X
 * 作者: Shang
 *******************************


*****************************

[rewrite_local]

^https:\/\/leo-online\.fbcontent\.cn\/api\/user\/info url script-response-body https://raw.githubusercontent.com/lieying8/sync/main/xiaoyuan.js

[mitm]

hostname = leo-online.fbcontent.cn

***************************/

const target_host = "leo-online.fbcontent.cn"; // 目标域名
const mock_vip_end_time = 1909660799999; // 2030-01-01 23:59:59

$done({
    response: {
        status: 200, // 模拟成功响应
        headers: {
            "Content-Type": "application/json",
            "X-Test-Env": "Sandbox" // 声明测试环境标识
        },
        body: JSON.stringify({
            // ===== 核心测试字段 =====
            vipSymbol: true,
            grade: 3,
            vipHistory: true,
            userVIPInfo: {
                endTime: mock_vip_end_time, // 修改VIP过期时间
                createTime: 1741862056812, // 保持原始注册时间不变
                monthly: false
            },
            
            // ===== 异常场景模拟 =====
            studyGroupRightInfo: {
                rightStatus: 2, // 测试异常状态(0-正常 1-过期 2-未加入)
                rightEndTime: 0
            },
            
            // ===== 测试数据隔离 =====
            name: "[TEST]猿宝92521", // 添加测试标识前缀
            avatarUrl: "https://test.cdn/mock_avatar.png",
            userMathAnimationEndTime: 0
        }, null, 2)
    }
});