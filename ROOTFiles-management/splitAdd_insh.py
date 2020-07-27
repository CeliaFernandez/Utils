import os
import subprocess
from optparse import OptionParser




if __name__ == "__main__":

    parser = OptionParser(usage="%prog --help")
    parser.add_option("-d", "--dir",       dest="dir",         type="string",   default='.',            help="Input directory")
    parser.add_option("-n", "--number",    dest="n",           type=int,        default=5,              help="Number of chunks")
    parser.add_option("-r", "--run",       dest="run",         type="string",   default='run.sh',       help="Name of run.sh")
    parser.add_option("-s", "--sample",    dest="sample",      type="string",   default='DY',           help="Name of sample")
    (options, args) = parser.parse_args()


    files = []
    for i in os.listdir(options.dir):
        if '.root' not in i:
            continue
        files.append(options.dir + '/' + i)

    counter = 0
    counterIter = 0
    nFilesPerChunk = int(len(files)/options.n)
    command = ''
    runf = open(options.run, 'w')
    c = 0
    for i in range(0, len(files)):
        if counterIter == nFilesPerChunk:
            command+= '> chunk'+ str(c)+'.log 2> chunk'+str(c)+'.err'
            runf.write(command)
            runf.write('\n')
            #os.system(command)
            counterIter = 0
            c+=1
        if counterIter == 0:
            command = 'hadd ' + options.sample + '_chunk'+str(c)+'.root '
            counter = counter + 1
        counterIter = counterIter + 1 
        command +=  files[i] + ' '

    command+= '> chunk'+ str(c)+'.log 2> chunk'+str(c)+'.err'
    runf.write(command)

    runf.close()


        

