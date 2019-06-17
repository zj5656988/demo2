"""
http://uat.crm.yxqiche.com/ydg-web/api/order/recheckOrderList
"""

import requests
import json
def fun():
    url_check="http://uat.crm.yxqiche.com/ydg-web/api/order/recheckOrderList"
    header_check={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Content-Type':'application/json; charset=utf-8',
        'Cookie':"sid=6b6b3a21-f555-4234-9ba8-7b0ca76b2e57; authorization=f767b96709944f7985ca5243227d021b; Hm_lvt_e39e5970b28d9025d0f918c738c63553=1560429796,1560429810,1560498568,1560498575; Hm_lpvt_e39e5970b28d9025d0f918c738c63553=1560498575"
    }
    param_check={
    "pageSize":10,
    "pageIndex":1,
    "beginCreateTime":"2019-06-08 00:00:00",
    "endCreateTime":"2019-06-14 23:59:00",
    "isByPhone":0
    }
    res=requests.post(url=url_check,headers=json.dumps(header_check),params=param_check)

    return res
if __name__ == '__main__':
    f=fun()
    print(f.text)


