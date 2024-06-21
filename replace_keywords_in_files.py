import os

def replace_keywords_in_files(directory_path, replacements):
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
                # Open and read the file
                with open(file_path, 'r') as file:
                    content = file.read()

                # Replace keywords in the content
                for old, new in replacements.items():
                    content = content.replace(old, new)

                # Write the modified content back to the file
                with open(file_path, 'w') as file:
                    file.write(content)

                print(f"Updated {file_name}")
            except Exception as e:
                print(f"Could not update {file_name}: {e}")

# Replace 'your/directory/path' with the path to the directory containing your files
directory_path = 'C:\CarMaker\VIL_Master_CM1023_05212024\Data\TestRun\BlueCruise\SILC'
# Define your replacements here: 'old_keyword': 'new_keyword'
replacements = {
    'Road.FName = SILC Road files/': 'Road.FName = SILC/',
    #'Link.0.Seg.1.File = BC_LMC_Tests/DDC/RoadSeg/': 'Link.0.Seg.1.File = BC_LMC_Tests/DDC/RoadSeg/',

#    'old_keyword2': 'new_keyword2',
    # Add more replacements as needed
}
replace_keywords_in_files(directory_path, replacements)