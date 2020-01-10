# coding: utf-8
import logging
# import os
# __author__ = 'liu.chunming'


def log(message):
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler('test.log')
    fh.setLevel(logging.DEBUG)
    # 定义handler的输出格式
    formatter = logging.Formatter('[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.error(message)
