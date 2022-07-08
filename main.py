import  os,sys

currentdir = os.curdir

#this is the instructions file. It includes instructions to how the files should be organised. the folder is before the > and all extentions that should go in it are afterwards. New folder names can be added to any amount as the Folder Function in this program is fully dynamic

#BUG: If a line ends with a comma in the instructions_file.txt the folders  go inside other folders.
#TODO: Should be able to understand when a line ends with just a comma


#iFile = f"D:\i.txt"
#Letting users define where the instruction file is:
#If i FIle  is present in same directory as "i.txt" no need to ask user

iFile = input("Instructions File Full path:\n")
while iFile.find(".txt") < 0: #make it sure that a txt file is given to us
    print("IFile can only be a txt file. The syntax is Folder>ext,ext,ext,ext\n Make sure to never keep a comma at the end of a line!")
    iFile = input("Instructions File Full path:\n")

#Instruction dictionary is how this is made dynamic. The key is the folder name while the value holds a list of the extentions as a list.
Instructions = {}

def iUpdate(location):
    """
    Reads the Instructions File. Adds all the instructions to the instructions dictionary.
    """
    with open(location, 'r') as iFile:
        lines = iFile.readlines()
        for line in lines:
            if line[-1] == ",":
                print("iFile is ending a line with a comma. This may cause unexpected results. Script is exiting!")
                sys.exit()
            seppos = line.find(">")
            seppos = seppos
            
            #changing extensions to a list
            all_exts = line[seppos+1:].rstrip()
            Instructions[line[:seppos]] = all_exts.split(",")
            Folder()
            
def Folder():
    """
    Executes all instructions from the dictionary file of instructions.
    """
    for key in Instructions:
        #creation of folders - TODO:We should delete empty folders afterwards!
        try:
            os.mkdir(key)
        except FileExistsError: #Should change to exec only if file exists so no waste
            pass
        
        
        extentions = []
        extentions.append(Instructions[key])
        filenamz = os.listdir()

        for  filename in  filenamz:
            (name,ext) = os.path.splitext(filename)
            ext = ext.replace(".","")
            #print(ext)
            if ext in extentions[0]:
                #print(f"{filename} shouuld be moved inside {key} folder")
                try:
                    if os.path.isdir(filename) == False: #make sure no directories are moved
                        if filename != os.path.basename(__file__): #make sure the current python file doesnt get moved
                            os.rename(filename,f"{currentdir}/{key}/{filename}")
                except:
                    continue

        #print(extentions[0])

    #deal with the rest of the files
    for  filename in  filenamz:
        try:
            os.mkdir("Others") #Make an others folder - TODO:Maybe users should be able to define the name of the folder.
        except FileExistsError:
            pass
        
        try:    
            if os.path.isdir(filename) == False: #make sure no directories are moved
                if filename != os.path.basename(__file__): #make sure the current python file doesnt get moved
                    os.rename(filename,f"{os.curdir}/Others/{filename}")
        except:
            continue
    cleanup()


def cleanup():
    working_dir = os.curdir
    dirs = os.listdir(working_dir)
    #print(dirs)
    for dir in dirs:
        if os.path.isdir(dir) == False: #must skip files
            continue
        #print(len(os.listdir(dir)))
        if len(os.listdir(dir)) == 0:
            os.rmdir(dir)


iUpdate(iFile)



        
                
    
    