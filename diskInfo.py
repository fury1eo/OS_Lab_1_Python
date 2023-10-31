import string
from ctypes import windll
from ctypes import wintypes as w
import ctypes


# Костыль для получения дисков. Сколько не искал, видимо это best practice
def getDrives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(f'{letter}:\\')
        bitmask >>= 1
    return drives


# Получение информации о диске
def getInfo(drives):
    dll = ctypes.WinDLL('kernel32', use_last_error=True)
    dll.GetVolumeInformationW.argtypes = w.LPCWSTR, w.LPWSTR, w.DWORD, w.LPDWORD, w.LPDWORD, w.LPDWORD, w.LPWSTR, w.DWORD
    dll.GetVolumeInformationW.restype = w.BOOL

    volumeName = ctypes.create_unicode_buffer(w.MAX_PATH + 1)
    fileSystemName = ctypes.create_unicode_buffer(w.MAX_PATH + 1)

    serialNumber = w.DWORD()
    maxComponentLength = w.DWORD()
    fileSystemFlags = w.DWORD()

    dll.GetDiskFreeSpaceExW.argtypes = (ctypes.c_wchar_p,) + (ctypes.POINTER(ctypes.c_ulonglong),) * 3

    result = []

    for drive in drives:
        _ = ctypes.c_ulonglong()
        total = ctypes.c_ulonglong()
        free = ctypes.c_ulonglong()

        dll.GetDiskFreeSpaceExW(
            drive,
            ctypes.byref(_),
            ctypes.byref(total),
            ctypes.byref(free)
        )

        dll.GetVolumeInformationW(
            drive,
            volumeName,
            ctypes.sizeof(volumeName),
            ctypes.byref(serialNumber),
            ctypes.byref(maxComponentLength),
            ctypes.byref(fileSystemFlags),
            fileSystemName,
            ctypes.sizeof(fileSystemName)
        )

        # Текстовая информация
        result.append(
            f'Диск {drive}\n'
            f'\tМетка тома - {volumeName.value}\n'
            f'\tТип файловой системы - {fileSystemName.value}\n'
            f'\tРазмер - {maxComponentLength.value}\n'
            f'\tСвободное пространство - {free.value}\n'
        )
    return result


# Вывод информации
for driveInfo in getInfo(getDrives()):
    print(driveInfo)
