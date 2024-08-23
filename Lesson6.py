# 1. Прочитайте про принципы ООП   https://tproger.ru/translations/oop-principles-cheatsheet
# 2. Создайте несколько классов - например: человек и т.д.
# 3. От класса человек отнаследуйте класс "ребёнок"
#

class Human:
    def __init__(self, vname, vage, vsex):
        self.name = vname
        self.age = vage
        self.sex = vsex
    def info(self):
        print(f'name {str(self.name)}, age {int(self.age)}, sex {str(self.sex)}')
masha = Human('Masha', 25, 'f')
masha.info()
# 5. У каждого ребёнка сделайте хранение его текущего местоположения и методы для его изменения/отображения.
class Kid(Human):
    def __init__(self, v_name, v_age, v_sex, v_poz = 'Home'):
        super().__init__(v_name, v_age, v_sex)
        self.pozition = v_poz
    def show_pozition(self):
        return self.pozition
    def change_pozition(self, poz):
        self.pozition = poz

boy = Kid('Atrey', 9, 'm')
boy.info()
girl=Kid('Melisa', 8, 'f')
girl2=Kid('Licua', 10, 'f')
girl3=Kid('Ashley', 7, 'f')
# 4. Создайте класс "автобус". В автобусе должно содержаться несколько "детей" - например в list.
# Для класса автобус напишите методы добавления ребёнка в автобус, удаления ребёнка из автобуса.

# У автобуса сделайте метод - при вызове которого будет меняться
#   местоположение у всех детей, кто в нём находится на заданное
#   (новое положение передавать в метод изменения положения)
class Bus():

    def __init__(self, v_name = 'Pazik',  v_vmestimost = 30):
        self.name = v_name
        self.vmestimost=v_vmestimost
        self.kids = {}
    def add_kid(self, kid):
        self.kids[kid.name] = kid
    def del_kid(self, kid):
        del self.kids[kid]
    def drive_to(self, poz):
        for i in self.kids.values():
            i.change_pozition(poz)
    def info(self):
        print('Автобус {} вмещает {} детей. '
              'Список детей в пазике:'
              ' {}'.format(self.name, self.vmestimost, list(self.kids.keys())))
pazik=Bus()

pazik.info()

pazik.add_kid(boy)
pazik.add_kid(girl)
pazik.add_kid(girl2)
pazik.add_kid(girl3)
pazik.info()
print(f'{boy.name} {boy.show_pozition()}, '
      f'{girl.name} {girl.show_pozition()},'
      f'{girl2.name} {girl2.show_pozition()}, '
      f'{girl3.name} {girl3.show_pozition()}')
pazik.del_kid('Ashley')
pazik.info()
pazik.drive_to('School')
print(f'{boy.name} {boy.show_pozition()}, '
      f'{girl.name} {girl.show_pozition()},'
      f'{girl2.name} {girl2.show_pozition()}, '
      f'{girl3.name} {girl3.show_pozition()}')
pazik.del_kid('Atrey')
pazik.drive_to('Shop')
print(f'{boy.name} {boy.show_pozition()}, '
      f'{girl.name} {girl.show_pozition()},'
      f'{girl2.name} {girl2.show_pozition()}, '
      f'{girl3.name} {girl3.show_pozition()}')


# 5. Проявите смекалку - и создайте ещё несколько классов, которые
 #      будут содержать переменные других классов и делать что-нибудь забавное.