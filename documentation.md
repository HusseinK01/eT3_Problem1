
For this problem I took the following steps

1. Began by specifying the paths to both the source and destination folders.
2. Created a list to keep track of filenames and prevent any duplicates from being lost.
3. Generated a CSV file and included appropriate headers.
4. Implemented a loop to iterate over the directories within the source folder. Removed the initial prefix (company name) from each filename.
5. Checked if a file with the same name already exists. If it does, a "b" is appended to the filename to avoid any loss during the copying process.
6. Constructed the source and destination file paths.
7. Utilized OS and datetime methods to collect image metadata, such as the last modification time (using getmtime) and converted it to a readable format.
8. Wrote the collected metadata into the CSV file.
9. Copied the file into the destination folder.

On how to run the solution: 
simply run problem1.py and the image_dataset folder will be populated. The csv report
will be created as well.