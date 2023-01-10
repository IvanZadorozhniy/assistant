'''Module helps work with different types of time and date in proper way'''
import time
from datetime import datetime

import utils


class TimeApi():
    '''Class works with time and date'''

    def get_current_time(self):
        '''return current time'''
        return time.localtime()

    def get_description_current_time(self):
        '''create description of time for tts'''
        cur_time = self.get_current_time()
        hours = utils.number_to_words(time.strftime("%H", cur_time))
        minutes = utils.number_to_words(time.strftime("%M", cur_time))
        full_description = f'''
                The current time is {hours} hours, and {minutes} minutes
            '''
        return full_description

    def get_daytime_now(self):
        '''return day and time for now'''
        return datetime.now()
