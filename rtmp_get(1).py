import base64
import json

import cv2
import threading
import time
from timeit import default_timer as timer
#import win32gui, win32con


# 对图片byte数组进行str解码
import requests

#-*-coding:utf-8-*-
############导入计算机视觉库opencv和图像处理库PIL####################
from PIL import Image
import os
import cv2
import time
time1 = time.time()
def get_size(file):
    # 获取文件大小:KB
    size = os.path.getsize(file)
    return size
########################自定义图像压缩函数############################
def compress_image(infile,outfile,yuzhi=1024*1024):
    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param yuzhi: 阈值，超过该阈值则压缩,b
    """
    if get_size(infile) > yuzhi:
        with Image.open(infile) as im:
            width, height = im.size
            new_width = 1024
            new_height = int(new_width * height * 1.0 / width)
            print('adjusted size:', new_width, new_height)
            resized_im = im.resize((new_width, new_height))
            resized_im.save(outfile)
    return outfile, get_size(outfile)

def getByte(path):
    with open(path, 'rb') as f:
        img_byte = base64.b64encode(f.read())
    img_str = img_byte.decode('ascii')
    return img_str

class Producer(threading.Thread):
    """docstring for Producer"""

    def __init__(self, rtmp_str):

        super(Producer, self).__init__()

        self.rtmp_str = rtmp_str

        # 通过cv2中的类获取视频流操作对象cap
        self.cap = cv2.VideoCapture(self.rtmp_str)

        # 调用cv2方法获取cap的视频帧（帧：每秒多少张图片）
        # fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        print(self.fps)

        # 获取cap视频流的每帧大小
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.size = (self.width, self.height)
        print(self.size)
        # 定义编码格式mpge-4
        self.fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        # 定义视频文件输入对象
        self.outVideo = cv2.VideoWriter('saveDir1.avi', self.fourcc, self.fps, self.size)
    def run(self):
        print('in producer')
        ret, image = self.cap.read()
        print(ret)
        prev_time = timer()
        sleep_time = 0
        while ret:
            # if ret== True:
            self.outVideo.write(image)
            cv2.imshow('video', image)
            cv2.waitKey(int(1000 / int(self.fps)))  # 延迟
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.outVideo.release()
                self.cap.release()
                cv2.destroyAllWindows()
                break
            ret, image = self.cap.read()

            curr_time = timer()
            exec_time = curr_time - prev_time
            prev_time = curr_time
            sleep_time = sleep_time + exec_time
            if sleep_time > 5:
                sleep_time = sleep_time - 5
                path_temp="C:/RTMP/"+str(exec_time)+".png"
                cv2.imwrite(path_temp,image)
                compress_image(path_temp,path_temp)
                imgstr = getByte(path_temp)
                url = 'http://47.114.53.192:8080/Server2_0_war_exploded/Edge_Receiver'
                data = {'img': imgstr, 'lng': str(116.945902), 'lat': str(34.172711), 'device_id': 'spot_01'}
                json_mod = json.dumps(data)
                requests.post(url=url, data=json_mod)
                #


if __name__ == '__main__':
    print('run program')
    # rtmp_str = 'rtmp://live.hkstv.hk.lxdns.com/live/hks'  # 经测试，已不能用。可以尝试下面两个。
    # rtmp_str = 'rtmp://media3.scctv.net/live/scctv_800'  # CCTV
    # rtmp_str = 'rtmp://58.200.131.2:1935/livetv/hunantv'  # 湖南卫视

    # producer = Producer('rtmp://www.uav-space.com/vod2/uspace3.mp4')  # 开个线程
    producer = Producer('rtmp://s3.nsloop.com:3882/live/')  # 开个线程
    producer.start()
