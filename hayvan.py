# parent class: hayvan
#    child class 1: kopek
#    child class 2: kus
#       child child class 1: karga

from canli import hayvan

class kopek(hayvan):
    def __init__(self, yas):
        super().__init__("kopek", yas, False)

class kus(hayvan):
    def __init__(self, cins, yas, ucabiliyormu):
        super().__init__(cins, yas, True)

class karga(kus):
    def __init__(self, cins, yas):
        super().__init__(cins, yas, True)
