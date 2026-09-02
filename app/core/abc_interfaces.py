from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def display_details(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass