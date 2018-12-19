from pymongo import MongoClient


client = MongoClient('mongodb://root:example@localhost:27017/')
db = client.test_database

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": "19-12-2018"
}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
