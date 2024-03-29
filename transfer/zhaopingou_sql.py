import requests
import json
import time
import MySQLdb
import hashlib

#最坑的地方在于，城市这个变动的数据值保存在cooike中,就是cookie的zhaopingou_select_city

headers = {'Host':'www.zhaopingou.com','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36','Cookie':'JSESSIONID=885F4342C726E39A1B4AECDEBE442B24; JSESSIONID=2EB867544CC327AE626EC41B92AF3760; Hm_lvt_b025367b7ecea68f5a43655f7540e177=1488520262,1488521555,1488521558,1488522258; Hm_lpvt_b025367b7ecea68f5a43655f7540e177=1488522988; zhaopingou_select_city='}

url_1 = 'http://www.zhaopingou.com/zhaopingou_interface/find_warehouse_by_position_new?timestamp='

url = url_1 + str(int(time.time() * 1000))

cookie = 'JSESSIONID=885F4342C726E39A1B4AECDEBE442B24; JSESSIONID=2EB867544CC327AE626EC41B92AF3760; Hm_lvt_b025367b7ecea68f5a43655f7540e177=1488520262,1488521555,1488521558,1488522258; Hm_lpvt_b025367b7ecea68f5a43655f7540e177=1488522988; zhaopingou_select_city='

payload = {'pageSize':'0','pageNo':'25','keyStrPostion':'iOS','startDegrees':'-1','endDegress':'-1','startAge':'0','endAge':'0','gender':'-1','timeType':'1','startWorkYear':'-1','endWorkYear':'-1','isMember':'-1','cityId':1,'userToken':'8F37BC7626DC3CE0','clientType':2}

# data parse
# cityID{'北京':'1','上海':'2','深圳':'3','杭州':'4','广州':'5'}
# timetype('三天':'1','一周':'2')

citys = [1,2,3,4,5]
czcity = ['beijing','shanghai','shenzhen','hangzhou','guangzhou']
jobs = ['iOS','Android','php','java','python','C++','web']


def mysqlBlock(location,job,num,insertTime,md5):
	sqli="insert IGNORE into zhaopingou values(NULL,%s,%s,%s,%s,%s)"
	cursor.execute(sqli,(location,job,num,insertTime,md5))

def get_md5_value(src):
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest

host="localhost"
user='root'
passwd='9981aa'
db='justTest'
conn=MySQLdb.connect(host,user,passwd,db)
cursor=conn.cursor()

# cursor.execute("create table zhaopingou(location varchar(40) ,job varchar(20), num varchar(30), createTiem varchar(40))")


for city in citys:
	for job in jobs:
		# print(city)
		# print(job)
		# print(payload)
		headers['Cookie'] = cookie + str(city)
		payload['keyStrPostion'] = job
		r = requests.post(url,headers=headers,data=payload)
		binary = r.content
		data = json.loads(binary)
		count = str(data['total'])
		createTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
		src = czcity[int(city)-1] + job + createTime
		result_md5_value=get_md5_value(src.encode('utf8'))

		# print(czcity[int(city)-1] + '近三天' + job + '简历数' + count)
		mysqlBlock(czcity[int(city)-1],job,count,createTime,result_md5_value)

		
cursor.close()
conn.commit()
conn.close()



