import os
from os import listdir
from os.path import isfile, join


#generic name
genericName="file"

#path for dir where are the files
mypath = "C:\\Users\\amand\\OneDrive\\Documentos\\Projetos\\Git\\JavaScript\\teste"

def RenameFilesGenericName(genericName, mypath):

    #list of files
    nameFiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    extensionFile = "."+nameFiles[0].split(".")[1]

    #Directory+Name of Files
    pathOldFiles = [os.path.join(mypath, file) for file in nameFiles] 
    pathNewFiles = [os.path.join(mypath, genericName+str(numberFile+1)+extensionFile) for numberFile in range(len(nameFiles))] 

    rename = [os.rename(pathOldFiles[numberFile], pathNewFiles[numberFile]) for numberFile in range(len(pathOldFiles))]

RenameFilesGenericName(genericName, mypath)
