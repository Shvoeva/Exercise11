from itertools import chain

def get_string_pooling(list1: list, list2: list):
    return chain(list1, list2)

if __name__ == '__main__':
    assert list(get_string_pooling([1, 2], [3, 4])) == [1, 2, 3, 4]