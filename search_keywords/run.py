from zipfile import ZipFile
import os 

def main():

    # VARIABLES
    is_code_run = True
    
    cycle = True
    
    # Temp folder name
    temp_folder = "temp"

    # MAIN APP CYCLE 
    while is_code_run:

        # User inputs keyword
        keyword = input("Input keyword: ")

        # Search all files in project folder
        for file in os.listdir("."):

            # Get zip files only
            if file.endswith(".zip"):

                # Extract zip file
                extract_ZIP_file_to_Temp_folder(file, keyword, temp_folder)

        # CONTINUE CYCLE
        while cycle:

            # Ask user to search another keyword
            to_continue = input("Do you want to search another keyword? [y]/n ")
            
            if to_continue == "y":
                is_code_run = True
                cycle = False

            elif to_continue == "n":
                is_code_run = False
                cycle = False

            else:
                print("Unknown answer")
                cycle = True



def extract_ZIP_file_to_Temp_folder(ZIP_file, keyword, temp_folder):

    # Create a ZipFile Object and load sample.zip in it
    with ZipFile(ZIP_file, 'r') as zipObj:
            
        # Get a list of all archived file names from the zip
        listOfFileNames = zipObj.namelist()
                
        # Iterate over the file names
        for fileName in listOfFileNames:
                
            # Check filename endswith BASH
            if fileName.endswith('.sh'):
                
                # Extract a BASH-files from zip
                zipObj.extract(fileName, temp_folder)

                # Find keywords in BASH-files
                find_keyword_in_bash(keyword, temp_folder)


def find_keyword_in_bash(keyword, temp_folder):

    # Get each temp file
    for BASH_file in os.listdir(temp_folder):
        print(BASH_file)

        # Open temp file
        with open("temp/" + BASH_file) as openfile:

            # Check each line
            for line in openfile:

                # Split line in parts and check parts separetly
                for part in line.split():
                    
                    # If keyword is found, print part with keyword
                    if keyword in part:
                        print(part)
        
        # Remove temp file
        os.remove(os.path.join("temp/" + BASH_file))

    # Remove temp folder
    os.rmdir(os.path.join(temp_folder))

if __name__ == '__main__':
    main()