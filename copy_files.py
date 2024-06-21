import os
import shutil

# Define the source and destination directories
source_dir = 'C:\CarMaker\VIL_Master_CM1023_Lastest_05172024\Data\Road\PCA'
dest_dir = 'C:\CarMaker\VIL_Master_CM1023_Lastest_05172024\Data\Road\Radar Test'

# Define the exact file names to copy
files_to_copy = [
'1_ALC_passing_PO_left.rd5',
'1_ALC_passing_PO_left.rd5',
'1_ALC_passing_PO_left.rd5',
'Radar_TestRoad.rd5',
'PCAi_2p3_NearSideTurn.rd5',
'PCAi_Ped.rd5',
'ALC_DriveInLeftLane_3Lanes.rd5'
]

try:
    # List all files in the source directory
    files = os.listdir(source_dir)

    for file_name in files:
        # Check if file name is in the list of files to copy
        if file_name in files_to_copy:
            # Construct full file path
            source_file = os.path.join(source_dir, file_name)
            
            # Ensure it's a file and not a directory
            if os.path.isfile(source_file):
                # Construct destination file path
                dest_file = os.path.join(dest_dir, file_name)
                
                # Check if the file already exists in the destination directory
                if not os.path.exists(dest_file):
                    # Copy the file
                    shutil.copy(source_file, dest_file)
                    print(f"Copied: {file_name}")
                else:
                    print(f"File already exists and won't be copied: {file_name}")

    print("Specified files have been copied.")
except Exception as e:
    print(f"An error occurred: {e}")