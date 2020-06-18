def lineCount(fileName):
    count=0
    f=open(fileName)
    for i in f:
        count+=1
    return count

if __name__=='__main__': # This will contain tests that you are used to check this specific file       
    print(lineCount('wc.py'))