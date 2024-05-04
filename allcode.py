import os


def gather_files(directory, extensions):
    """ Recursively gather all files in the specified directory with given extensions. """
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(extensions)):
                files_list.append(os.path.join(root, file))
    return files_list


def concatenate_files(files, output_file):
    """ Concatenate the contents of each file into a single output file. """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file in files:
            with open(file, 'r', encoding='utf-8') as infile:
                outfile.write(f"// Start of {file}\n")
                outfile.write(infile.read())
                outfile.write(f"\n// End of {file}\n\n")


# Define the folder path and output file
folder_path = ''
output_file = 'all_code_concatenated.txt'

# Specify the file extensions
code_extensions = ['.py', '.java']

# Gather and concatenate the files
files = gather_files(folder_path, code_extensions)
concatenate_files(files, output_file)
