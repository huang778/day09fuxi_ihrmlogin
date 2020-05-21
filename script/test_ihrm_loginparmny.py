import unittest
import requests
import logging
from parameterized import parameterized

import app
from api.test_login_api import  LoginApi
from unilt import duanyan, read_login_data


# 创建测试类
class Login(unittest.TestCase):
    #初始化
      def setUp(self):
         self.testapi= LoginApi()
      def tearDown(self):
          ...
    # 编写一个测试用例
      filename=app.BASE_DIR + "/data/login_data.json"
      @parameterized.expand(read_login_data(filename))
      def test01_login(aa,case_name,jsonData,http_code,success,code,message):
          headers = {"Content-Type": "application/json"} # 请求头
          jsonData = jsonData
          repons=aa.testapi.loginapi(jsonData ,headers)
          # # 返回登录结果
          # kk=repons.json()
          # # 打印返回登录结果
          # print("登录为：",kk)
          logging.info("登录为:{}".format(repons.json()))
          duanyan(http_code,success,code,message, repons, aa)