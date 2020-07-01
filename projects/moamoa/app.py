from pymongo import MongoClient, ReturnDocument

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup


@app.route('/')
def home():
    return render_template('index.html')

##아이템
@app.route('/item', methods=['GET'])
def listing():
    result = list(db.items.find({}))
    return jsonify({'result':'success', 'items':result})

@app.route('/item', methods=['POST'])
def saving():

    url_receive = request.form['url_give']
    price_receive = request.form['price_give']

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')

    url_image = og_image['content']
    url_title = og_title['content']

    item = {'_id': getNextSequence('itemID'), 'url': url_receive, 'price': price_receive, 'image': url_image,
               'title': url_title, 'included': False}

    db.items.insert_one(item)

    return jsonify({'result': 'success'})

##아이템 삭제
@app.route('/item/delete', methods=['POST'])
def deleteItem():
    id_receive = int(request.form['id_give'])
    db.items.delete_one({'_id':id_receive})
    return jsonify({'result': 'success'})


##counter.py
def getNextSequence (idStr) :
    sequenceDocument = db.counters.find_one_and_update (
        {'_id' : idStr},
        {'$inc' : {'seq' : 1}},
        return_document=ReturnDocument.AFTER
    )
    return int(sequenceDocument['seq'])

##컬렉션
@app.route('/collection', methods=['POST'])
def putItem():
    included_receive = request.form['included_give']

    db.items.update_many({included_receive:False},{'$set':{included_receive:True}})



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)