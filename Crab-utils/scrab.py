import os
import argparse

parser = argparse.ArgumentParser("scrab version 1.0")
parser.add_argument('command', help='Command to launch into dir')
parser.add_argument('-d', dest='directory', type=str, default='')
parser.add_argument('-p', dest='prefix', type=str, default='')
args = parser.parse_args()


### Crab status
if 'status' in args.command:

    for it in os.scandir(args.directory):
        if it.is_dir():
            os.system('crab ' + args.command + ' ' + it.path)


### Crab submit
if 'submit' in args.command:

    for it in os.scandir(args.directory):

        path = it.path
        filename = path.split('/')[-1]
        nprefix = len(args.prefix)
        file_prefix = filename[:nprefix]

        if args.prefix==file_prefix and filename[-3:]=='.py':
            os.system('crab ' + args.command + ' ' + it.path)
       


