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
import requests



print("即将对景区实时客流空间分布数据进行模拟...")

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
# ip随机生成池
RANDOM_IP_POOL=['192.168.10.222/0']
def __get_random_ip():
    str_ip = RANDOM_IP_POOL[random.randint(0,len(RANDOM_IP_POOL) - 1)]
    str_ip_addr = str_ip.split('/')[0]
    str_ip_mask = str_ip.split('/')[1]
    ip_addr = struct.unpack('>I',socket.inet_aton(str_ip_addr))[0]
    mask = 0x0
    for i in range(31, 31 - int(str_ip_mask), -1):
        mask = mask | ( 1 << i)
    ip_addr_min = ip_addr & (mask & 0xffffffff)
    ip_addr_max = ip_addr | (~mask & 0xffffffff)
    return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))
# 电话号码随机生成
def raddomPhone():
    headList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "186", "187", "188", "189"]
    return (random.choice(headList) + "".join(random.choice("0123456789") for i in range(8)))

jsonA=[]
for i in range(0,120):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.108804, base_lat=37.505338, radius=250)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(2,20)
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
    data['count'] =random.randint(10,30)
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
    data['count'] =random.randint(1,14)
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
    data['count'] =random.randint(1,14)
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
    data['count'] =random.randint(1,14)
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
    data['count'] =random.randint(15,35)
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
    data['count'] =random.randint(1,20)
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
    data['count'] =random.randint(1,20)
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
print("")

print("开始随机模拟龙霄公园 148个坐标点 人群空间密度检测数据")

jsonB=[]
for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.947097, base_lat=34.172719, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.94678, base_lat=34.172701, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.946276, base_lat=34.172715, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.945922, base_lat=34.172697, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.945632, base_lat=34.17271, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.945214, base_lat=34.17271, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.944855, base_lat=34.172728, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.9445, base_lat=34.172724, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.944093, base_lat=34.172724, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.943766, base_lat=34.17271, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.94339, base_lat=34.172719, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.943143, base_lat=34.172715, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.942789, base_lat=34.172724, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.942757, base_lat=34.17271, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.942376, base_lat=34.172715, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.941963, base_lat=34.172724, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(1,7)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,8):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.942843, base_lat=34.172724, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(9,20)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

for i in range(0,12):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=116.945707, base_lat=34.172693, radius=24)
    data['lng']=float(longitude_)
    data['lat']=float(latitude_)
    data['count'] =random.randint(9,15)
    data['date']=date_now
    data['time']=time_now
    data['scenic']='huancui_JiMuTing'
    data['device']='uav_03'
    jsonB.append(data)

print("龙霄公园人群密度json数据如下")
print(json.dumps(jsonB))
print("正在将随机模拟的 148个坐标点 填充入数据库")

for jsonChild in jsonB:
    lng=jsonChild['lng']
    lat=jsonChild['lat']
    count=jsonChild['count']
    date=jsonChild['date']
    timeB=jsonChild['time']
    scenic=jsonChild['scenic']
    device=jsonChild['device']
    data=(scenic,date,timeB,lng,lat,count,device)
    sql="INSERT INTO scenic_flow (scenic_id, record_date, record_time,spot_lng,spot_lat,person_count,data_source) VALUES ( '%s', '%s', '%s', '%s', '%s', '%s', '%s' )"
    cursor.execute(sql % data)
    connect.commit()
print("龙霄公园148条人群空间密度数据填充完成")
print("")
print("开始随机模拟游客游玩时空深度数据...")
sql_d_1="truncate table person_actual_location"
cursor.execute(sql_d_1)
jsonC=[]
ip_list01=[]
ip_list02=[]
ip_list03=[]
ip_list04=[]
# 随机生成时间
time_01=(int(time_temp.strftime('%Y')),int(time_temp.strftime('%m')),int(time_temp.strftime('%d')),int(time_temp.strftime('%H')),int(time_temp.strftime('%M')),int(time_temp.strftime('%S')),0,0,0)
time_02=(int(time_temp.strftime('%Y')),int(time_temp.strftime('%m')),int(time_temp.strftime('%d')),int(time_temp.strftime('%H'))-1,int(time_temp.strftime('%M')),int(time_temp.strftime('%S')),0,0,0)
time_03=(int(time_temp.strftime('%Y')),int(time_temp.strftime('%m')),int(time_temp.strftime('%d')),int(time_temp.strftime('%H'))-4,int(time_temp.strftime('%M')),int(time_temp.strftime('%S')),0,0,0)
stamp01=time.mktime(time_01)
stamp02=time.mktime(time_02)
stamp03=time.mktime(time_03)

time_list01=[]
time_list02=[]
time_list03=[]
time_list04=[]
time_list05=[]
time_list06=[]
time_list07=[]
time_list08=[]

# 现在～1.5小时之前
for i in range(0,12):
    t=random.randint(stamp02,stamp01)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    time_list01.append(time.strftime("%H:%M:%S",date_touple))  #将时间元组转成格式化字符串（1976-05-21）
for i in range(0,24):
    t=random.randint(stamp02,stamp01)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    time_list02.append(time.strftime("%H:%M:%S",date_touple))  #将时间元组转成格式化字符串（1976-05-21）
for i in range(0,15):
    t=random.randint(stamp02,stamp01)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    time_list03.append(time.strftime("%H:%M:%S",date_touple))  #将时间元组转成格式化字符串（1976-05-21）
for i in range(0,40):
    t=random.randint(stamp02,stamp01)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    time_list04.append(time.strftime("%H:%M:%S",date_touple))  #将时间元组转成格式化字符串（1976-05-21）

# 1.5小时～3.5小时之前
for i in range(0,12):
    t=random.randint(stamp03,stamp02)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    time_list05.append(time.strftime("%H:%M:%S",date_touple))  #将时间元组转成格式化字符串（1976-05-21）
for i in range(0,24):
    t=random.randint(stamp03,stamp02)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    time_list06.append(time.strftime("%H:%M:%S",date_touple))  #将时间元组转成格式化字符串（1976-05-21）
for i in range(0,15):
    t=random.randint(stamp03,stamp02)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    time_list07.append(time.strftime("%H:%M:%S",date_touple))  #将时间元组转成格式化字符串（1976-05-21）
for i in range(0,40):
    t=random.randint(stamp03,stamp02)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    time_list08.append(time.strftime("%H:%M:%S",date_touple))  #将时间元组转成格式化字符串（1976-05-21）

# 盆景园
for i in range(0,12):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.11479, base_lat=37.504803, radius=90)
    ip_list01.append(str(__get_random_ip()))
    data['person_ip']=ip_list01[i]
    data['person_tel']=str(raddomPhone())
    data['record_date']=date_now
    data['record_time']=random.choice(time_list05)
    data['scenic_id']='huancui_PenJing'
    data['person_lng'] = float(longitude_)
    data['person_lat'] = float(latitude_)
    jsonC.append(data)
# 环翠楼
for i in range(0,24):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.112678, base_lat=37.504974, radius=130)
    ip_list02.append(str(__get_random_ip()))
    data['person_ip']=ip_list02[i]
    data['person_tel']=str(raddomPhone())
    data['record_date']=date_now
    data['record_time']=random.choice(time_list06)
    data['scenic_id']='huancui_Building'
    data['person_lng'] = float(longitude_)
    data['person_lat'] = float(latitude_)
    jsonC.append(data)
for i in range(0,15):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.10845, base_lat=37.50517, radius=170)
    ip_list03.append(str(__get_random_ip()))
    data['person_ip']=ip_list03[i]
    data['person_tel']=str(raddomPhone())
    data['record_date']=date_now
    data['record_time']=random.choice(time_list07)
    data['scenic_id']='huancui_JiMuTing'
    data['person_lng'] = float(longitude_)
    data['person_lat'] = float(latitude_)
    jsonC.append(data)
for i in range(0,40):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.103381, base_lat=37.505161, radius=80)
    ip_list04.append(str(__get_random_ip()))
    data['person_ip']=ip_list04[i]
    data['person_tel']=str(raddomPhone())
    data['record_date']=date_now
    data['record_time']=random.choice(time_list08)
    data['scenic_id']='huancui_KongMiao'
    data['person_lng'] = float(longitude_)
    data['person_lat'] = float(latitude_)
    jsonC.append(data)


# 盆景园
for i in range(0,12):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.11479, base_lat=37.504803, radius=90)
    # ip_list01.append(str(__get_random_ip()))
    data['person_ip']=ip_list01[i]
    data['person_tel']=str(raddomPhone())
    data['record_date']=date_now
    data['record_time']=random.choice(time_list01)
    data['scenic_id']='huancui_PenJing'
    data['person_lng'] = float(longitude_)
    data['person_lat'] = float(latitude_)
    jsonC.append(data)
# 环翠楼
for i in range(0,24):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.112678, base_lat=37.504974, radius=130)
    # ip_list02.append(str(__get_random_ip()))
    data['person_ip']=ip_list02[i]
    data['person_tel']=str(raddomPhone())
    data['record_date']=date_now
    data['record_time']=random.choice(time_list02)
    data['scenic_id']='huancui_Building'
    data['person_lng'] = float(longitude_)
    data['person_lat'] = float(latitude_)
    jsonC.append(data)
for i in range(0,15):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.10845, base_lat=37.50517, radius=170)
    # ip_list03.append(str(__get_random_ip()))
    data['person_ip']=ip_list03[i]
    data['person_tel']=str(raddomPhone())
    data['record_date']=date_now
    data['record_time']=random.choice(time_list03)
    data['scenic_id']='huancui_JiMuTing'
    data['person_lng'] = float(longitude_)
    data['person_lat'] = float(latitude_)
    jsonC.append(data)
for i in range(0,40):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.103381, base_lat=37.505161, radius=80)
    # ip_list04.append(str(__get_random_ip()))
    data['person_ip']=ip_list04[i]
    data['person_tel']=str(raddomPhone())
    data['record_date']=date_now
    data['record_time']=random.choice(time_list04)
    data['scenic_id']='huancui_KongMiao'
    data['person_lng'] = float(longitude_)
    data['person_lat'] = float(latitude_)
    jsonC.append(data)
print("游客游玩时空深度数据如下")
print("正在将随机模拟的 182条 游客游玩时空深度数据填充入数据库")
print(json.dumps(jsonC))
for jsonChild in jsonC:
    person_ip=jsonChild['person_ip']
    person_tel=jsonChild['person_tel']
    record_date=jsonChild['record_date']
    record_time=jsonChild['record_time']
    scenic_id=jsonChild['scenic_id']
    person_lng=jsonChild['person_lng']
    person_lat=jsonChild['person_lat']
    data=(person_ip,person_tel,record_date,record_time,scenic_id,person_lng,person_lat)
    sql="INSERT INTO person_actual_location (person_ip,person_tel,record_date,record_time,scenic_id,person_lng,person_lat) VALUES ( '%s', '%s', '%s', '%s', '%s', '%s', '%s' )"
    cursor.execute(sql % data)
    connect.commit()
print("游客游玩时空深度182条数据填充完成")
print("")
print("开始随机模拟 12条 环翠楼公园游客求助数据...")
print("环翠楼公园游客求助json数据如下")

# 随机生成时间
time_E=(int(time_temp.strftime('%Y')),int(time_temp.strftime('%m')),int(time_temp.strftime('%d')),int(time_temp.strftime('%H')),int(time_temp.strftime('%M')),int(time_temp.strftime('%S')),0,0,0)
time_B=(int(time_temp.strftime('%Y')),int(time_temp.strftime('%m')),int(time_temp.strftime('%d')),int(time_temp.strftime('%H'))-2,int(time_temp.strftime('%M')),int(time_temp.strftime('%S')),0,0,0)
stampE=time.mktime(time_E)
stampB=time.mktime(time_B)
time_list_help=[]
scenic_list=['huancui_KongMiao','huancui_PenJing','huancui_Building','huancui_JiMuTing']
for i in range(0,12):
    t = random.randint(stampB, stampE)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    time_list_help.append(time.strftime("%H:%M:%S", date_touple))  # 将时间元组转成格式化字符串（1976-05-21）
jsonD=[]
for i in range(0,12):
    data={}
    longitude_, latitude_ = generate_random_gps(base_log=122.112678, base_lat=37.504974, radius=130)
    data['record_date']=date_now
    data['record_time']=random.choice(time_list_help)
    data['person_tel']=str(raddomPhone())
    data['person_lng'] = float(longitude_)
    data['person_lat'] = float(latitude_)
    data['scenic_id']=random.choice(scenic_list)
    jsonD.append(data)
sql_help_d="truncate table person_help"
cursor.execute(sql_help_d)
print(json.dumps(jsonD))

print("正在将随机模拟的 12条 环翠楼公园游客求助数据填充入数据库")
for jsonChild in jsonD:
    record_date=jsonChild['record_date']
    record_time=jsonChild['record_time']
    person_tel=jsonChild['person_tel']
    person_lng=jsonChild['person_lng']
    person_lat=jsonChild['person_lat']
    scenic_id=jsonChild['scenic_id']
    data=(record_date,record_time,person_tel,person_lng,person_lat,scenic_id)
    sql="INSERT INTO person_help (record_date,record_time,person_tel,person_lng,person_lat,scenic_id) VALUES ( '%s', '%s', '%s', '%s', '%s', '%s')"
    cursor.execute(sql % data)
    connect.commit()
print("环翠楼公园 12条 游客求助数据填充完成")

print("")
print("开始随机模拟 5条 危险区域游客数据...")
print("危险区域游客json数据如下")

jsonE=[]
for i in range(0,5):
    data={}
    #设置隧道口为危险区域
    longitude_, latitude_ = generate_random_gps(base_log=122.108575, base_lat=37.506407, radius=15)
    data['record_date']=date_now
    data['record_time']=random.choice(time_list_help)
    data['person_lng'] = float(longitude_)
    data['person_lat'] = float(latitude_)
    data['person_ip']=str(__get_random_ip())
    jsonE.append(data)
sql_danger_d="truncate table dangerous_person"
cursor.execute(sql_danger_d)
print(json.dumps(jsonE))

print("正在将随机模拟的 5条 危险区域游客数据填充入数据库")
for jsonChild in jsonE:
    record_date=jsonChild['record_date']
    record_time=jsonChild['record_time']
    person_lng=jsonChild['person_lng']
    person_lat=jsonChild['person_lat']
    person_ip=jsonChild['person_ip']
    data=(record_date,record_time,person_lng,person_lat,person_ip)
    sql="INSERT INTO dangerous_person (record_date,record_time,person_lng,person_lat,person_ip) VALUES ( '%s', '%s', '%s', '%s', '%s')"
    cursor.execute(sql % data)
    connect.commit()
print("环翠楼公园 5条 危险区域游客数据填充完成")

print("")

print("正在准备环翠楼公园历史客流量数据...")
sql_f_d = "truncate table flow_actual_time"
sql_s_d="truncate table scenic_person_sum"
cursor.execute(sql_f_d)
cursor.execute(sql_s_d)
print('正在将 9636条 历史客流量数据写入数据库')

# 景点列表
scenic_list_d=['huancui_Building','huancui_JiMuTing','huancui_KongMiao','huancui_PenJing']


# 时间 8:00~20:00


time_begin2 = '2020-06-01 8:00:00'
time_temp2 = datetime.datetime.strptime(time_begin2, '%Y-%m-%d %H:%M:%S')
delta2 = datetime.timedelta(days=1)
# 38对应7月8日
for k in range(0,40):
    date_temp_str=time_temp2.strftime('%Y-%m-%d')
    time_temp2 = time_temp2 + delta2

    time_begin = '2020-06-01 8:00:00'
    time_temQ = datetime.datetime.strptime(time_begin, '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(minutes=10)
    if k==39:
        print("正在准备最后一天的数据")
        # 50对应18：10分
        # 42对应16：50分
        # 40对应16：30分 37
        for i in range(0,40):

            time_temp_str = time_temQ.strftime('%H:%M:%S')
            time_temQ = time_temQ + delta
            # 日期和时间准备就绪

            # 生成随机数
            person_count = []
            if (k < 10):
                person_count.append(int(random.uniform(10, 30)))
                person_count.append(int(random.uniform(5, 48)))
                person_count.append(int(random.uniform(20, 60)))
                person_count.append(int(random.uniform(12, 35)))
            elif (k > 10 and k < 20):
                person_count.append(int(random.uniform(20, 40)))
                person_count.append(int(random.uniform(10, 20)))
                person_count.append(int(random.uniform(0, 50)))
                person_count.append(int(random.uniform(13, 35)))
            else:
                person_count.append(int(random.uniform(25, 55)))
                person_count.append(int(random.uniform(13, 32)))
                person_count.append(int(random.uniform(15, 90)))
                person_count.append(int(random.uniform(21, 45)))
            # 上传数据
            for l in range(0, 4):
                # print(date_temp_str+" "+time_temp_str+" "+str(person_count[l])+" "+scenic_list_d[l])
                sql2 = "INSERT INTO flow_actual_time (record_date, record_time, person_count,scenic_id) VALUES ( '%s', '%s', '%s', '%s' )"
                data = (date_temp_str, time_temp_str, str(person_count[l]), scenic_list_d[l])
                cursor.execute(sql2 % data)
                connect.commit()
            # 人群总数
            person_sum = person_count[0] + person_count[1] + person_count[2] + person_count[3]
            sql3 = "INSERT INTO scenic_person_sum(record_date,record_time,person_sum) VALUES ('%s', '%s', '%s')"
            data2 = (date_temp_str, time_temp_str, str(person_sum))
            cursor.execute(sql3 % data2)
            connect.commit()
    else:
        for i in range(0, 73):
            time_temp_str=time_temQ.strftime('%H:%M:%S')
            time_temQ = time_temQ + delta
            # 日期和时间准备就绪

            # 生成随机数
            person_count=[]
            if (k<10):
                person_count.append(int(random.uniform(10,30)))
                person_count.append(int(random.uniform(5,48)))
                person_count.append(int(random.uniform(20,60)))
                person_count.append(int(random.uniform(12,35)))
            elif (k>10 and k<20):
                person_count.append(int(random.uniform(20, 40)))
                person_count.append(int(random.uniform(10, 20)))
                person_count.append(int(random.uniform(0, 50)))
                person_count.append(int(random.uniform(13, 35)))
            else:
                person_count.append(int(random.uniform(25, 55)))
                person_count.append(int(random.uniform(13, 32)))
                person_count.append(int(random.uniform(15, 90)))
                person_count.append(int(random.uniform(21, 45)))
            # 上传数据
            for l in range(0,4):
                # print(date_temp_str+" "+time_temp_str+" "+str(person_count[l])+" "+scenic_list_d[l])
                sql2 = "INSERT INTO flow_actual_time (record_date, record_time, person_count,scenic_id) VALUES ( '%s', '%s', '%s', '%s' )"
                data=(date_temp_str,time_temp_str,str(person_count[l]),scenic_list_d[l])
                cursor.execute(sql2 % data)
                connect.commit()
            # 人群总数
            person_sum=person_count[0]+person_count[1]+person_count[2]+person_count[3]
            sql3="INSERT INTO scenic_person_sum(record_date,record_time,person_sum) VALUES ('%s', '%s', '%s')"
            data2=(date_temp_str,time_temp_str,str(person_sum))
            cursor.execute(sql3 % data2)
            connect.commit()

print('环翠楼公园 9636条数据 填充完成')
print('')
print('最后处理数据杂项')
sql_dd="insert into danger_count_history(record_date,count) values ('%s','%s')"
data_dd=(date_now,str(10))
cursor.execute(sql_dd % data_dd)
connect.commit()

print('数据杂项处理完成')

print("正在断开数据库连接...")

cursor.close()
connect.close()

print("已断开数据库连接")
