/* 录丸 解锁会员 A+ 
[rewrite_local]
^https:\/\/irecgo\.softin-tech\.com\/user\/info url script-response-body https://raw.githubusercontent.com/lieying8/sync/main/lw2.js
[mitm]
hostname = irecgo.softin-tech.com
*/

body = $response.body.replace(/expires_date_ms":\d+/g, 'expires_date_ms":1800000000111');
$done({body});
