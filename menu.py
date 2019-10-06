from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user = input("Etner you author name:")
        self.user_blog = None

        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs',{'author':self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user,
                    title= title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want read (R) or write (W) blogs?")
        if read_or_write =='R':
            self._list_blogs()
            self._view_blogs()
            pass

        elif read_or_write == 'W' :
            self.user_blog.new_post()

        else:
            print('Thank you for blogging! ')
        #User read or write blogs?
        #if read: list blogs in datbase
        #allow user pick one
        #dislplay posts
        #if write
        #check if user has a blog
        #if they do prompt to wire a post
        #if not prompt to create new blog
        pass

    def _list_blogs(self):
        blogs = Database.find(collection='blogs',
                                  query={})
        for blog in blogs:
            print("ID: {}, Title :{}, Author:{}".format(blog['id'],blog['title'], blog['author']))

    def _view_blogs(self):
        blog_to_see = input("Enter the ID of the blog you like to read: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {} \n\n{}".format(post['date'],post['title'], post['content']))

