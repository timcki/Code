from simple_timer import Timer
from time import sleep

class Session:

    def __init__(self, session_time=25):
        self.timer = Timer()
        self.session_time = session_time

    def check_if_finished(self):
        if self.timer.duration > self.session_time * 60:
            return False
        else: return True

    def time_elapsed(self):
        minutes = int(self.timer.duration / 60)
        seconds = int(self.timer.duration % 60)
        return "{}:{}".format(minutes, seconds)


session = Session()

session_active = True;
while session_active:
    sleep(1)
    session_active = session.check_if_finished()
    print("\rTime elapsed: {}".format(session.time_elapsed()), end='')
