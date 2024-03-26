from repository.group import GroupRepositoriy
from schemas.employee import *

from typing import List


class GroupService:
    
    def __init__(self, group_repository: GroupRepositoriy,) -> None:
        self.group_repository = group_repository

    def add_new_group(self, group: GroupCreateSchema) -> str:
        ret = self.group_repository.add_new_group(group)
        return ret
        