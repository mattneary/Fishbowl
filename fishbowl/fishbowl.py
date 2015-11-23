from datetime import datetime
import funcy
import json
import os
import subprocess
import time

MY_PATH = os.path.dirname(__file__)
LIB_PATH = os.path.abspath(os.path.join(MY_PATH, '../lib'))


class ActivityStore(object):
    def __init__(self):
        self.boundaries = []
        self.current_app = None

    def record_app(self, app):
        if app != self.current_app:
            self.boundaries.append((app, datetime.now(),))
            self.current_app = app

    def flush(self):
        self.boundaries.append((None, datetime.now(),))
        ranges = funcy.pairwise(self.boundaries)
        self.boundaries = []
        self.current_app = None
        date_str = lambda d: d.strftime("%Y-%m-%d %H:%M:%S")
        return [(app, date_str(start), date_str(end)) for (app, start), (_, end) in ranges]

    def _osascript_call(self, script_name):
        '''Return the result of the applescript provided by name.'''
        return subprocess.check_output(['osascript', os.path.join(LIB_PATH, script_name)]).rstrip()

    def log_open_app(self):
        '''Get and record the name of the current app'''
        app = self._osascript_call('active.applescript')
        self.record_app(app)
        return app


if __name__ == '__main__':
    store = ActivityStore()

    i = 0
    while True:
        if not i % 60:
            print json.dumps(store.flush())
        store.log_open_app()
        time.sleep(5)
        i += 1

