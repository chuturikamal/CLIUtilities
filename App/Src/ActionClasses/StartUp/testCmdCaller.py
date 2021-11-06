from .caller import caller

def Testcmd(opt = 0):
    if opt == 0:
        sendCmd(0, '')
    elif opt == 1:
        sendCmd(1, 'lower')


def sendCmd(option, args):
    callObj = caller(option)
    callObj.initiateCmd(args)