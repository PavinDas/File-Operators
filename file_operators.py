import os


#! rename files
def bulk_rename_files(directory, prefix, extension=None):
    try:
        # ? List all files
        files = os.listdir(directory)
        # ? Filter files by extension
        if extension:
            files = [f for f in files if f.endswith(extension)]
        files.sort()

        for index, filename in enumerate(files):
            # ? Separate file extension
            file_extension = os.path.splitext(filename)[1]

            # ? create new file name
            new_name = f"{prefix}_{index + 1}{file_extension}"

            # ? create full path
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_name)

            # ? Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_name}'")

        print("Bulk rename completed.")
    except Exception as e:
        print(f"Error renaming files: {e}")


# * File renamer calling
def bulk_rename_calling():
    directory = input("Enter path: ")

    prefix = input("Enter new name: ")

    x = input("have you any extension? [Yes:y/ No:n]")
    if x == "y" or x == "yes" or x == "Y" or x == "Yes" or x == "YES":
        extension = input("Enter extension (exclude '.'): ")
    else:
        extension = None

    bulk_rename_files(directory, prefix, extension)


#! Remove Empty Folders
def remove_empty_folders(directory):
    #? Walk to direcories and subdirecories
    for dirpath, dirnames, filenames in os.walk(directory, topdown=False):
        for dirname in dirnames:
            #? Create the full path to the directory
            dir_to_check = os.path.join(dirpath, dirname)
            try:
                #? Check the directory is empty or not
                if not os.listdir(dir_to_check):
                    os.rmdir(dir_to_check) 
                    print(f"Removed empty folder: {dir_to_check}")
            except OSError as e:
                print(f"Error removing {dir_to_check}: {e}")


def select_choice():
    print("1. Rename all files \n2. Remove empty folders")
    user_choice = input("_____________\nSelect one: ")

    if user_choice == "1":
        bulk_rename_calling()
    elif user_choice == "2":
        remove_empty_folders(input("Enter the path: "))
    else:
        print("Invalid input")
        select_choice()


select_choice()
