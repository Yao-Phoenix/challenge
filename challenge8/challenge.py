#!/usr/bin/env python3
import re 
from collections import Counter
from datetime import datetime


def open_parser(filename):
    with open(filename) as logfile:
        pattern = (r''
                r'(\d+.\d+.\d+.\d+)\s-\s-\s'
                r'\[(.+)\]\s'
                r'"GET\s(.+)\s\w+/.+"\s'
                r'(\d+)\s'
                r'(\d+)\s'
                r'"(.+)"\s'
                r'"(.+)"'
                )
        parsers = re.findall(pattern, logfile.read())
    return parsers

def main():
    logs = open_parser('nginx.log')

    ip_list = []
    _404_list = []

    for log in logs:
        dt = datetime.strptime(log[1][:-6], '%d/%b/%Y:%H:%M:%S')
        if int(dt.strftime("%d")) == 11:
            ip_list.append(log[0])

        if int(log[3]) == 404:
            _404_list.append(log[2])

    ip_counts = Counter(ip_list)
    _404_counts = Counter(_404_list)

    sorted_ip = sorted(ip_counts.items(), key = lambda x: x[1])
    sorted_404 = sorted(_404_counts.items(), key = lambda x: x[1])
    ip_dict = dict([sorted_ip[-1]])
    url_dict = dict([sorted_404[-1]])

    return ip_dict, url_dict

if __name__ == '__main__':
    print(main())
