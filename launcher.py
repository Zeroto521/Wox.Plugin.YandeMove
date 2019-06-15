# -*- coding: utf-8 -*-

import copy
import os
import re
import shutil
from getpass import getuser

from send2trash import send2trash

from pytest import testit
from wox import Wox, WoxAPI

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

reg = re.compile(r'^yande\.re.+?\d+?.*?\.(png|jpg|jpeg)$', flags=re.I)


class Main(Wox):

    def query(self, key):
        """Wox dealing programm

        Returns:
            list -- wox json list
        """

        result = []

        counter = 0

        for raw_path in RAW_PATH_LIST:
            for file in os.listdir(raw_path):
                if reg.match(file):  # find the yande's pictures
                    raw = os.path.join(raw_path, file)
                    aim = os.path.join(AIM_PATH, file)

                    if not os.path.exists(aim):
                        # move picture to aim path
                        shutil.move(raw, aim)
                        counter += 1
                    else:
                        # sand to win sys recycle
                        send2trash(raw)

        title = "{} pictures have been moved.".format(counter)
        subtitle = 'Click to open the aim folder in window.'
        method = 'openFolder'
        result.append(self.genaction(title, subtitle, method, AIM_PATH))

        return result

    @staticmethod
    def genaction(tit, subtit, method, actparam):
        """Generate wox json data with copy action

        Arguments:
            title {str} -- as name
            actparam {str} -- the paramter which need to copy

        Returns:
            json -- wox json
        """

        res = copy.deepcopy(RESULT_TEMPLATE)
        res['Title'] = tit
        res['SubTitle'] = subtit

        action = copy.deepcopy(ACTION_TEMPLATE)
        action['JsonRPCAction']['method'] = method
        action['JsonRPCAction']['parameters'] = [actparam]
        res.update(action)

        return res

    def openFolder(self, path):
        os.startfile(path)
        WoxAPI.change_query(path)


if __name__ == '__main__':
    Main()
