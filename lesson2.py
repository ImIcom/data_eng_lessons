

    # ДЗ:
    # 1. Создать несколько листов. Сложить их.
    # В новый словарь выбрать только уникальные значения (можете в видосе посмотреть, как это делать)

    # 2. Создать несколько словарей. Словари с базовыми типами, словари с листами, словари со словарями.
    # 3. Подоставать значения из словарей через .get()

    # 4. Положить один словарь в другой. Потом достать значения из вложеного словаря.

    # 5. Сделать лист с ключами словаря. Сделать лист со значениями словаря.

    # 6. В уже созданном словаре изменить значение элемента (перезаписать другим значением)

    # 7. Всё вышеперечисленное повторить несколько раз.

# list1=[1,2,3,4,5,6,7,8]
# list2=[4,5,6,7,8,9,10,11,100]
# list3=list1+list2
# print(list3)
# list4=list(set(list3))
# print(list4)
#
# dt1=dict()
#
# dt1[1]='first'
# dt1[2]='second'
# print(dt1)
#
# print(dt1.get(1))
# print('')
# dt2={
#     'vasya':25,
#     'sanya':30,
#     'ladik':40
# }
# print(dt2)
# print(dt2.get('vasya'))
# print('')
# dt3={
#     1:list4,
#     2:list3
# }
# print(dt3)
# print(dt3.keys())
# print(dt3.values())
# print(dt3.items())
#
#
# dt4={
#     'fd':dt1,
#     'sd':dt2,
#     'td':dt3
# }
# print(dt4)
# print(dt4.get('fd').get(1))
# print(dt4.get('sd').get('sanya'))
# list5=dt4.keys()
# print(list5)
# list6=dt4.values()
# print(list6)
#
# dt4['fd']='test'
# print(dt4)
list1=list()
list2=[3,4,5]
print(list1+list2*2)
list3=list2*3
print(list3)
dt1= {1: list(set(list3))}
print(dt1)
print(type(dt1))
dt1[2]=list2
dt1[3]='Dog'
dt1[4]='Russia'
print(dt1)
print(dt1.get(4))
dt2={'vasy':25,
    'petya':30,
    'test':dt1
}
print(dt2)
print(dt2.get('test').get(4))
list6=dt2.keys()
list7=dt2.values()
print(list6)
print(list7)
dt2['petya']='Pupkin'
print(dt2)