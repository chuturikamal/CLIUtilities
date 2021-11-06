import click
from .caller import caller

@click.group()
def ClickGroup():
    pass

@click.command(name="transfer")
def DownloadFilesTransfer():
    sendCmd(0, '')

@click.command(name="tree")
@click.option('--u', 'direction', flag_value='upper', help='direction of the tree')
@click.option('--l', 'direction', flag_value='lower', help='direction of the tree')
@click.option('--d','direction', default='upper')
def CreateDirectoryTree(direction):
    sendCmd(1, direction)

ClickGroup.add_command(DownloadFilesTransfer)
ClickGroup.add_command(CreateDirectoryTree)

def callCommands():
    ClickGroup()

def sendCmd(option, args):
    callObj = caller(option)
    callObj.initiateCmd(args)