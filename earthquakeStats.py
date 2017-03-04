def frequencyTable(countdict):
    
    print("ITEM", "\t", "FREQUENCY")
    ## print the dictionary sorted by the key
    
    for i in sorted(countdict):
        print(i, "\t", countdict.get(i))

def mode(alist, countdict):

    ## iterate over alist and build a dictionary called countdict
    ## to store the frequency of each value in alist

    for i in alist:
        if i in countdict:
            n = countdict.get(i)
            n = n + 1
            countdict[i] = n
        else:
            countdict[i] = 1

    maxcount = -1## find the highest value in a value componet of the dictionary
    
    for i in countdict:
        v = countdict.get(i)
        if v > maxcount:
            maxcount = v

    modelist = [ ]      ## creates a list of modes since there may be more than one mode        
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)
    return modelist

def median(alist):
    median = sorted(alist[:])[len(alist) // 2] if len(alist) % 2 == 0 else (sorted(alist[:])[len(alist) // 2] + sorted(alist[:])[len(alist) // 2 + 1]) / 2
    return median

def makeMagnitudeList():
        quakefile = open("earthquakes.txt","r")
        headers = quakefile.readline()
        
        maglist = [ ]
        for aline in quakefile:
            vlist = aline.split()
            maglist.append(float(vlist[1]))
        return maglist  

def main():
    magList = makeMagnitudeList()
    print(magList)
    print("mean: ", sum(magList) / len(magList))
    frequencyDict = {}
    med = median(magList)
    print("median: ", med)
    mod = mode(magList, frequencyDict)
    print("mode: ", mod)
    frequencyTable(frequencyDict)

if __name__ == '__main__':
    main()
