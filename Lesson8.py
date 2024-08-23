# ДЗ:
# 1. Почитать про обработку ошибок:
# https://habr.com/ru/companies/wunderfund/articles/736526/
# если в этой статье слишком непонятно - тут короче и максимально просто: https://metanit.com/python/tutorial/2.11.php
# 2. Посмотреть список самых популярных исключений (хотя бы 1 раз все прочитать):
# https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
# 3. Создать классы: человек, рота, полк. В роте могут содержаться несколько человек, в полку - несколько рот.
# Написать методы:
# - добавления человека в роту, добавления роты в полк.
# - удаления человека из роты или из полка (в этом случае, человек удалиться из роты).
#       Метод на вход должен получать list с несколькими переменными типа Human - как я с автобусом делал.
# - выводить информацию об одном человеке: имя, возраст.
# - выводить информацию об всех людях в роте.
# - выводить информацию об всех людях в полку.
class Human:
    def __init__(self, v_name = 'Ivan', v_age = 18):
        self._name = v_name
        self._age = v_age
    def get_info(self):
        try:
            return self._name + ':' + str(self._age)
        except:
            print("Не могу вывести информацию")
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
    def add_rota(self, rota:list):
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





boy1 = Human()
boy2 = Human('Nikita', 22)
boy3 = Human('Vlad', 23)
boy4 = Human('Alex', 25)
print(boy1.get_info())
rota1 = Rota()
rota2 = Rota()
rota2.add_humans([boy1, boy4])
rota1.add_humans([boy1, boy2, boy3])
print(rota1.get_info())
rota1.kick_humans([boy1])
print(rota1.get_info())
polk1 = Polk()
print(polk1.get_info())
polk1.add_rota([rota1, rota2])
print(polk1.get_info())
print('----------')
polk1.kick_humans([boy4, boy1])
print(polk1.get_info())
print(rota1.get_info(), rota2.get_info())







# 4. Для всех методов из п.3 использовать обработку исключений. Можно не обрабатывать отдельные исключения - достаточно общего через просто Except.
# Добиться, чтобы сработало исключение - и обработалось через except.