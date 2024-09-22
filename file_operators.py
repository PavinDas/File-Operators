import os


#! rename files
def bulk_rename_files(directory, prefix, extension=None):
    # List all files in the given directory
    try:
        files = os.listdir(directory)
        # Filter files based on extension (if provided)
        if extension:
            files = [f for f in files if f.endswith(extension)]
        files.sort()  # Sort to rename files in order

        # Loop over the files and rename them
        for index, filename in enumerate(files):
            # Extract the file extension
            file_extension = os.path.splitext(filename)[1]

            # Build the new file name
            new_name = f"{prefix}_{index + 1}{file_extension}"

            # Form the full path for the old and new names
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_name}'")

        print("Bulk rename completed.")
    except Exception as e:
        print(f"Error renaming files: {e}")


# * File renamer calling
def bulk_rename_calling():
    # Replace with the directory path where your files are located
    directory = input("Enter path: ")

    # Define a new prefix for the renamed files
    prefix = input("Enter new name: ")

    # Optionally, define a specific extension (e.g., ".txt") or set to None to rename all files
    x = input("have you any extension? [Yes:y/ No:n]")
    if x == "y" or x == "yes" or x == "Y" or x == "Yes" or x == "YES":
        extension = input("Enter extension (exclude '.'): ")
    else:
        extension = None

        # Call the function to rename files in bulk
    bulk_rename_files(directory, prefix, extension)


#! Remove Empty Folders
def remove_empty_folders(directory):
    # Walk the directory tree in reverse to check for empty folders
    for dirpath, dirnames, filenames in os.walk(directory, topdown=False):
        for dirname in dirnames:
            # Create the full path to the directory
            dir_to_check = os.path.join(dirpath, dirname)
            try:
                # Check if the directory is empty
                if not os.listdir(dir_to_check):  # Directory is empty
                    os.rmdir(dir_to_check)  # Remove the empty directory
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
