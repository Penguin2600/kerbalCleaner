#!/usr/bin/python
import re

def main():

    debrisFound=0
    debrisBeginLine=0
    debrisEndLine=0
    lineCount=0

    pData = []
    pFile = open('persistent.sfs', 'r+')
    pData = pFile.readlines()
    pFile.close()

    endVessel=re.compile(r"^\t\t}")
        
    for l in pData:
        
        if "VESSEL" in l:
            print "Begin Vessel:", lineCount
            debrisBeginLine=lineCount-1
                
        if "Debris" in l:
            debrisFound=1
            print "DEBRIS FOUND"
                    
        match=re.search(endVessel, l)
            
        if match:
            print "End Vessel:", lineCount
            debrisEndLine=lineCount

            if debrisFound==1:
                print "deleting lines", debrisBeginLine, "to", debrisEndLine
                for i in range(debrisBeginLine, debrisEndLine):
                    pData[i]=""
                debrisFound=0


        lineCount += 1
        
    pFile = open('persistent_new.sfs', 'w')
    pFile.truncate()
    for i in pData:
        if i:
            pFile.write(i)
    pFile.close()

    print "Done"

if __name__=="__main__":

    main()
