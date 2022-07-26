'''
读取config.ini配置信息
'''
import os
import sys
import configparser

class Config():
    '''
    读取配置类
    '''

    @classmethod
    def set_path(cls,path=os.path.join(sys.path[0],'config.ini')):
        return path

    @classmethod
    def get_config(cls):
        config=configparser.ConfigParser()
        config_path=cls.set_path()
        if not os.path.exists(config_path):
            raise FileExistsError('配置文件不存在')
        config.read(filenames=config_path,encoding='utf-8')
        return config

    @classmethod
    def keepwindows(cls):
        return cls.get_config().get(section="TEST",option="keepwindows")

