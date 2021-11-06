#!/usr/bin/python3
from Src.ActionClasses.StartUp.CmdCaller import callCommands
from Src.ActionClasses.StartUp.testCmdCaller import Testcmd

def main():
    cmd = callCommands()
    #Testcmd(1)

if __name__ == '__main__':
    main()
