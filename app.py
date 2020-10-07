from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from api_constants import password, db_name

app = Flask(__name__)

db_uri = "mongodb+srv://kathir:{}@scrappeddata.8uo7e.mongodb.net/{}?retryWrites=true&w=majority".format(password,
                                                                                                        db_name)
app.config['MONGO_DBNAME'] = db_name
app.config['MONGO_URI'] = db_uri

mongo = PyMongo(app)


# class Questions(db.Document):
#     doc_id = db.StringField()
#     question = db.StringField()
#     views = db.StringField()
#     vote_count = db.IntField()
#     post_tag = db.StringField()
#     asked_by = db.StringField()
#     avatar = db.StringField()
#
#     def to_json(self):
#         return {
#             "doc_id": self.doc_id,
#             "question": self.question,
#             "views": self.views,
#             "vote_count": self.vote_count,
#             "post_tag": self.post_tag,
#             "asked_by": self.asked_by,
#             "avatar": self.avatar
#         }


@app.route('/api/test', methods=["GET"])
def test():
    return jsonify("kathir", 200)


@app.route('/api/questions', methods=["GET"])
def get_questions():
    questions = mongo.db.posts
    results = []
    for i in questions.find():
        results.append({
            "doc_id": i["doc_id"],
            "question": i["question"],
            "views": i["views"],
            "vote_count": i["vote_count"],
            "post_tag": i["post_tag"],
            "asked_by": i["asked_by"],
            "avatar": i["avatar"],
        })
    return jsonify({'result': results})


if __name__ == '__main__':
    app.run()
