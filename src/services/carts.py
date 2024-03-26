from repository.carts import CartsRepositoriy
from schemas.carts import CartsCreateSchema

from typing import List


class CartsService:
    def __init__(self, carts_repository: CartsRepositoriy,) -> None:
        self.carts_repository = carts_repository

    def get_cart(self, id: int) -> List[CartsCreateSchema]:
        carts = self.carts_repository.get_cart()
        return carts
    
