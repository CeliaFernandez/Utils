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
    for i in range(0, len(files)):
        if counterIter == nFilesPerChunk:
            counterIter = 0
        if counterIter == 0:
            target = options.dir + '/chunk_' + str(counter)
            os.mkdir(target)
            counter = counter + 1
        p = subprocess.Popen(["cp", files[i], target], stdout=subprocess.PIPE)
        counterIter = counterIter + 1 

    runf = open(options.run, 'w')
    for i in range(0, options.n):
        target = options.dir + '/chunk_' + str(i)
        runf.write('hadd ' + options.dir + '/' + options.sample + '_chunk' + str(i) + '.root ' + target + '/*.root > output_' + str(i) + '.log 2> output_' + str(i) + '.err' + '\n')

    runf.close()


        

