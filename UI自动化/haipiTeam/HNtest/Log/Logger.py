import logging
import os
import sys
import time

class Logger(object):
    def __init__(self,logger):
        '''
        指定日志文件的路径和日志级别
        :param logger:
        '''
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            #创建一个handler用于写入日志文件
            rztime=time.strftime('%Y%m%H%M',time.localtime(time.time()))
            projectdir = sys.path[0]
            report_dir = projectdir + '\\report'
            if os.path.exists(report_dir):
                for i, x, name in os.walk(report_dir):
                    n=x[-1]
                    if x[-1] == "pic":
                        new_reportName = x[-2]
                    else:
                        new_reportName = x[-1]
                    projectdir = os.path.join(report_dir, new_reportName, 'logs\\')
                    if not os.path.exists(projectdir):
                        os.mkdir(projectdir)
                    break
            log_name=projectdir+rztime+'.log'
            flog=logging.FileHandler(log_name,mode='a',encoding='utf-8')
            flog.setLevel(logging.INFO)
            #创建一个handler用户控制台输出
            clog=logging.StreamHandler()
            clog.setLevel(logging.INFO)
            #定义handler的输出格式
            formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
            flog.setFormatter(formatter)
            clog.setFormatter(formatter)
            #给logger定义handler
            self.logger.addHandler(flog)
            self.logger.addHandler(clog)
    def getlog(self):
        return self.logger
