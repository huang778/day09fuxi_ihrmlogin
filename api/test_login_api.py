# 导包
import requests
class LoginApi:
         def __init__(self):
            self.login_url="http://ihrm-test.itheima.net"+"/api/sys/login"
         def loginapi(self,jsonData,headers):
            repons = requests.post(url=self.login_url,
                                   json=jsonData,  # 发送登录请求
                                   headers=headers)
            return repons
