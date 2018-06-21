#Book_Thief.py


def reader():
    with open('referat.txt', 'r') as file:
        content = file.read()
        print(len(content.replace('\n', ' ').split(' ')))


if __name__ == '__main__':
    reader()
