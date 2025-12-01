from abc import ABC, abstractmethod


class ExameAprovavel(ABC):

    @abstractmethod
    def aprovar(self):
        pass
