from logging import exception
from .ServiceInterface import ServiceInterface
from ..Utilities.DirectoryUtility import FetchDirectoryFiles, getPath, Parentpath, GetFolderName, CheckIfDir

class DirectoryTreeService(ServiceInterface):
    def __init__(self, arg):
        self.direction = arg
        self.dirList = []

    def Start(self):
        if self.direction == 'upper':
            self.UpperTree()
        elif self.direction == 'lower':
            self.LowerTree()

    def LowerTree(self):
        print('Initiating the Lower Directory tree ')
        path = getPath()
        print(path)
        self.ChildTreeDisplay(path)

    def ChildTreeDisplay(self, path, i = 0):
        try:
            dirFiles = FetchDirectoryFiles(path)
            if len(dirFiles) > 0:
                folderName = GetFolderName(path)
                
                iVal = 0
                msg = ''
                while iVal < i * 5:
                    msg += ' '
                    iVal += 1
                msg += f'|{folderName}'
                print(msg)

                for file in dirFiles:
                    filePath = path + '/' + file
                    if CheckIfDir(filePath):
                        self.ChildTreeDisplay(filePath, i + 1)
        except PermissionError:
            print('exception raised')

       
    def UpperTree(self):
        print('Initiating the Upper Directory tree ')
        parentPath = ''
        prevChildpath = ''

        while not ((parentPath != '' and prevChildpath != '') and parentPath == prevChildpath):
            dir = FetchDirectoryFiles(parentPath)
            dirName = GetFolderName(parentPath)
            self.dirList.append({'name': dirName, 'dirFiles': dir})
            prevChildpath = parentPath
            parentPath = Parentpath(parentPath)
        self.ParentTreeDisplay(self.dirList[::-1])

    def ParentTreeDisplay(self, currList, i = 0):
        dats = currList if i == 0 else currList['dirFiles']
        for data in dats:
            dirName = data['name'] if i == 0 else data
            if not dirName.startswith('.') and dirName != '':
                iVal = 0
                msg = ''
                while iVal < i * 5:
                    msg += ' '
                    iVal += 1
                msg += f'|{dirName}'
                print(msg)
                
                dirfiles = filter(lambda x: x['name'] == dirName, self.dirList)
                dirfiles = list(dirfiles)
                self.dirList = filter(lambda x: x['name'] != dirName, self.dirList)
                self.dirList = list(self.dirList)
                #LogMessage(dirfiles)
                if len(dirfiles) >0:
                    self.ParentTreeDisplay(dirfiles[0], i + 1)
                    break
        return 0