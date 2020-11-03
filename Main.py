###Import statement from functions file into main file###

from Volume import Cube_Volume, Pyramid_Volume, Ellipsoid_Volume, formatInput, summarize, Sort_List

###Variables and Lists###

Processed_Shape_Input=0
C_Counter=0
P_Counter=0
E_Counter=0
Shape_Counter=0
EXIT_LIST=["q"]
Cube_Volumes_List=[]
Pyramid_Volumes_List=[]
Ellipsoid_Volumes_List=[]

###Beginning of main program###

print("     ***    WELCOME TO THE AMAZING VOLUME CALCULATOR!   ***        ")    #Title and Legend
print("")
print("Cube = c")
print("Pyramid = p")
print("Ellipsoid = e")
print("Quit = q")
print("")

while Processed_Shape_Input not in EXIT_LIST:
    Shape_Input= input("Please input type of shape: ")                          #Prompt for type of shape
    Processed_Shape_Input= formatInput(Shape_Input)
    if Processed_Shape_Input in "c":                                            #Cube operations/calculations
        Side_Length=input("Please input a positive, integer side length value: ")
        Side_Length=int(Side_Length)
        C_Volume=Cube_Volume(Side_Length)
        C_Value_Storage=Cube_Volumes_List.append(C_Volume)                      #Cube Value added to list
        C_Counter=C_Counter+1
    elif Processed_Shape_Input in "p":                                          #Pyramid operations/calculations
        Base_Length=input("Please input a positive, integer base length value: ")
        Base_Length=int(Base_Length)
        Height=input("Please input a positive, integer height value: ")
        Height=int(Height)
        P_Volume=Pyramid_Volume(Base_Length,Height)
        P_Value_Storage=Pyramid_Volumes_List.append(P_Volume)                   #Pyramid value added to list
        P_Counter=P_Counter+1
    elif Processed_Shape_Input in "e":                                          #Ellipsoid operations/calculations
        Radius1=input("Please input a positive, integer radius value: ")
        Radius1=int(Radius1)
        Radius2=input("Please input another positive, integer radius value: ")
        Radius2=int(Radius2)
        Radius3=input("Please input a final positive, integer radius value (last one I promise!): ")
        Radius3=int(Radius3)
        E_Volume=Ellipsoid_Volume(Radius1,Radius2,Radius3)
        E_Value_Storage=Ellipsoid_Volumes_List.append(E_Volume)                 #Ellipsoid value added to list
        E_Counter=E_Counter+1
    elif Processed_Shape_Input in "q":                                          #Exit/quit operations and actions
        Shape_Counter=(C_Counter + P_Counter + E_Counter)
        if Shape_Counter != 0:                       #Exportation of sorted lists to new file with parameters/conditions
            Sort_List(Cube_Volumes_List)
            Sort_List(Pyramid_Volumes_List)
            Sort_List(Ellipsoid_Volumes_List)
            Test_Number=input("Please input a test number: ")
            Test_Number=int(Test_Number)
            Exporting_Of_Data=summarize(Cube_Volumes_List,Pyramid_Volumes_List,Ellipsoid_Volumes_List,Test_Number)
            print("You have reached the end of your session")
            print("The volumes calculated for each shape are:")
            if C_Counter != 0:                #Dealing with no entries in only a particular shape(s) in the main program
                print("Cube: ",Cube_Volumes_List)
            else:
                print("Cube: No shapes entered")
            if P_Counter != 0:
                print("Pyramid: ",Pyramid_Volumes_List)
            else:
                print("Pyramid: No shapes entered")
            if E_Counter != 0:
                print ("Ellipsoid: ",Ellipsoid_Volumes_List)
            else:
                print("Ellipsoid: No shapes entered")
        else:                                                           #Dealing with no entries at all
            print("")
            print("This is the end of your session")
            print("You did not perform any volume calculations")
    else:                                                               #Dealing with invalid entries for type of shape
        print("Sorry, this is not a shape or an exit option")
