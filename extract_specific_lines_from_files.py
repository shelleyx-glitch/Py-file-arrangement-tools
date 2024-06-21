import os

def extract_specific_lines_from_files(directory_path, keyword):
    # List all files in the given directory
    try:
        files = os.listdir(directory_path)
    except FileNotFoundError:
        print("The directory was not found. Please check the path.")
        return

    # Loop through each file in the directory
    for file_name in files:
        # Construct full file path
        file_path = os.path.join(directory_path, file_name)
        
        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            try:
                # Open and read the file line by line
                with open(file_path, 'r') as file:
                    for line in file:
                        # Check if the line contains the keyword
                        if keyword in line:
                            print(f"Found in {file_name}: {line.strip()}")
            except Exception as e:
                print(f"Could not read {file_name}: {e}")

# Replace 'your/directory/path' with the path to the directory containing your files
directory_path = 'C:\CarMaker\VIL_Master_CM1023_05212024\Data\TestRun\BlueCruise\SILC'
# Define the keyword to search for in each line

keyword = 'Road.FName'
#keyword = 'Link.0.Seg.1.File = '

extract_specific_lines_from_files(directory_path, keyword)