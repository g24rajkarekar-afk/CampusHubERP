from datetime import datetime
from abc import ABCMeta


class ModelMeta(ABCMeta):

    def __new__(cls, name, bases, namespace):
        namespace["created_at"] = None
        namespace["updated_at"] = None

        return super().__new__(cls, name, bases, namespace)