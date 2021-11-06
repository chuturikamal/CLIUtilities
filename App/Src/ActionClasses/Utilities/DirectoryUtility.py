import os
import logging
import shutil
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def FetchDirectoryFiles(path = ''):
    if path != '':
        return os.listdir(path)
    else:
        return os.listdir()

def Parentpath(path = ''):
    if path != '':
        path = Path(path)
        return path.parent.absolute()
    else:
        path = Path(os.getcwd())
        return path.parent.absolute()

def GetFolderName(path):
    if path == '':
        return os.path.basename(os.getcwd())
    else:
        return os.path.basename(path)

def getPath():
    return os.getcwd()

def LogMessage(message):
    logging.info(message)

def extSplit(file):
    return os.path.splitext(file)

def fileMove(src, dest):
    LogMessage(f'moved to [{dest}]')
    shutil.move(src, dest)

def CheckIfDir(path):
    return os.path.isdir(path)