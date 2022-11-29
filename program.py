"""
program file

steps to add new category:
    - add name in categories list
    - add file path in fetch_data function
        - individual category
        - all categories
"""
import os
import json
import random

def empty_space(num: int = 1) -> None:
    """prints n newlines

    Args:
        n (int, optional): number of new lines. Defaults to 1.
    """
    for _ in range(num):
        print("\n")

def select_category(category_list: list[str]) -> int:
    """select from given categories

    Args:
        category_list (list[str]): list of categories

    Returns:
        int: index of selected category
    """
    print("select a category")
    print("")
    for i, category in enumerate(category_list):
        print(f"{i}: {category}")
    # all categories
    print("99: all")
    return int(input())

def fetch_data(cat_index: int) -> dict[str, str] | None:
    """fetch data of category with index

    Args:
        cat_index (int): index of category

    Returns:
        dict[str, str] | None: returns dict of data if valid category else None
    """
    # general category
    if cat_index == 0:
        with open("./questions/general.json", encoding="utf-8") as file:
            return json.load(file)
    # add new category here
    # all categories
    elif cat_index == 99:
        all_data: dict[str, str] = {}
        # general
        with open("./questions/general.json", encoding="utf-8") as file:
            all_data.update(json.load(file))
        return all_data
    else:
        print("invalid category")
        return None

def shuffle_data(data_dict: dict[str, str]) -> list[tuple[str, str]]:
    """shuffle received data

    Args:
        data_dict (dict[str, str]): data in form of dictionary

    Returns:
        list[tuple[str, str]]: returns list of tuple of key value pair
    """
    keys: list[str] =  list(data_dict.keys())
    random.shuffle(keys)
    return [(key, data_dict[key]) for key in keys]

# ---------- main namespace ----------

# list of categories
categories: list[str] = ["general"]
# index of selected category
selected_category: int = -1
# question answer data
data: list[tuple[str, str]] = []
# index of current question
index: int = 0

# some empty space
empty_space()
# select category
selected_category = select_category(categories)
# fetch data of category
result = fetch_data(selected_category)
# if data found
if result:
    # clear screen
    os.system('cls')
    # shuffle data
    data = shuffle_data(result)
    # get length of data
    length: int = len(data)

    while index < length:
        # question number
        print(f"{index+1}/{length}")
        # question
        print(data[index][0])
        # quit if 'q'
        q = input()
        if q == 'q':
            break
        # answer
        print(data[index][1])
        # quit if 'q'
        q = input()
        if q == 'q':
            break
        # clear screen
        os.system('cls')
        # next question
        index += 1
