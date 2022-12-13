/* 录屏 - 屏幕录制软件 https://apps.apple.com/cn/app/%E5%BD%95%E5%B1%8F-%E5%B1%8F%E5%B9%95%E5%BD%95%E5%88%B6%E8%BD%AF%E4%BB%B6/id1380506650

附Qx规则
#录丸 解锁会员 A+ 
^https:\/\/irecgo\.softin-tech\.com\/user\/info url script-response-body lw.js

hostname
irecgo.softin-tech.com

*/

body = $response.body.replace(/expires_date_ms":\d+/g, 'expires_date_ms":1800000000111');
$done({body});
