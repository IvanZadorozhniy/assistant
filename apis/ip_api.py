"""Module for IP finding"""
import logging
import re
import socket
from urllib.error import URLError
from urllib.request import urlopen

import utils

IP_URL_API = 'http://checkip.dyndns.com/'


class IpApi():
    "IpApi class works to get to know about ip"

    def __init__(self):
        host_name = socket.gethostname()
        self._local_ip = socket.gethostbyname(host_name)
        try:
            html = str(urlopen(IP_URL_API).read())
            pattern = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)')
            self._global_ip = pattern.search(html).group(1)
        except URLError as err:
            logging.debug(err)
            self._global_ip = "unknown"

    @property
    def local_ip(self):
        '''getter local ip'''
        return self._local_ip

    @property
    def global_ip(self):
        '''getter global ip'''
        return self._global_ip

    @local_ip.setter
    def local_ip(self, ip_address):
        '''setter local ip'''
        self._local_ip = ip_address

    @global_ip.setter
    def global_ip(self, ip_address):
        '''setter global ip'''
        self._local_ip = ip_address

    def get_info_about_ip(self):
        '''string representation about ips'''
        answer = f"""
        Your local IP is {self.__ip_as_string(self.local_ip)}. 
        Global IP is {self.__ip_as_string(self.global_ip)}
        """
        return answer
    def __str__(self):
        return f"Local: {self.local_ip}<<-->>Global: {self.global_ip}"
    @staticmethod
    def __ip_as_string(ip_address):
        numbers = ip_address.split(".")

        answer = " point. ".join([utils.number_to_words(number)
                                  for number in numbers]).strip()
        return answer


if __name__ == "__main__":
    ip = IpApi()
    a = ip.get_info_about_ip()
    print(a)
