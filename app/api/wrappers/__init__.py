from get import GetManager
from post import PostManager
from update import UpdateManager
# from delete import DeleteManager


class Manager(object):
    def __init__(self):
        self.get = GetManager()
        self.post = PostManager()
        self.update = UpdateManager()
        # self.delete = DeleteManager()


