import datetime as dt
class Human:
    name: str
    age: int
    def __init__(self, v_name = 'Ivan'):
        self.name = v_name
        self.birth_date = dt.date(1970,1,1)
        self.age = 18
    def get_info(self):
        return self.name + ':' + str(self.age)

class Rota(Human):
    _rota = []

    def get_info(self):
        try:
            sostav = []
            for man in self._rota:
                sostav.append(man.get_info())
            return sostav
        except:
            print('Не могу вывести состав')

    def add_humans(self, humans: list):
        try:
            self._rota = self._rota + humans
        except:
            print('Невозможно добавить людей в роту')

    def kick_humans(self, humans: list):
        for man in humans:
            # try:
            self._rota.remove(man)
        # except:
        #   print('Не могу убрать {} из роты'.format(man.get_info()))

class Polk(Rota):
    _polk = list()

    def get_info(self):
        try:
            sostav = []
            for man in self._polk:
                sostav.append(man.get_info())
            return sostav
        except:
            print('Не могу вывести состав')

    def add_rota(self, rota: list):
        try:
            self._polk = self._polk + rota
        except:
            print('Не могу добавить роту')

    def del_rota(self, del_rota: list):
        try:
            for rota in del_rota:
                self._polk.remove(rota)
        except:
            print('Не могу удалить роту')

    def kick_humans(self, humans: list):
        for rota in self._polk:
            try:
                rota.kick_humans(humans)
            except:
                None


