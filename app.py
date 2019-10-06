from menu import Menu
from models.blog import Blog
from database import Database


Database.initialize()

menu = Menu()

menu.run_menu()
# blog  = Blog(author = "Sasha",
#              title= "simple title",
#              description = "Sample description")
#
# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database = Blog.from_mongo(blog.id)
#
# print(blog.get_posts())
 # post = Post(blog_id= "123",
#             title="some title",
#             content="This is some simple content",
#             author="Sasha")
#
# post.save_to_mongo()
