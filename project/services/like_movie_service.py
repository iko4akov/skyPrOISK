from project.dao.base import BaseDAO
from project.models import LikeMovie


class LikeMovieService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao


    def create(self, new_data):
        return self.dao.create(new_data)


    def delete(self, pk):
        return self.dao.delete(pk)

    def get_all(self) -> list[LikeMovie]:
        return self.dao.get_all()
