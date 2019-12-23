#!/usr/bin/env python3
import pandas as pd
import json, sys

def analysis(file, user_id):
    df = pd.read_json(file)
    s = df[df['user_id'] == user_id]['minutes']
    return s.count(), s.sum()

if __name__ == '__main__':
    print(analysis('user_study.json', 131866))

