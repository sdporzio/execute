import os, sys, argparse

def GenerateScript(inputFile,inputString):
    commands = 0
    cwd = os.path.dirname(os.path.realpath(__file__))
    fOut = open(cwd+'/script.tempexe','w')
    if inputFile:
        fIn = open(inputFile,'r')
        commands = [line[:-1] if line[-1]=='\n' else line for line in fIn.readlines()]
    if inputString:
        commands = [inputString]
    for i,cmd in enumerate(commands):
        startTime = 'export START_TIME=$(date)\n'
        printCmd = 'echo -e "\033[1;33m-> %s \033[0m"\n' %(cmd)
        wrapCmd = '{ unbuffer time %s ; } 2>&1 | tee -a %s/Logs/status%i.templog\n' %(cmd,cwd,i)
        endTime = 'export END_TIME=$(date)\n'
        sleep = 'sleep 1\n'
        mail = 'echo -e "---> Job completed:\\n%s\\n\\n\\n---> Start time:\\n${START_TIME}\\n---> End time:\\n${END_TIME}\\n\\n\\n---> Job end:\\n$(tail --lines=10 %s/Logs/status%i.templog)\\n\\n\\n---> Full job log:\\n$(less %s/Logs/status%i.templog)" | mutt -s "Job %s (%s of %s) finished" salvatore.porzio@postgrad.manchester.ac.uk\n' %(cmd,cwd,i,cwd,i,cmd,i+1,len(commands))
        fOut.write(startTime)
        fOut.write(printCmd)
        fOut.write(wrapCmd)
        fOut.write(endTime)
        fOut.write(sleep)
        fOut.write(mail)
    fOut.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-if','--inputFile',required=False,help='Input file',type=str)
    parser.add_argument('-is','--inputString',required=False,help='Input string',type=str)
    args = parser.parse_args()
    GenerateScript(args.inputFile,args.inputString)

if __name__ == '__main__':
    main()
