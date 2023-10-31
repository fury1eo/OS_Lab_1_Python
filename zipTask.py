import zipfile
import os
import pathlib


# Создать архив и добавить файл
def createArchiveAndInsertFile(archive, file):
    with zipfile.ZipFile(archive, 'w') as z:
        z.write(file)


# Прочитать файл из архива
def readFileFromArchive(archive, file):
    with zipfile.ZipFile(archive, 'r') as z:
        z.extract(file)

        with open(file, 'r') as f:
            print(f.read())


# Удалить архив
def deleteArchive(archive, file):
    filePath = f'{str(pathlib.Path.cwd())}\{file}'
    archivePath = f'{str(pathlib.Path.cwd())}\{archive}'

    if os.path.isfile(filePath):
        os.remove(filePath)
        print(f'Файл {file} удалён')
    else:
        print(f'Файла {file} не существует')

    if os.path.isfile(archivePath):
        os.remove(archivePath)
        print(f'Архив {archive} удалён')
    else:
        print(f'Архива {archive} не существует')


archiveName = f'{input("Введите название архива: ")}.zip'
fileName = input('Введите название файла: ')

createArchiveAndInsertFile(archiveName, fileName)
readFileFromArchive(archiveName, fileName)
deleteArchive(archiveName, fileName)
