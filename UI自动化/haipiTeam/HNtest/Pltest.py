#coding:utf-8
import sys
import os
import time
import unittest as unittest
import pandas as pd
from HNtest.BeautifulReport import BeautifulReport
from HNtest.Log.Logger import Logger

global testurl
testurl=''

class Pltest(object):

    def __init__(self,project_path=None):
        if project_path:
            self.project_path=project_path
        else:
            self.project_path=sys.path[0]

    def mkdir_report(self,project_path,time):
        '''
        生成测试报告文件夹，并返回文件路径
        :param project_path: 项目路径
        :param time: 执行时间
        :return: 返回reportpath
        '''
        reportpath = project_path+ '\\report\\{}'.format(time)
        os.makedirs(rf"{reportpath}")
        return reportpath

    def get_projectconf(self):
        '''
        获取项目测试配置.xlsx的配置信息
        :return: 要执行的项目的列表
        '''
        cf=pd.read_excel(io=self.project_path+"\项目测试配置.xlsx",sheet_name=0)
        maxrow=cf.shape[0]
        files=[]
        for row in range(maxrow):
            if self.isrun(cf.at[row,"是否执行"]):
                filename=cf.at[row,"文件名"]
                modulename=cf.at[row,"模块名称"]
                urlstr=cf.at[row,"测试环境"]
                files.append([filename,modulename,urlstr])
        return files

    def get_testplan(self,modulename,filename):
        '''
        获取自动化用例执行计划.xlsx的配置信息
        :param modulename: 代码模块的名称，如自动化测试
        :return: 要执行的文件或类或方法的信息
        '''
        planpath=self.project_path+"\\"+modulename+"\\"+filename
        pf=pd.read_excel(io=planpath,sheet_name=0)
        maxrow=pf.shape[0]
        plans=[]
        for row in range(maxrow):
            if self.isrun(pf.at[row,"是否执行"]):
                testway=pf.at[row,"运行方式"]
                testpath=pf.at[row,"测试套件文件夹名称"]
                testfile=pf.at[row,"文件名称"]
                testclass=pf.at[row,"类名"]
                testfun=pf.at[row,"方法名"]
                plans.append([testway,testpath,testfile,testclass,testfun])
        return plans

    def runcase(self):
        confs=self.get_projectconf()
        if confs:
            for conf in confs:
                global testurl
                testurl = conf[2]
                plans=self.get_testplan(modulename=conf[1],filename=conf[0])
                for plan in plans:
                    now = time.strftime('%m%d%H%M%S')
                    suite = unittest.TestSuite()
                    testLoader = unittest.TestLoader()
                    report_path=self.mkdir_report(project_path=self.project_path,time=now)
                    logger = Logger(logger='logger').getlog()
                    if plan[0]=="1-按方法运行":
                        strimport=f'from {conf[1]}.{plan[1]}.{plan[2]} import *'
                        exec(strimport)
                        case="suite.addTest("+plan[3]+"('"+plan[4]+"'))"
                        exec(case)

                        logger.info("测试套件构建完成，开始执行测试方法>>>>")
                        testsuite = str(suite)
                        truesuite=testsuite[35:-3]
                        logger.info(truesuite)

                        BeautifulReport(suite).report(filename=f'{now}', description='用例执行详细信息', report_dir=report_path)
                    if plan[0]=="2-按类运行":
                        strimport=f"{conf[1]}.{plan[1]}.{plan[2]}.{plan[3]}"
                        suite.addTest(testLoader.loadTestsFromName(strimport))
                        logger.info("测试套件构建完成，开始执行测试方法>>>>")
                        # testsuite=str(suite)
                        # strsuite = testsuite[66:-4]
                        # suitelist=strsuite.split(",")
                        # for thesuite in suitelist:
                        #     testcalss=thesuite[thesuite.index("Test_"):thesuite.index(" ")]
                        #     testmethod=thesuite[thesuite.index("test_"):-1]
                        #     suite2 = unittest.TestSuite()
                        #     strimport = f'from {conf[1]}.{plan[1]}.{plan[2]} import *'
                        #     exec(strimport)
                        #     case = "suite2.addTest(" + testcalss + "('" +testmethod+ "'))"
                        #     exec(case)
                        #     logger.info(thesuite)
                        #     BeautifulReport(suite2).report(filename=f'{now}', description='用例执行详细信息',
                        #                                   log_path=report_path)

                        BeautifulReport(suite).report(filename=f'{now}', description='用例执行详细信息', report_dir=report_path)
                    if plan[0]=="3-按文件运行":
                        testfile = 'testfile'
                        strimport = f'import {conf[1]}.{plan[1]}.{plan[2]} as {testfile}'
                        exec(strimport)
                        suite.addTest(testLoader.loadTestsFromModule(testfile))
                        BeautifulReport(suite).report(filename=f'{now}', description='用例执行详细信息', report_dir=report_path)
        else:
            raise RuntimeError("项目测试配置.xlsx文件中没有可运行的选项")

    def isrun(self,value):
        '''
        判断配置文件是否执行
        :param value:
        :return: 返回bool
        '''
        if "n"==value or "N"==value:
            return False
        else:
            return True

    def seturl_by_txt(self,modulename,url):
        filepath = str(self.project_path) +'\\'+modulename +'TestData\\TempData\\url.txt'
        file = open(filepath, "w")
        file.write(url)
        file.close()
