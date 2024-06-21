import os
import shutil

# Define the source and destination directories
source_dir = 'C:\CarMaker\VIL_Master_CM1023_Lastest_05172024\Data\Road'
dest_dir = 'C:\CarMaker\VIL_Master_CM1023_Lastest_05172024\Data\Road\Video Box'

# Define substrings to identify the files to move
# For example, move files that contain 'report' or 'summary' in their names
substrings_to_match = [
'PCA_C2C_Road_CL.rd5',
'PCA_C2C_Road.rd5',
'AlignmentRoad.rd5'
]

try:
    # List all files in the source directory
    files = os.listdir(source_dir)

    for file_name in files:
        # Check if file name contains any of the specified substrings
        if any(substring in file_name for substring in substrings_to_match):
            # Construct full file path
            source_file = os.path.join(source_dir, file_name)
            
            # Ensure it's a file and not a directory
            if os.path.isfile(source_file):
                # Construct destination file path
                dest_file = os.path.join(dest_dir, file_name)
                
                # Move the file
                shutil.move(source_file, dest_file)
                print(f"Moved: {file_name}")

    print("Specified files have been moved.")
except Exception as e:
    print(f"An error occurred: {e}")