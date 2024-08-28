# ДЗ:
# 1. Почитать про YAML формат: https://ru.wikipedia.org/wiki/YAML
# 2. Почитать про JSON формат: https://habr.com/ru/articles/554274/
# 3. Создать класс, в классе хранить лист словарей (как у меня в коде пример с
# подключениями - можете придумать что-нибудь своё, например в словарях данные людей будут или ещё что-нибудь)
# 4. Сделать 2 метода для работы с YAML - для сохранения в файл и для чтения из
# файла. Название фала должно передаваться в метод входным параметром.
# 5. Сделать 2 метода для работы с JSON - для сохранения в файл и для чтения
# из файла. Название фала должно передаваться в метод входным параметром.

# 6. В другом поле хранить Pandas DataFrame с данными. Написать ещё 2
# метода - для сохранения данных в файл .csv и для чтения данных из .csv файла в датафрейм.

# Так же написать для 4, 5, 6 пунктов методы, которые будут просто отображать данные, которые внутри объекта хранятся.
# 7. Попробовать при помощи объекта класса прочитать данные из YAML формата, а сохранить - в JSON.
# 8. Наоборот: прочитать данные из JSON, сохранить в YAML.
import yaml
import json
import pandas as pd
class Test_11:
    list=[]
    def __init__(self, dicts: list = [{"username":"user1", "password":"123"}]):
        self.list = dicts
        self.df1 = pd.DataFrame(dicts)
    def save_to_yml(self, fname:str = 'file.yaml'):
        with open(fname, 'w') as file:
            documents = yaml.dump(self.list, file)
    def load_from_yaml(self, fname:str = 'file.yaml'):
        with open(fname) as file:
            con = yaml.load(file, Loader=yaml.FullLoader)
            return con
    def save_to_json(self, fname = 'file.json'):
        json_obj = json.dumps(self.list, indent=4)
        with open(fname, 'w') as file:
            file.write(json_obj)
    def load_from_json(self, fname = 'file.json'):
        with open(fname) as file:
            json_obj = json.load(file)
            return json_obj
    def save_to_csv(self, fname = 'file.csv'):
        self.df1.to_csv(fname)
    def load_from_csv(self, fname = 'file.csv'):
        df2 = pd.read_csv(fname)
        return df2
dt1 = [
    {
        "username":"user1",
        "password":'123'
    },
    {
        'username':'user2',
        'password':'321'
    }
]
test = Test_11(dt1)
# print(test.list)
test.save_to_yml()
# print(test.load_from_yaml())
# test.save_to_json()
# print(test.load_from_json())
# print(test.df1)
# test.save_to_csv()
# print(test.load_from_csv())

# obj_from_y = json.dumps(test.load_from_yaml(), indent=4)
# print(obj_from_y)
# with open('new_file1.json', 'w') as file:
#     file.write(obj_from_y)
obj_from_j = test.load_from_json()
print (obj_from_j)
with open('new_file.yaml', 'w') as file:
    yaml.dump(obj_from_j, file)
