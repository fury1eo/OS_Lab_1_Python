import os
import pathlib


# Создать файл
def createFile(file):
    f = open(file, 'w')
    f.close()


# Вставить строку в файл
def insertStringToFile(file):
    with open(file, 'w') as f:
        f.write(input('Введите текст: '))


# Прочитать файл
def readFile(file):
    with open(file, 'r') as f:
        print(f.read())


# Удалить файл
def deleteFile(file):
    path = f'{pathlib.Path.cwd()}\{file}'
    if os.path.isfile(path):
        os.remove(path)
        print(f'Файл {file} удалён')
    else:
        print(f'Файла {file} не существует')


fileName = f'{input("Введите название файла: ")}.txt'
createFile(fileName)
insertStringToFile(fileName)
readFile(fileName)
deleteFile(fileName)
