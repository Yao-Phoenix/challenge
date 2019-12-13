#!/usr/bin/env python3
import sys
from pymongo import MongoClient

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests 
    data= {}
    for item in contests.find():
        if data.get(item['user_id']):
            data[item['user_id']][0] += item['score']
            data[item['user_id']][1] += item['submit_time']
        else:
            data[item['user_id']] = [item['score'], item['submit_time']]
    rank_list = sorted(data.values(), key = lambda x: (-x[0],x[1]))
    for i, j in enumerate(rank_list):
        data[[k for k, v in data.items() if v==j][0]].insert(0, i+1)
    return tuple(data[user_id])

if __name__ == '__main__':
    try:
        user_id = int(sys.argv[1])
        print(get_rank(user_id))
    except:
        print("NOTFOUND")
        exit()


