# I - Principio da Segregação de Interfaces (ISP)
## "Uma classe não deve ser forçada a implementar interfaces que ela não utiliza"
### Em vez disso, as interfaces devem ser segregadas em conjuntos menores e mais específicos de métodos

# pdf, txt, excel
from abc import ABC, abstractmethod


class Document(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def view(self):
        pass

    @abstractmethod
    def format(self):
        pass

    @abstractmethod
    def calculate(self):
        pass


class DocumentPDF(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def view(self):
        pass


class DocumentTXT(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def format(self):
        pass


class DocumentExcel(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def calculate(self):
        pass
