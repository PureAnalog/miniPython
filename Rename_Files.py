import os

# 1. get file names from a folder

# 2. for each file, rename filename



def rename_files():
    file_list = os.listdir(r"C:\Users\phill_000\Desktop\whatever")
    #print(file_list)

   
    print( "Current working Directory is: " + os.getcwd())
    os.chdir("C:\Users\phill_000\Desktop\whatever")
    print( "Current working Directory is: " + os.getcwd())
    for file_name in file_list:
        os.rename( file_name, file_name.translate(None, "0123456789"))

    print(file_list)
    
rename_files()

