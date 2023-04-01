import logging 
import time
import os
import sys


my_logger = logging.Logger("service-logger", logging.INFO)


def app_log(msg, level = logging.INFO):
    my_logger.log(level, msg, extra={
        'log_layer': 'App'
    })

def api_log(msg, level = logging.INFO):
    my_logger.log(level, msg, extra={
        'log_layer': 'API'
    })

def domain_log(msg, level = logging.INFO):
    my_logger.log(level, msg, extra={
        'log_layer': 'Domain'
    })

def data_log(msg, level = logging.INFO):
    my_logger.log(level, msg, extra={
        'log_layer': 'Data'
    })


def configure_logging():
    FORMAT = logging.Formatter('[%(log_layer)s][%(asctime)s]: %(message)s')
    file_name = "{0}/{1}.log".format('logs/', time.ctime().replace(' ', '_').replace(':', '-'))
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    fileHandler = logging.FileHandler(file_name)
    fileHandler.setFormatter(FORMAT)
    my_logger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(FORMAT)
    my_logger.addHandler(consoleHandler)

    app_log('Initialized logging')