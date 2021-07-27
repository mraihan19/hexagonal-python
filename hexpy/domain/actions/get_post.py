import inject

from hexpy.domain.post import Post
from hexpy.domain.database_interface import DatabaseInterface


class GetPost:
    @inject.autoparams()
    def __init__(self, database: DatabaseInterface):
        self.__database = database

    def execute(self, post_id: int) -> Post:
        return self.__database.get_post(post_id)
