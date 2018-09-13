# coding=utf-8
# 添加引用
import requests
import json
# 尝试导入先前账号密码
try:
    ins = open('data.json', 'r')
    payload2 = json.load(ins)
except Exception as err:
    # 否则输入宽带账号密码
    name = input(u"输入账号")
    password = input(u"输入密码")
    # 设置更改宽带设置所需字典
    payload2 = {
        "cbid.network.wan.username": name,
        "cbid.network.wan.password": password,
        "cbid.network.wan.randommac": "1",
        "cbid.network.wan.autoredial": "1",
        "cbid.network.wan.dialtype": "3",
        "cbid.network.wan.proto": "pppoe",
        "cbid.network.wan.macaddr": "",
        "step": "4",
        "quit": "0",
    }

# 新建一个requests
session_requests = requests.session()
# 指定访问url
login_url = 'http://192.168.1.1/cgi-bin/luci'
# 设置登录所需字典
payload = {"luci_username": "root", "luci_password": "admin"}
# POST操作登录
result = session_requests.post(login_url, data=payload)
# 生成新的跳转url
new_url = result.url + "/admin/guide"
# POST操作修改宽带设置
result2 = session_requests.post(new_url, data=payload2)

# 打印结果提示页面
print(result2.content)
# 存储账号密码
output = open('data.json', 'w')
json.dump(payload2, output)
output.close()
