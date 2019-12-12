#!/usr/bin/env python3
import sys, socket

def scan():
    args = sys.argv[1:]
    try:
        host = args[args.index('--host') + 1]
        port = args[args.index('--port') + 1]
        assert len(host.split('.')) == 4
        if '-' in port:
            start, end = port.split('-')
            assert int(start) < int(end)
            ports = range(int(start), int(end) + 1)
        else:
            ports = [int(port)]
    except (ValueError, IndexError, AssertionError):
        print('Parameter Error')
        exit()

    open_ports = []
    s = socket.socket()
    s.settimeout(0.1)

    for port in ports:
        if s.connect_ex((host, port)) == 0:
            open_ports.append(port)
            print(port, 'open')
        else:
            print(port, 'close')
    s.close
    print('Complted scan. Opening ports at {}'.format(open_ports))

if __name__ == '__main__':
    scan()
