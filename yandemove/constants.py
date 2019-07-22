# -*- coding: utf-8 -*-

from getpass import getuser

USERNAME = getuser()

AIM_PATH = r'C:\Users\{}\Pictures\舔图猫'.format(USERNAME)
RAW_PATH_LIST = [r'C:\Users\{}\Downloads'.format(USERNAME)]

RESULT_TEMPLATE = {
    'Title': '',
    'SubTitle': '',
    'IcoPath': 'Images/favicon.ico',
}

ACTION_TEMPLATE = {
    'JsonRPCAction': {
        'method': '',
        'parameters': [],
    }
}
