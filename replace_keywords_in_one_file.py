# Define the path to your file. Include the file name and extension.
file_path = 'C:\CarMaker\VIL_Master_CM1023_Lastest_05172024\Data\TestRun\BlueCruise\BC LMC Tests\APG Events\Curves.ts'

# Define the keywords to be replaced and their replacements
# For example, replacing 'old_keyword' with 'new_keyword'
replacements = {
    'BlueCruise/APG Events/Curves/': 'BlueCruise/BC LMC Tests/APG Events/Curves/',
    # Add more replacements as needed
}

# Read the content of the file
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Replace the keywords
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print("File has been updated.")
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
