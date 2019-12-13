#!/usr/bin/env python3
import sys
from pymongo import MongoClient

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests 
    scores = 0
    submit_times = 0
    for item in contests.find():
        data = {item['user_id']: [item['score'], item['submit_time']]}
        scores += data[item['user_id']][0]
        submit_times += data[item['user_id']][1]
        rank_list = sorted(data.values(), key = lambda x: (x[0],x[1]))
    for i, j in enumerate(rank_list):
        rank = i
        score = data[[k for k, v in data.items() if v==j]][0]
        submit_time = data[[k for k, v in data.items() if v==j]][1]
    return rank, score, submit_time

if __name__ == '__main__':
    try:
        user_id = int(sys.argv[1])
    except:
        print('Parameter Error')
        exit()

    print(get_rank(user_id))


