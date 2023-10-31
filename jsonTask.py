import json
import os
import pathlib


# Создать файл
def createFile(file):
    with open(file, 'w') as f:
        json.dump([], f)


# Вставить данные в файл
def insertDataToFile(file, jsonData):
    with open(file, 'w') as f:
        json.dump(jsonData, f)


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


fileName = f'{input("Введите название файла: ")}.json'

data = {
    'name': input("Имя: "),
    'age': input("Возраст: "),
    'country': input("Страна: ")
}

createFile(fileName)
insertDataToFile(fileName, data)
readFile(fileName)
deleteFile(fileName)
