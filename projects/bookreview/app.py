from flask import Flask, render_template, jsonify, request  #Flask 프레임워크를 사용하면 터미널 로그창에 리로딩되서 서버가 새로 뜸
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    author = request.form['author_give']   #사용에 용이하게 선언
    title = request.form['title_give']     #POST는 request.form['data']
    review = request.form['review_give']

    #몽고db에 data라는 이름의 dictionary 만듦
    data = {
        'author': author,
        'title' : title,
        'review' : review
    }

    #reviews라는 컬렉션에 data라는 dictionary를 넣음
    db.reviews.insert_one(data)

    return jsonify({'result':'success', 'msg': '리뷰가 성공적으로 작성되었습니다'})



@app.route('/reviews', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({},{'_id':0}))   #find 함수로 모든 데이터를 가져옴. '_id':0 은 id라는 컬럼을 제거한다는 뜻
    return jsonify({'result':'success', 'reviews': reviews}) #reviews라는 키로 접근하면 list인 것



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)