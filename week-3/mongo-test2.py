from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

target_movie = db.movies.find_one({'title':'매트릭스'})
target_star = target_movie['star']

#target_star와 같은 평점의 영화 제목의 평점을 0으로 만들기

db.movies.update_many({'star':target_star},{'$set':{'star':0}})




######
#from pymongo import MongoClient
#client = MongoClient('localhost', 27017)
#db = client.dbsparta 

#target_movie = db.movies.find_one({'title':'매트릭스'})
#if target_movie is not None:
    #target_star = target_movie['star']

    #movie = list(db.movies.find({'star':target_star}))

    #for movie in movies:
        #title = movie['title']
        #db.movies.update_one({'title':title}, {'$set':{'star':0}})