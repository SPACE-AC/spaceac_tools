try:
    from _global import *
except:
    from ._global import *


class RTC:
    def __init__(self):
        self.start_time = time.time()

    @staticmethod
    def format_time(time):
        time_list = [str(time.hour).zfill(2), str(time.minute).zfill(
            2), str(time.second).zfill(2), str(time.microsecond)[0:3]]
        timen = ' '.join(
            time_list) if time.second % 2 == 0 else ':'.join(time_list)
        return timen

    @staticmethod
    def time_local():
        time = datetime.now().time()
        return RTC.format_time(time)

    @staticmethod
    def time_UTC():
        time = datetime.utcnow().time()
        return RTC.format_time(time)

    def time_elapsed(self):
        delta = time.time() - self.start_time
        second = round(delta % 60)
        microsecond = str(datetime.now().time().microsecond)[:2]
        minute = delta // 60
        minute = minute % 60
        hour = minute // 60
        time_list = [str(round(hour)), str(round(minute)),
                     str(round(second)), microsecond]
        timestp = ' '.join(
            time_list) if second % 2 == 0 else ':'.join(time_list)
        return timestp

    @staticmethod
    def date_local():
        return datetime.now().date()

    @staticmethod
    def date_UTC():
        return datetime.utcnow().date()


if __name__ == '__main__':
    print(f'Local: {RTC.date_local()} {RTC.time_local()}')
    print(f'UTC: {RTC.date_UTC()} {RTC.time_UTC()}')
    clock = RTC()
