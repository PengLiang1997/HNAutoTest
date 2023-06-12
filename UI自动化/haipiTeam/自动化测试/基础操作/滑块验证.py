import sys
import os
import cv2
import numpy as np
import time
import shutil


from HNtest.testcasesec.testcasesec import page
from HNtest.Secselenium.secdriver import Secdriver
from ..元素对象库.登录页 import *


class 滑块验证(page):
    flage = 0
    def __init__(self,Secdriver=None):
        page.__init__(self,secdriver=Secdriver)

    def matchImg(self,imgPath1,imgPath2):
        imgs = []
        # 原始图像，用于展示
        sou_img1 = cv2.imread(imgPath1)
        sou_img2 = cv2.imread(imgPath2)
        # 原始图像，灰度
        # 最小阈值100,最大阈值500
        strtime = str(int(time.time()))
        img1 = cv2.imread(imgPath1, 0)
        blur1 = cv2.GaussianBlur(img1, (3, 3), 0)
        canny1 = cv2.Canny(blur1, 200, 400)
        tempName1 = 'temp1_' + strtime + '.png'
        cv2.imwrite("report\pic\\"+tempName1, canny1)
        img2 = cv2.imread(imgPath2, 0)
        blur2 = cv2.GaussianBlur(img2, (3, 3), 0)
        canny2 = cv2.Canny(blur2, 200, 400)
        tempName2='temp2_'+strtime+'.png'
        cv2.imwrite("report\pic\\"+tempName2, canny2)
        target = cv2.imread("report\pic\\"+f'temp1_{strtime}.png')
        template = cv2.imread("report\pic\\"+f'temp2_{strtime}.png')
        # 调整显示大小
        target_temp = cv2.resize(sou_img1, (350, 200))
        target_temp = cv2.copyMakeBorder(target_temp, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        template_temp = cv2.resize(sou_img2, (200, 200))
        template_temp = cv2.copyMakeBorder(template_temp, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        imgs.append(target_temp)
        imgs.append(template_temp)
        theight, twidth = template.shape[:2]
        # 匹配拼图
        result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
        # 归一化
        cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # equal=int(int(max_loc[0]-min_loc[0]))
        return int(max_loc[0])
    def 清理pic目录(self):
        firpath = sys.path[0]
        picpath=firpath+'\\report\pic'
        if os.path.exists(picpath):
            if os.listdir(picpath):
                for j in os.listdir(picpath):
                    filedata = picpath + "\\" + j
                    os.remove(filedata)
        else:
            os.makedirs(rf"{picpath}")


    def 滑块验证操作(self):
        self.清理pic目录()
        self.flage+=1
        self.default_content()
        self.wait(人机验证弹窗对象库.弹窗标题,1)
        # #获取背景图src
        # targetUrl=self.driver.getelement(人机验证弹窗对象库.背景图).get_attribute('src')
        # #获取拼图src
        # tempUrl=self.driver.getelement(人机验证弹窗对象库.拼图).get_attribute('src')
        # #新建标签页
        # self.driver.driver.execute_script("window.open('');")
        # self.switch_to_new_window()
        # self.driver.driver.get(targetUrl)
        # time.sleep(3)
        # #截图
        # strtime=str(int(time.time()))
        # backtarget1='temp_target_'+f'{strtime}'+'.png'
        # self.get_screenshot(path='report\pic\\'+backtarget1)
        # w=310
        # h=155
        # img=cv2.imread('report\pic\\'+backtarget1)
        # size=img.shape
        # top = int((size[0] - h) / 2)
        # height = int(h + ((size[0] - h) / 2))
        # left = int((size[1] - w) / 2)
        # width = int(w + ((size[1] - w) / 2))
        #
        # cropped = img[top:height, left:width]
        # #裁剪
        # backtarget2='temp_target_crop_'+f'{strtime}'+'.png'
        # cv2.imwrite("report\pic\\"+backtarget2,cropped)
        # self.driver.close()
        # self.switch_to_window_byTagName("HAPYTEAM 管理您的设计数据")
        #
        # #新建标签页
        # self.driver.driver.execute_script("window.open('');")
        # self.switch_to_new_window()
        # self.driver.driver.get(tempUrl)
        # time.sleep(3)
        # #截图
        # target1 = 'temp_temp_' + f'{strtime}' + '.png'
        # self.get_screenshot(path='report\pic\\'+target1)
        # w=47
        # h=155
        # img = cv2.imread('report\pic\\'+target1)
        # size = img.shape
        # top = int((size[0] - h) / 2)
        # height = int(h + ((size[0] - h) / 2))
        # left = int((size[1] - w) / 2)
        # width = int(w + ((size[1] - w) / 2))
        # cropped = img[top:height, left:width]
        # #裁剪
        # target2 = 'temp_temp_crop_' + f'{strtime}' + '.png'
        # cv2.imwrite('report\pic\\'+target2, cropped)
        # self.driver.close()
        # self.switch_to_window_byTagName("HAPYTEAM 管理您的设计数据")
        #
        # #模糊匹配
        # move=self.matchImg('report\pic\\'+backtarget2,'report\pic\\'+target2)
        self.drag_and_drop_by_offset(srpath=人机验证弹窗对象库.滑动按钮,offset_x=150,offset_y=0)
        if self.wait('//*[text()="验证失败"]',1):
            if self.flage>20:
                raise RuntimeError("人机验证失败")
            else:
                self.滑块验证操作()

