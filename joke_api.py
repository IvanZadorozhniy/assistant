'''Module helps work with pyjokes library'''
import pyjokes


class JokeApi():
    '''Class helps work with pyjokes in property way'''

    def get_joke(self):
        '''Get a random joke'''
        return pyjokes.get_joke()
