import requests

class EmpApi:
    def __init__(self):
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"
        # 封装添加员工
    def add_emp(self,username,mobile,headers,):
        reposn = requests.post(self.emp_url,
                               json={
                                   "username": username,
                                   "mobile": mobile,
                                   "timeOfEntry": "2020-05-05",
                                   "formOfEmployment": 1,
                                   "workNumber": "1234123",
                                   "departmentName": "测试部",
                                   "departmentId": "1063678149528784896",
                                   "correctionTime": "2020-05-17T16:00:00.000Z"
                               }, headers=headers)
        return reposn
    # 封装查询员工
    def que_emp(self,emp_id,headers):
        reposn = requests.get(self.emp_url + "/" + emp_id,
                              headers=headers)
        return reposn
    # 封装修改员工
    def up_emp(self,emp_id,username,headers):
        reposn = requests.put(self.emp_url + "/" + emp_id,
                              json={"username": username},
                              headers=headers)
        return reposn
    def delete_emp(self,emp_id,headers):
        reposn = requests.delete(self.emp_url + "/" + emp_id,
                                 headers=headers)
        return reposn
