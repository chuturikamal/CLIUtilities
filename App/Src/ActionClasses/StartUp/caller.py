from ..Service.ServiceInterface import ServiceInterface
from ..Service.TransferService import TransferService
from ..Service.DirectoryTreeService import DirectoryTreeService
from ..Utilities.DirectoryUtility import LogMessage

class caller:
    def __init__(self, opt):
        self.opt = opt

    def initiateCmd(self, args):
        ServiceObj = ServiceInterface()
        msg = ''
        if self.opt == 0:
            ServiceObj = TransferService()
            msg = 'Transfer from Download files'
        elif self.opt == 1:
            ServiceObj = DirectoryTreeService(args)
            msg = 'Tree Directory Structure'

        self.callService(ServiceObj, msg)


    def callService(self, obj, msg):
        print(f'|------------------- Initiated {msg} ---------------------|')
        serviceObj = obj
        serviceObj.Start()
        print(f'|------------------- Ended {msg} ---------------------|')
        pass