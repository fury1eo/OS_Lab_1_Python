import xml.etree.ElementTree as ET
import os
import pathlib


# Создать файл
def createFile(file):
    root = ET.Element('root')
    tree = ET.ElementTree(root)
    tree.write(file)


# Вставить данные в файл
def insertDataToFile(file, xmlData):
    root = ET.Element('root')
    tree = ET.ElementTree(root)

    data = ET.SubElement(root, 'data')
    data.text = xmlData
    tree.write(file)


# Прочитать файл
def readFile(file):
    tree = ET.parse(file)
    root = tree.getroot()

    for data in root:
        print(data.tag, data.text)


# Удалить файл
def deleteFile(file):
    path = f'{pathlib.Path.cwd()}\{file}'
    if os.path.isfile(path):
        os.remove(path)
        print(f'Файл {file} удалён')
    else:
        print(f'Файла {file} не существует')


fileName = f'{input("Введите название файла: ")}.xml'
data = input('Введите данные: ')

createFile(fileName)
insertDataToFile(fileName, data)
readFile(fileName)
deleteFile(fileName)
