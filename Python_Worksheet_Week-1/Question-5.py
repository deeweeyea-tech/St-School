def count_items(items_list):
    item_count = {}

    for item in items_list:
        item_count[item] = item_count.get(item, 0) + 1

    return item_count


print(count_items(['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']))