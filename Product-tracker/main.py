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
