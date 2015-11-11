import os
import subprocess
import time

MY_PATH = os.path.dirname(__file__)
LIB_PATH = os.path.abspath(os.path.join(MY_PATH, '../lib'))

def osascript_call(script_name):
    return subprocess.check_output(['osascript', os.path.join(LIB_PATH, script_name)]).rstrip()
def get_current_app():
    '''Get the name of the current app'''
    return osascript_call('active.applescript')

if __name__ == '__main__':
    while True:
        print get_current_app()
        time.sleep(5)

