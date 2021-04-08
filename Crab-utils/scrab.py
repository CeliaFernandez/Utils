import os
import argparse

parser = argparse.ArgumentParser("scrab version 1.0")
parser.add_argument('command', help='Command to launch into dir')
parser.add_argument('-d', dest='directory', type=str)
args = parser.parse_args()

print(args.directory)

for it in os.scandir(args.directory):
    if it.is_dir():
        os.system('crab ' + args.command + ' ' + it.path)






