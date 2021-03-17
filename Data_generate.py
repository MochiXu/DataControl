import datetime
from datetime import timedelta
import json
import random
import math
import time


#  参数含义
# base_log：经度基准点，
# base_lat：维度基准点，
# radius：距离基准点的半径
import socket
import struct

import pymysql
print("数据库连接初始化...")


# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    # host='47.114.53.192',
    port=3306,
    user='xmc',
    passwd='294207',
    db='deeppupil',
    charset='utf8'
)
print("成功建立数据库连接")

print("")
# 数据随机模拟日期
time_temp = datetime.datetime.now()
date_now=time_temp.strftime('%Y-%m-%d')
time_now=time_temp.strftime('%H:%M:%S')
# 模拟数据的前三个半小时


# 获取游标
cursor = connect.cursor()
print("开始对环翠楼公园随机模拟 650个坐标点 人群空间密度检测数据")
print("环翠楼公园人群空间密度json数据如下")
# GPS坐标随机生成
def generate_random_gps(base_log=None, base_lat=None, radius=None):
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    longitude = y + base_log
    latitude = x + base_lat
    # 这里是想保留14位小数
    loga = '%.6f' % longitude
    lata = '%.6f' % latitude
    return loga, lata

jsonA=[]
for i in range(0,120):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.108804, base_lat=37.505338, radius=250)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,3)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonA.append(data)

for i in range(0,120):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.104269, base_lat=37.504811, radius=205)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(2,4)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_KongMiao'
    data['device']='uav_04'
    jsonA.append(data)

for i in range(0,60):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.10605, base_lat=37.505594, radius=100)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,3)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonA.append(data)


for i in range(0,50):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.104151, base_lat=37.507177, radius=150)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,2)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonA.append(data)

for i in range(0,50):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.106339, base_lat=37.503866, radius=100)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,3)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonA.append(data)

for i in range(0,50):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.113099, base_lat=37.50459, radius=160)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(2,3)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_Building'
    data['device']='uav_02'
    jsonA.append(data)

for i in range(0,100):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.111253, base_lat=37.505032, radius=200)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,3)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_Building'
    data['device']='uav_02'
    jsonA.append(data)

for i in range(0,100):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.114857, base_lat=37.504844, radius=100)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,3)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_PenJing'
    data['device']='uav_01'
    jsonA.append(data)
print(json.dumps(jsonA))

# requests.post(url='http://localhost:8080/RecevieImage_war_exploded/DataBase', data=json.dumps(jsonA))


print("正在将随机模拟的 650 个坐标点填充入数据库")
sql_d_1="truncate table scenic_flow"
cursor.execute(sql_d_1)

for jsonChild in jsonA:
    lng=jsonChild['lng']
    lat=jsonChild['lat']
    count=jsonChild['count']
    date=jsonChild['date']
    timeA=jsonChild['time']
    scenic=jsonChild['scenic']
    device=jsonChild['device']
    data=(scenic,date,timeA,lng,lat,count,device)
    sql="INSERT INTO scenic_flow (scenic_id, record_date, record_time,spot_lng,spot_lat,person_count,data_source) VALUES ( '%s', '%s', '%s', '%s', '%s', '%s', '%s' )"
    cursor.execute(sql % data)
    connect.commit()
print("环翠楼公园650条人群空间密度数据填充完成")

print("")
