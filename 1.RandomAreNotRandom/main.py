from random import uniform

def get_random_number(n: int):
    for i in range(n):
        yield uniform(0, n)

if __name__ == '__main__':
    print(list(get_random_number(3)))