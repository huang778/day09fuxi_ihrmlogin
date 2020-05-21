import unittest
import requests
import logging
#创建测试类
from parameterized import parameterized

import app
from api.test_emp_api import EmpApi
from api.test_login_api import LoginApi
from unilt import read_emp_data, duanyan


class PASS(unittest.TestCase):
    #初始化
    def setUp(self):
        self.login=LoginApi() # 登录初始化
        # self.emp_url="http://ihrm-test.itheima.net" + "/api/sys/user"
        self.empapi=EmpApi() #员工接口初始化
    def tearDown(self):
        ...
    def test01_login(self):
        # headers = {"Content-Type": "application/json"}  # 请求头
        # jsonData = {"mobile": "13800000002", "password": "123456"} # 登录数据
        # reposn=self.kk.loginapi({"mobile": "13800000002", "password": "123456"},
        #                            {"Content-Type": "application/json"}) # 发送请求
        reposn = self.login.loginapi({"mobile": "13800000002", "password": "123456"},
                                        {"content-Type": "application/json"})
        # 打印数据
        logging.info("结果为:{}".format(reposn.json()))
        # 获取token令牌
        token= reposn.json().get("data")
        # 保存令牌到请求头中
        headers={"content-Type":"application/json","Authorization":"Bearer " + token}
        # 打印令牌
        # print("令牌为：",headers)
        app.EGM = headers
        logging.info("令牌为:{}".format(headers))
    filename = app.BASE_DIR + "/data/emp_data.json"
    @parameterized.expand(read_emp_data(filename,'add_emp'))
    def test02_emp(self,username,mobile,http_code, success,code, message):
        # 添加员工
        reposn = self.empapi.add_emp(username, mobile,app.EGM)
        # 打印添加员工
        logging.info("添加员工为:{}".format(reposn.json()))
        # 获取员工id
        emp_id = reposn.json().get("data").get("id")
        app.EMP=emp_id
        # 断言添加员工的结果
        duanyan(http_code, success, code, message,  reposn, self)
    @parameterized.expand(read_emp_data(filename,'que_emp'))
    def test03_que(self,http_code, success, code, message):
        # 查询员工
        reposn = self.empapi.que_emp(app.EMP, app.EGM)
        # 打印查询员工
        logging.info("查询员工为:{}".format(reposn.json()))
        # 断言查询员工的结果
        duanyan(http_code, success, code, message, reposn, self)
    @parameterized.expand(read_emp_data(filename,'up_emp'))
    def test04_up(self,username,http_code, success, code, message):
        # 修改员工
        reposn = self.empapi.up_emp(app.EMP, username,app.EGM)
        # # 打印修改数据
        logging.info("修改数据为:{}".format(reposn.json()))
        # 断言修改员工的结果
        duanyan(http_code, success, code, message,  reposn, self)
    @parameterized.expand(read_emp_data(filename,'delete_emp'))
    def test05_dele(self,http_code,success,code,message):
        # 删除员工
        reposn = self.empapi.delete_emp(app.EMP,
                                        app.EGM)
        # # 打印删除数据
        logging.info("删除数据为:{}".format(reposn.json()))
        # 断言删除员工的结果
        duanyan(http_code, success, code, message,  reposn, self)
