import sys
import os
from os import rename
from os import walk
from os.path import exists


def main():
    prefix, directory = get_input()

    if exists(directory) is False:
        print("This path does NOT exist.")

    else:
        print("Doing replacement...")
        rename_file_with_prefix(prefix,directory)



def get_input():
    print(" You entered", len(sys.argv)-1, "arguments at the command line.")

    if len(sys.argv) != 3:
        # Ordinary exception now vs. IndexError: list index out of range.
        raise Exception(
            " Error: Wrong number of arguments. Enter 2 arguments: 1. "
            " Prefix to be removed 3. Path foor the files ")

    # Read in parameters.
    prefix = sys.argv[1]
    directory = sys.argv[2]
   

    print(' Prefix:\t', prefix)
    print(' Directory path:\t', directory)
    print()
    return prefix, directory

def rename_file_with_prefix(prefix,directory):
    # directory = "YOUR DIRECTORY NAME"
    # prefix = 'Your Prefix'
    for filename in os.listdir(directory):
        if filename.startswith(prefix):
            old_filepath = os.path.join(directory, filename)
            if filename.startswith(prefix):
                 new_filename = filename[len(prefix):]  # Remove the prefix
            else:
                return filename
            new_filepath = os.path.join(directory, new_filename)
            os.rename(old_filepath, new_filepath)
            print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == '__main__':
    main()
