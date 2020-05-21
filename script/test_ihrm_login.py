# 导包
import unittest
import requests
import logging
from api.test_login_api import  LoginApi
from unilt import duanyan
# 创建测试类
class Login(unittest.TestCase):
    #初始化
      def setUp(self):
         self.testapi= LoginApi()
      def tearDown(self):
          ...
    # 编写一个测试用例
      def test01_login(self):
          headers = {"Content-Type": "application/json"} # 请求头
          jsonData = {"mobile": "13800000002","password": "123456"}
          repons=self.testapi.loginapi(jsonData ,headers)
          # # 返回登录结果
          # kk=repons.json()
          # # 打印返回登录结果
          # print("登录为：",kk)
          logging.info("登录为:{}".format(repons.json()))
          duanyan(200, True, 10000, "操作成功", repons, self)
      def test02_mobile(self):
          headers = {"Content-Type": "application/json"} # 请求头
          jsonData = {"mobile": "13900000002","password": "123456"}
          repons=self.testapi.loginapi(jsonData ,headers)
          # # 返回登录结果
          # kk=repons.json()
          # # 打印返回登录结果
          # print("登录为：",kk)
          logging.info("登录为:{}".format(repons.json()))
          duanyan(200, False, 20001, "用户名或密码错误", repons, self)
      def test03_error_password(self):
          headers = {"Content-Type": "application/json"} # 请求头
          jsonData = {"mobile": "13800000002","password": "error"}
          repons=self.testapi.loginapi(jsonData ,headers)
          # # 返回登录结果
          # kk=repons.json()
          # # 打印返回登录结果
          # print("登录为：",kk)
          logging.info("登录为:{}".format(repons.json()))
          duanyan(200, False, 20001, "用户名或密码错误", repons, self)
      def test04_null_password(self):
          headers = {"Content-Type": "application/json"} # 请求头
          jsonData = {"mobile": "13800000002","password": ""}
          repons=self.testapi.loginapi(jsonData ,headers)
          # # 返回登录结果
          # kk=repons.json()
          # # 打印返回登录结果
          # print("登录为：",kk)
          logging.info("登录为:{}".format(repons.json()))
          duanyan(200, False, 20001, "用户名或密码错误", repons, self)
      def test05_null_mobile(self):
          headers = {"Content-Type": "application/json"} # 请求头
          jsonData = {"mobile": "","password": "123456"}
          repons=self.testapi.loginapi(jsonData ,headers)
          # # 返回登录结果
          # kk=repons.json()
          # # 打印返回登录结果
          # print("登录为：",kk)
          logging.info("登录为:{}".format(repons.json()))
          duanyan(200, False, 20001, "用户名或密码错误", repons, self)
      def test06_null(self):
          headers = {"Content-Type": "application/json"} # 请求头
          jsonData = {}
          repons=self.testapi.loginapi(jsonData ,headers)
          # # 返回登录结果
          # kk=repons.json()
          # # 打印返回登录结果
          # print("登录为：",kk)
          logging.info("登录为:{}".format(repons.json()))
          duanyan(200, False, 20001, "用户名或密码错误", repons, self)
      def test07_error_mobile(self):
          headers = {"Content-Type": "application/json"} # 请求头
          jsonData = {"mboile": "13800000002","password": "123456"}
          repons=self.testapi.loginapi(jsonData ,headers)
          # # 返回登录结果
          # kk=repons.json()
          # # 打印返回登录结果
          # print("登录为：",kk)
          logging.info("登录为:{}".format(repons.json()))
          duanyan(200, False, 20001, "用户名或密码错误", repons, self)
      def test08_less_mobile(self):
          headers = {"Content-Type": "application/json"} # 请求头
          jsonData = {"password": "123456"}
          repons=self.testapi.loginapi(jsonData ,headers)
          # # 返回登录结果
          # kk=repons.json()
          # # 打印返回登录结果
          # print("登录为：",kk)
          logging.info("登录为:{}".format(repons.json()))
          duanyan(200, False, 20001, "用户名或密码错误", repons, self)
      def test09_less_password(self):
          headers = {"Content-Type": "application/json"} # 请求头
          jsonData = {"mobile": "13800000002"}
          repons=self.testapi.loginapi(jsonData ,headers)
          # # 返回登录结果
          # kk=repons.json()
          # # 打印返回登录结果
          # print("登录为：",kk)
          logging.info("登录为:{}".format(repons.json()))
          duanyan(200, False, 20001, "用户名或密码错误", repons, self)
      def test10_mobile_as(self):
          headers = {"Content-Type": "application/json"} # 请求头
          jsonData = {"mobile": "1380(000002","password": "123456"}
          repons=self.testapi.loginapi(jsonData ,headers)
          # # 返回登录结果
          # kk=repons.json()
          # # 打印返回登录结果
          # print("登录为：",kk)
          logging.info("登录为:{}".format(repons.json()))
          duanyan(200, False, 20001, "用户名或密码错误", repons, self)
      def test11_more_params(self):
          headers = {"Content-Type": "application/json"} # 请求头
          jsonData = {"mobile": "13800000002","password": "123456","more_params":"1"}
          repons=self.testapi.loginapi(jsonData ,headers)
          # # 返回登录结果
          # kk=repons.json()
          # # 打印返回登录结果
          # print("登录为：",kk)
          logging.info("登录为:{}".format(repons.json()))
          duanyan(200, True, 10000, "操作成功", repons, self)
      def test12_None(self):
          headers = {"Content-Type": "application/json"} # 请求头
          jsonData =None
          repons=self.testapi.loginapi(jsonData ,headers)
          # # 返回登录结果
          # kk=repons.json()
          # # 打印返回登录结果
          # print("登录为：",kk)
          logging.info("登录为:{}".format(repons.json()))
          duanyan(200, False, 99999, "抱歉，系统繁忙，请稍后重试！", repons, self)
