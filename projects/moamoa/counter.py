from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

try:
    db.counters.insert_one({
        '_id': 'itemID',
        'seq': 0
    })

except errors.DuplicateKeyError:
    print('이미 초기화가 되었습니다.')