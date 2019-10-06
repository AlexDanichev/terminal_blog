from database import Database
import uuid
import datetime


class Post():

    def __init__(self, blog_id,title,content,author,date=datetime.datetime.utcnow(), post_id = None):
        self.title = title
        self.content = content
        self.author = author
        self.blog_id = blog_id
        self.post_id = uuid.uuid4().hex if post_id is None else post_id
        self.created_date = date

    def save_to_mongo(self):
        Database.insert(collection ='posts',
                        data = self.json())

    def json(self):
        return {
            'post_id': self.post_id,
            'blog_id': self.blog_id,
            'title' : self.title,
            'content' : self.content,
            'author' : self.author,
            'date': self.created_date

        }

    @classmethod
    def from_mongo(cls,id):
        post_data= Database.find_one(collection='posts',query={'post_id':id})
        return cls(blog_id=post_data['blog_id'],
                   title= post_data['title'],
                   content= post_data['content'],
                   author=post_data['author'],
                   date = post_data['date'],
                   post_id= post_data['post_id']
                   )

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection="posts", query={"blog_id": id})]