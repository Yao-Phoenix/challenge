#!/usr/bin/env python3
from simpledu.app import create_app

# ʹ�ÿ�����������
app = create_app('development')

if __name__ == '__main__':
    app.run()