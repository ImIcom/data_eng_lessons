# Во всех последующих заданиях используйте только приватные поля, геттеры и сеттеры:
# 2. Создайте несколько классов - например: человек и т.д.

class Human():
    def __init__(self, v_name, v_sex):
        self._name = v_name
        self._sex = v_sex


# 3. От класса человек отнаследуйте класс "ребёнок"

class Child(Human):
    def __init__(self, v_name, v_sex, v_age):
        super().__init__(v_name, v_sex)
        self.__age = v_age
        self.__pozition = 'Home'
    def get_info(self):
        return self._name, self._sex, self.__age, self.__pozition
    def get_name(self):
        return self._name
    def set_pozition(self, v_poz):
        self.__pozition = v_poz

# 4. Создайте класс "автобус". В автобусе должно содержаться несколько "детей" - например в list.
class Bus():
    def __init__(self):
        self.__name = 'Pazik'
        self.__kids = {}
    def get_name(self):
        return self.__name
    def set_name(self, v_name):
        self.__name = v_name
    def set_kids(self, v_name):
        self.__kids[v_name.get_name()] = v_name
    def get_kids(self):
        return self.__kids.keys()
    def del_kids(self, v_name):
        del self.__kids[v_name]
    def change_pozition(self, v_poz):
        for kid in self.__kids.values():
            kid.set_pozition((v_poz))
    def get_info(self):
        return self.__name, list(self.__kids.keys())

edik = Child('Edik', 'm', 8)
dasha = Child('Dasha', 'f', 7)
masha = Child('Masha', 'f', 6)
vlad = Child('Vlad', 'm', 9)
print(edik.get_info())
print(dasha.get_info())
print(masha.get_info())
print(vlad.get_info())
pazik=Bus()
print(pazik.get_info())
pazik.set_kids(edik)
pazik.set_kids(dasha)
pazik.set_kids(masha)
pazik.set_kids(vlad)
print(pazik.get_info())
pazik.change_pozition('School')
print(edik.get_info())
print(dasha.get_info())
print(masha.get_info())
print(vlad.get_info())
pazik.del_kids('Vlad')
print(pazik.get_info())
pazik.change_pozition('Shop')
print(edik.get_info())
print(dasha.get_info())
print(masha.get_info())
print(vlad.get_info())


# Для класса автобус напишите методы добавления ребёнка в автобус, удаления ребёнка из автобуса.
# 5. У каждого ребёнка сделайте хранение его текущего местоположения и методы для его изменения/отображения.
# У автобуса сделайте метод - при вызове которого будет меняться местоположение у всех детей,
#       кто в нём находится на заданное (новое положение передавать в метод изменения положения)
# 5. Проявите смекалку - и создайте ещё несколько классов, которые будут содержать переменные других классов
#       и делать что-нибудь забавное.