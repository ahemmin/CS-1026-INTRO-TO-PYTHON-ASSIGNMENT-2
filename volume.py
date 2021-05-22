import math
###Cube Volume Formula###

def Cube_Volume(Side_Length):
    Volume=Side_Length**3
    Volume=round(Volume,3)
    return Volume


###Pyramid Formula###

def Pyramid_Volume(Base_Length,Height):
    Volume=(1/3)*((Base_Length**2)*(Height))
    Volume=round(Volume,3)
    return Volume

###Ellipsoid Formula###

def Ellipsoid_Volume(Radius1,Radius2,Radius3):
    Volume=((4/3)*(math.pi))*(Radius1*Radius2*Radius3)
    Volume=round(Volume,3)
    return Volume

###String Processor###

def formatInput(TextLine):
    TextLine=TextLine.lower().strip()
    Wordlist=TextLine.split()
    TextLine="".join(Wordlist)
    return TextLine

###Value Processing and Exporting###

NEWLINE = "\n"
DASH = "-"
SPACE = " "

def summarize(clist,plist,elist,testNumber):
    fname = "Asgn2TestCase" + str(testNumber)
    print()
    print("*** Creating output for test "+ str(testNumber))
    print()
    outf = open(fname,"w")
    output_list(clist,outf)
    output_list(plist,outf)
    output_list(elist,outf)
    outf.close()

def output_list(lst,outfile):
    lngth = len(lst)
    if lngth > 0:
        for item in lst:
            str = "%6.2f" % item
            outfile.write(str+SPACE)
        outfile.write(NEWLINE)
    else:
        outfile.write(DASH+NEWLINE)

###List Sorting###

def Sort_List(List):
    List=List.sort(reverse=False)
    return List
