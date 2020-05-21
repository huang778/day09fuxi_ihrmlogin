# 导包
import unittest
import requests
import logging
#创建测试类
from api.test_emp_api import EmpApi
from api.test_login_api import LoginApi
class EmpYess(unittest.TestCase):
    #初始化
    def setUp(self):
        self.login=LoginApi() # 登录初始化
        # self.emp_url="http://ihrm-test.itheima.net" + "/api/sys/user"
        self.empapi=EmpApi() #员工接口初始化
    def tearDown(self):
        ...
    def test01_empyess(self):
        # headers = {"Content-Type": "application/json"}  # 请求头
        # jsonData = {"mobile": "13800000002", "password": "123456"} # 登录数据
        # reposn=self.kk.loginapi({"mobile": "13800000002", "password": "123456"},
        #                            {"Content-Type": "application/json"}) # 发送请求
        reposn = self.login.loginapi({"mobile": "13800000002", "password": "123456"},
                                        {"content-Type": "application/json"})
        # rusit=reposn.json() # 返回数据
        # print("返回结果：",rusit)
        # 打印数据
        logging.info("结果为:{}".format(reposn.json()))
        # 获取token令牌
        token= reposn.json().get("data")
        # 保存令牌到请求头中
        headers={"content-Type":"application/json","Authorization":"Bearer " + token}
        # 打印令牌
        # print("令牌为：",headers)
        logging.info("令牌为:{}".format(headers))
        # 添加员工
        reposn=self.empapi.add_emp("爱黄哥","18378986521",headers)
        # 打印添加员工
        # rusit=reposn.json()
        # print("打印员工为：",rusit)
        logging.info("添加员工为:{}".format(reposn.json()))
        # 获取员工id
        emp_id = reposn.json().get("data").get("id")
        # 查询员工
        reposn=self.empapi.que_emp(emp_id,headers)
        # 打印查询员工
        # rusit=reposn.json()
        # print("查询员工为：",rusit)
        logging.info("查询员工为:{}".format(reposn.json()))
        # 修改员工
        reposn= self.empapi.up_emp(emp_id,"我超爱黄志松",headers)
        # # 获取返回数据
        # rusit=reposn.json()
        # # 打印修改数据
        # print("修改数据为：",rusit)
        logging.info("修改数据为:{}".format(reposn.json()))
        # 删除员工
        reposn=self.empapi.delete_emp(emp_id,headers)
        # # 获取返回数据
        # rusit=reposn.json()
        # # 打印删除数据
        # print("删除数据为：",rusit)
        logging.info("删除数据为:{}".format(reposn.json()))





