/* 录丸 解锁会员 A+ 软件版本2.6.4
[rewrite_local]
^https:\/\/irecgo\.softin-tech\.com\/user\/info url script-response-body https://raw.githubusercontent.com/lieying8/sync/main/lw.js

[mitm]
hostname = irecgo.softin-tech.com
*/

var body = $response.body;
var url = $request.url;

const path1 = '\/user\/info';

let obj = JSON.parse(body);

if (url.indexOf(path1) != -1) {
	obj.data["expires_date_ms"] = 4099692800000;
	body = JSON.stringify(obj);  
 }
$done({body});


