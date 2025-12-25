"""
=== PRODUCT TRACKER ===
Мой первый проект на Python.
Трекер товаров с использованием словарей.

История:
1. Сначала не понимал, как добавлять в словарь из input()
2. Пробовал через списки - не работало
3. Понял, что нужно assort_price[key] = value
4. 3 часа дебага - и заработало!

Автор: [Ivan]
Дата: декабрь. 18.2025
"""

# == == == == == == == == == == СТАРЫЕ ПОПЫТКИ(закомментировано) == == == == == == == == == ==


# ------------- Version 0.1 -------------------------

# asort_price = {}
#
# while True:
#     user_input = input("1. Добавить новый товар\n"
#                        "2. Удалить существующий\n"
#                        "3. Изменить существующий\n"
#                        "4. Показать список\n"
#                        "5. Выход")
#     user_price_dict = {}
#     user_price2_dict = {}
#     user_price_list = []
#     user_price2_list = []
#
#     if user_input == "1":
#
#         user_price_list.append(input("one:"))
#         user_price2_list.append(input("tue:"))
#         user_price_dict.update(dict(user_price_lisе))
#
#         print(user_price_dict)
#         # print(user_price2)
#         # user_price.update(user_price2)
#         # if len(user_price) > 0:
#         #
#         #
#         # else:
#         #     print("Ошибка добавления товара")

# -------------------- Version 0.2 ------------------------

# asort_price = {}
#
# while True:
#     user_input = input("1. Добавить новый товар\n"
#                        "2. Удалить существующий\n"
#                        "3. Изменить существующий\n"
#                        "4. Показать список\n"
#                        "5. Выход")
#     user_price_dict = {}
#     user_price2_dict = {}
#     user_price_list = []
#     user_price2_list = []
#
#     if user_input == "1":
#         user_price_list.append(input("one:"))
#         user_price2_list.append(input("tue:"))
#         user_price_dict.update(dict(user_price2_dict))
#
#         print(user_price_dict)
#         # print(user_price2)
#         # user_price.update(user_price2)
#         # if len(user_price) > 0:
#         #
#         #
#         # else:
#         #     print("Ошибка добавления товара")
#

# ----------------- Version 0.3 --------------------

#
# assort_price = {}
#
# while True:
#     user_input = input("1. Добавить новый товар\n"
#                        "2. Удалить существующий\n"
#                        "3. Изменить существующий\n"
#                        "4. Показать список\n"
#                        "5. Выход")
#
#     user_unique_key_save = []
#     user_item_name_save = []
#     user_item_price_save = []
#     user_ves_num_save = []
#     user_kolicestvo_save = []
#
#     if user_input == "1":
#         user_unique_key_save.append(input("Введите уникальный ключ: "))
#         user_item_name_save.append(input("Введите название: "))
#         user_item_price_save.append(input("Введите цену: "))
#         user_ves_num_save.append(input("Введите единицу измерения: "))
#         user_kolicestvo_save.append(input("Введите количество: "))

        # user_unique_key =
        # user_item_name =
        # user_item_price
        # user_ves_num =
        # user_kolicestvo =
        #


    #     print(user_price_dict)
    #     # print(user_price2)
    #     # user_price.update(user_price2)
        # if len(user_price) > 0:
        #
        #
        # else:
        #     print("Ошибка добавления товара")

# ------------------ Version 0.4 --------------------------

#         Более менее вариант но надо дописать


# assort_price = {}
# change_assort_dict = {}
#
#
# while True:
#     user_input = input("1. Добавить новый товар\n"
#                        "2. Удалить существующий\n"
#                        "3. Изменить существующий\n"
#                        "4. Показать список\n"
#                        "5. Выход\n"
#                        "\n"
#                        "Выберите действие: ")
#
# #     добавляться вроде должно так принять c input

#     # g = input(Введите уникал ключ)
#     # дальше сами значение для добавления в словарь добавлять над вот так вроде
#     # user_dict = {g: и сами значения с input  по веременным типо name, ear, }
#        #
#     if user_input == "1":
#         input_unique_key = input("Введите уникальный ключ: ").strip().lower()
#
#         item_name = input("Введите название: ").strip().lower()
#         items_price = input("Введите цену: ").strip().lower()
#         item_weight = input("Введите единицу измерения: ").strip().lower()
#         quantity_items = input("Введите количество: ").strip().lower()
#
#
#         assort_price[input_unique_key]= {item_name: (items_price, item_weight, quantity_items)}
#         print("Товар добавлен")
#         print()
#
#     elif user_input == "2":
#         user_input_delite = input("Введите название ключа для удаления: ").strip().lower()
#         print()
#
#         if user_input_delite in assort_price:
#             assort_price.pop(user_input_delite)
#             print("Товар удален!")
#
#         else:
#             print("Ошибка удаления!\n\nТакого товара нет в списке.")
#
#     elif user_input == "3":
#         user_change_input_key = input("Введите уникальный ключ: ")
#
#         if user_change_input_key in assort_price:
#
#             item_name_change = input("Введите название: ").strip().lower()
#             items_price_change = input("Введите цену: ").strip().lower()
#             item_weight_change = input("Введите единицу измерения: ").strip().lower()
#             quantity_items_change = input("Введите количество: ").strip().lower()
#
#
#             change_assort_dict[user_change_input_key] = {item_name_change:
#                                                         (items_price_change,
#                                                         item_weight_change,
#                                                         quantity_items_change)}
#
#             assort_price.update(change_assort_dict)
#
#             print("Товар изменен в словаре")
#
#         else:
#             print("Ошибка изменения!\nТакого ключа нет.")
#
#     elif user_input == "4":
#
#         for key, item in assort_price.items():
#
#             print(f"{key} - {item[]} (${item} x {item} {item}.)")
#
#
#     elif user_input == "5":
#         print("\nПрограмма завершена!")
#         break
#
#     print(assort_price)
#     print(change_assort_dict)

# выводить нужен так вроде

        # print(f"{assort_price.get()}"
        #       f" - {assort_price.values()}"
        #       f" (${assort_price.values()})"
        #       f"x {assort_price.values()} "
        #       f"{assort_price.values()}")

        # print(f"{assort_price.get(input_unique_key)}"
        #       f" - {assort_price.get(item_name)}"
        #       f" (${assort_price.get(items_price)})"
        #       f"x {assort_price.get(quantity_items)} "
        #       f"{assort_price.get(item_weight)}")

# ________________________________________________________________
#        Чистый код без коментов на данный момент не дописан

# assort_price = {}
# change_assort_dict = {}


# while True:
#     user_input = input("1. Добавить новый товар\n"
#                        "2. Удалить существующий\n"
#                        "3. Изменить существующий\n"
#                        "4. Показать список\n"
#                        "5. Выход\n"
#                        "\n"
#                        "Выберите действие: ")
#
#
#     if user_input == "1":
#         input_unique_key = input("Введите уникальный ключ: ").strip().lower()
#
#         item_name = input("Введите название: ").strip().lower()
#         items_price = input("Введите цену: ").strip().lower()
#         item_weight = input("Введите единицу измерения: ").strip().lower()
#         quantity_items = input("Введите количество: ").strip().lower()
#
#         assort_price[input_unique_key]= {item_name: (items_price, item_weight, quantity_items)}
#         print("Товар добавлен")
#         print()
#
#     elif user_input == "2":
#         user_input_delite = input("Введите название ключа для удаления: ").strip().lower()
#         print()
#
#         if user_input_delite in assort_price:
#             assort_price.pop(user_input_delite)
#             print("Товар удален!")
#
#         else:
#             print("Ошибка удаления!\n\nТакого товара нет в списке.")
#
#     elif user_input == "3":
#         user_change_input_key = input("Введите уникальный ключ: ")
#
#         if user_change_input_key in assort_price:
#
#             item_name_change = input("Введите название: ").strip().lower()
#             items_price_change = input("Введите цену: ").strip().lower()
#             item_weight_change = input("Введите единицу измерения: ").strip().lower()
#             quantity_items_change = input("Введите количество: ").strip().lower()
#
#             change_assort_dict[user_change_input_key] = {item_name_change:
#                                                         (items_price_change,
#                                                         item_weight_change,
#                                                         quantity_items_change)}
#
#             assort_price.update(change_assort_dict)
#
#             print("Товар изменен в словаре")
#
#         else:
#             print("Ошибка изменения!\nТакого ключа нет.")
#
#     elif user_input == "4":
#
#         for key, item in assort_price.items():
#
#             print(f"{key} - {item[]} (${item} x {item} {item}.)")
#
#
#     elif user_input == "5":
#         print("\nПрограмма завершена!")
#         break



# ---------------- Version 0.5 ----------------------

# 
# 
# assort_price = {}
# change_assort_dict = {}
# 
# 
# while True:
#     user_input = input("1. Добавить новый товар\n"
#                        "2. Удалить существующий\n"
#                        "3. Изменить существующий\n"
#                        "4. Показать список\n"
#                        "5. Выход\n"
#                        "\n"
#                        "Выберите действие: ")
# 
# 
#     if user_input == "1":
#         input_unique_key = input("Введите уникальный ключ: ").strip().lower()
# 
#         item_name = input("Введите название: ").strip().lower()
#         items_price = input("Введите цену: ").strip().lower()
#         item_weight = input("Введите единицу измерения: ").strip().lower()
#         quantity_items = input("Введите количество: ").strip().lower()
# 
#         assort_price[input_unique_key] = {item_name: [items_price, item_weight, quantity_items]}
# 
#         # тоже не то если было бы так то надо добавлять отдельно ключ принимать и значения валуе для соединения
#         # assort_price[input_unique_key] = {item_name}
#         # assort_price[items_price] = {items_price}
#         # assort_price[item_weight] = {item_weight}
#         # assort_price[quantity_items] = [quantity_items]
# 
#         print("Товар добавлен")
#         print()
# 
#     elif user_input == "2":
#         user_input_delite = input("Введите название ключа для удаления: ").strip().lower()
#         print()
# 
#         if user_input_delite in assort_price:
#             assort_price.pop(user_input_delite)
#             print("Товар удален!")
# 
#         else:
#             print("Ошибка удаления!\n\nТакого товара нет в списке.")
# 
#     elif user_input == "3":
#         user_change_input_key = input("Введите уникальный ключ: ")
# 
#         if user_change_input_key in assort_price:
# 
#             item_name_change = input("Введите название: ").strip().lower()
#             items_price_change = input("Введите цену: ").strip().lower()
#             item_weight_change = input("Введите единицу измерения: ").strip().lower()
#             quantity_items_change = input("Введите количество: ").strip().lower()
# 
#             change_assort_dict[user_change_input_key] = {item_name_change:
#                                                         (items_price_change,
#                                                         item_weight_change,
#                                                         quantity_items_change)}
# 
#             assort_price.update(change_assort_dict)
# 
#             print("Товар изменен в словаре")
# 
#         else:
#             print("Ошибка изменения!\nТакого ключа нет.")
# 
#     elif user_input == "4":
# 
#         for key, inner_dict in assort_price.items():
#             #  получаем с внутреннего словаря ключ через  метод словарей keys() и получаем values  с методом славарей
#             # values()  переводим все в лист для вывода по индексам values
#             item_name_key = list(inner_dict.keys())[0]
#             item_name_value = list(inner_dict.values())[0]
# 
#             print(f"{key} - {item_name_key} (${item_name_value[0]}) x {item_name_value[2]} {item_name_value[1]}.")
#             print("-" * 50)
# 
# 
#             # print(key, value)
#             # print(f"{key} - {item[]} (${item} x {item} {item}.)")
#             # print(f"{assort_price[key]} - {assort_price[value[0]]} $ "
#                   # f"{assort_price[value[1]]} x {assort_price[value[4]]} {assort_price[value[3]]}.)")
#             # print(f"{assort_price[key]} - {assort_price[key[0]]} $ {assort_price[value[0]]} x {assort_price[value[2]]} {assort_price[value[1]]}.)")
# 
#             # хм вроде нашел выход надо брать саму в цикле кей[вывести ключ] дальше кен
#             # print(f"{assort_price[value[0]]} -.)")
#             # print(f"{key} - {assort_price[value]["item_name"]}")
# 
#             # а если вывести key[key[0]так как это словарь в словаре]
#             # print(key, value)
#         # print(assort_price[0][1])
#         # все не то(
# 
#         # print(assort_price)
#     elif user_input == "5":
#         print("\nПрограмма завершена!")
#         break
# 
# 
# 
# # {'tea2': {'tea': ('10', 'ml', '2')}}
# 
# # так ключ tea2  он сам key отельный если его выбрать то дает значения {'tea': ('10', 'ml', '2')}
# # надо вытащить как то из key



# ---------------------------------------------------------
# чистый код рабочий вариант кода не законченная версия так как нет обработок ошибок еще 




assort_price = {}
change_assort_dict = {}


while True:
    user_input = input("1. Добавить новый товар\n"
                       "2. Удалить существующий\n"
                       "3. Изменить существующий\n"
                       "4. Показать список\n"
                       "5. Выход\n"
                       "\n"
                       "Выберите действие: ")


    if user_input == "1":
        input_unique_key = input("Введите уникальный ключ: ").strip().lower()

        item_name = input("Введите название: ").strip().lower()
        items_price = input("Введите цену: ").strip().lower()
        item_weight = input("Введите единицу измерения: ").strip().lower()
        quantity_items = input("Введите количество: ").strip().lower()

        assort_price[input_unique_key] = {item_name: [items_price, item_weight, quantity_items]}

        print("Товар добавлен")
        print()

    elif user_input == "2":
        user_input_delite = input("Введите название ключа для удаления: ").strip().lower()
        print()

        if user_input_delite in assort_price:
            assort_price.pop(user_input_delite)
            print("Товар удален!")

        else:
            print("Ошибка удаления!\n\nТакого товара нет в списке.")

    elif user_input == "3":
        user_change_input_key = input("Введите уникальный ключ: ")

        if user_change_input_key in assort_price:

            item_name_change = input("Введите название: ").strip().lower()
            items_price_change = input("Введите цену: ").strip().lower()
            item_weight_change = input("Введите единицу измерения: ").strip().lower()
            quantity_items_change = input("Введите количество: ").strip().lower()

            change_assort_dict[user_change_input_key] = {item_name_change:
                                                        (items_price_change,
                                                        item_weight_change,
                                                        quantity_items_change)}

            assort_price.update(change_assort_dict)

            print("Товар изменен в словаре")

        else:
            print("Ошибка изменения!\nТакого ключа нет.")

    elif user_input == "4":

        for key, inner_dict in assort_price.items():

            item_name_key = list(inner_dict.keys())[0]
            item_name_value = list(inner_dict.values())[0]

            print(f"{key} - {item_name_key} (${item_name_value[0]}) x {item_name_value[2]} {item_name_value[1]}.")
            print("-" * 50)

    elif user_input == "5":
        print("\nПрограмма завершена!")
        break

# ----------------------------------------------------------------
# в программе решил сложным вариантом иза вложенного dict сам того не зная надо упростить
# assort_price = {"key": item_key,
#                 "name": item_name,
#                 "price": item_price,
#                 "weight": item_weight,
#                 "quantity": item_quantity}

# так не пойдет надо другим способом

# это вроде похоже на рабочий вариант

# ошибка была моя в сложном варианте иза добавления вложенным словарем типо
# так не правильно добавил assort_price[unique_key] = {item_name: [item_price, item_weight, item_quantity]}
# хотя я правильно сделал проект работает но коряво  и усложнено но там и плюс есть могу добавлять сразу в пустой словарь
# без создания самих нужных структур требований в словаре типо вот так это пример
#                   {"key": item_key,
# #                 "name": item_name,
# #                 "price": item_price,
# #                 "weight": item_weight,
# #                 "quantity": item_quantity}
# ------------------------------------------------------------
#         правильный и упрощенный  вариант добавления
assort_price = {}

while True:

    item_unique_key = input("Введите уникальный ключ: ")
    item_name = input("Введите название: ")
    item_price = input("Введите цену: ")
    item_weight = input("Введите единицу измерения :")
    item_quantity = input("Введите количество: ")

    assort_price[item_unique_key] = {"name": item_name,
                                     "price": item_price,
                                     "weight": item_weight,
                                     "quantity": item_quantity}

    print(assort_price[item_unique_key]["price"])
# ----------------------------------------------------------------

# вариант как думал нужно добавлять

# assort_price = {"key": item_key,
#                 "name": item_name,
#                 "price": item_price,
#                 "weight": item_weight,
#                 "quantity": item_quantity}
#
#
#
# item_key = input("Введите уникальный ключ: ")
# item_name = input("Введите название: ")
# item_price = input("Введите цену: ")
# item_weight = input("Введите единицу измерения :")
# item_quantity = input("Введите количество: ")
#
# assort_price[item_key] = {item_name, item_price, item_weight, item_quantity}
#
# print(assort_price)



# ------------------------------- Version 0.6 ---------------------------------------

assort_price = {}


while True:

    print("-" * 40)

    user_input_actions = input("1. Добавить новый товар\n"
                               "2. Удалить существующий\n"
                               "3. Изменить существующий\n"
                               "4. Показать список\n"
                               "5. Выход\n"
                               "\n"
                               "Выберите действие: ").strip().lower()
    if user_input_actions != "":

        if user_input_actions == "1":

            assort_unique_key = input("Введите уникальный ключ: ").strip().lower()

            item_name = input("Введите название: ").strip().lower()
            item_price = input("Введите цену: ").strip().lower()
            item_weight = input("Введите единицу измерения: ").strip().lower()
            item_quantity = input("Введите количество: ").strip().lower()

            assort_price[assort_unique_key] = {"name": item_name,
                                               "price": item_price,
                                               "weight": item_weight,
                                               "quantity": item_quantity}

            print("Товар добавлен в словарь!")

        elif user_input_actions == "2":

            item_key_remove = input("Введите уникальный ключ для удаления товара: ").strip().lower()

            if item_key_remove in assort_price:
                assort_price.pop(item_key_remove)
                print("Товар удален!")

            else:
                print("Ошибка удаления!\n\nТакого ключа нет!")

        elif user_input_actions == "3":
            user_change_input_key = input("Введите ключ для замены: ")

            if user_change_input_key == "":
                print("Вы ничего не ввели для замены!\n\nВведите данные!")

            else:

                if user_change_input_key in assort_price:

                    item_name_change = input("Введите новое имя товара: ")
                    item_price_change = input("Введите новую цену для замены: ")
                    item_weight_change = input("Введите новую единицу измерения: ")
                    item_quantity_change = input("Введите новое количество: ")

                    assort_price[user_change_input_key] = {"name": item_name_change,
                                                           "price": item_price_change,
                                                           "weight": item_weight_change,
                                                           "quantity": item_quantity_change}

                    print("Данные изменены!")

                else:

                    print("Ошибка изменения\n\nТакого ключа нет!")

        elif user_input_actions == "4":

            for key, value in assort_price.items():

                print(f"{key} - {value['name']} (${value['price']}) x {value['quantity']} {value['weight']}.")

        elif user_input_actions == "5":

            print("программа завершена!")
            break

    else:
        print("Ошибка!\nПустой ввод данных!")

