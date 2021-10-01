from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({'title':'월-E'})
target_star = target_movie['star'] #9.41
same_movie = list(db.movies.find({'star': target_star})) #이미 여기서 if

db.movies.update_many({'star':target_star}, {'$set' : {'star' :'0'}})


for i in same_movie:
    print(i['title'])
