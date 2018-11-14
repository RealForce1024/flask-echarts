def split_v1(list):
    length = len(list)
    collection = []
    for i in range(length - 1):
        lst = []
        for j in range(length - 1 - i):
            if list[j] == list[j + 1]:
                lst.append(list[j])
        collection.append(lst)
    return collection


def split_v2(list):
    length = len(list)
    collection = []
    for i in range(length - 1):
        lst = []
        for j in range(length - 1 - i):
            if list[j] == list[j + 1]:
                lst.append(list[j])
            else:
                break
        collection.append(lst)
    return collection


def split_v3(list):
    length = len(list)
    collection = []
    for i in range(length - 1):
        lst = []
        for j in range(length - 1 - i):
            if list[j] == list[j + 1]:
                lst.append(list[j])
            else:
                continue
        collection.append(lst)
    return collection


def split_v4(list):
    length = len(list)
    collection = []
    index = 0
    for i in range(length - 1):
        lst = []
        i = i + index
        for j in range(length - 1 - i):
            if list[j] == list[j + 1]:
                lst.append(list[j])
                index = index + 1
            else:
                break
        collection.append(lst)
    return collection


if __name__ == "__main__":
    a = ['a', 'a', 'a', 'b', 'b', 'a', 'a']
    # print(split_v1(a))
    # print(split_v2(a))
    # print(split_v3(a))
    print(split_v4(a))