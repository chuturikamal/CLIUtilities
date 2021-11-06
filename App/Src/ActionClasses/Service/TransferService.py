from .ServiceInterface import ServiceInterface
from ..Utilities.DirectoryUtility import FetchDirectoryFiles, LogMessage, extSplit, fileMove
import shutil

class TransferService(ServiceInterface):
    def __init__(self):
        self.LoadSupportedExtensions()
        self.LoadPaths()
        
    def LoadSupportedExtensions(self):
        self.extAppList = ['.dmg']
        self.extMovieList = ['.mp4', '.mkv']
        self.extMusList = []
        self.extPicList = ['.jpg', '.png']

    def LoadPaths(self):
        self.DownloadPath = '/Users/chuturikamalmurthy/Downloads'
        self.MoviesPath = '/Users/chuturikamalmurthy/Movies'
        self.musicPath = '/Users/chuturikamalmurthy/Music'
        self.picturePath = '/Users/chuturikamalmurthy/Pictures'
        self.applicationPath = '/Users/chuturikamalmurthy/Applications'

    def Start(self):
        LogMessage('Service Call Started')
        getFiles = FetchDirectoryFiles(self.DownloadPath)

        for file in getFiles:
            if not file.startswith('.'):
                fileTuple = extSplit(file)
                fileName = fileTuple[0]
                fileExtesion = fileTuple[1]
                self.extTransfer(file, fileExtesion)
        LogMessage('Service Call ended')


    def extTransfer(self, fileName, fileExtesion):
        src = self.DownloadPath + '/' + fileName
        destinationPath = ''
        #Applications
        if fileExtesion in self.extAppList:
            LogMessage(f'{fileName} is a Application Type')
            destinationPath = self.applicationPath
        #Movies
        elif fileExtesion in self.extMovieList:
            LogMessage(f'{fileName} is a Movies Type')
            destinationPath = self.MoviesPath
        #Musics
        elif fileExtesion in self.extMusList:
            LogMessage(f'{fileName} is a Music Type')
            destinationPath = self.musicPath
        #Pictures
        elif fileExtesion in self.extPicList:
            LogMessage(f'{fileName} is a Picture Type')
            destinationPath = self.picturePath

        destinationPath += '/' + fileName
        
        fileMove(src, destinationPath)