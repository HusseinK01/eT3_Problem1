import math
import os
import shutil
import csv
import datetime


source_folder = './dairies'
destination_folder = './image_dataset'
if not os.path.exists(destination_folder):
    os.makedirs('image_dataset')

file_names = []
# Create the csv file that will hold images metadata
with open('Report.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Image', 'Image size (KB)', 'Image Modification Date'])
# Iterate over the root folder and its subfolders
for root, _, files in os.walk(source_folder):
    for filename in files:
        # Extract the last part of the filename after the first dash
        split_filename = filename.split('-', 1)  # Split at the first dash
        new_filename = split_filename[1] if len(split_filename) > 1 else filename
        if new_filename in file_names:
            new_filename = new_filename[:-4] + 'b.jpg'
        file_names.append(new_filename)

        # Construct the source and destination paths
        source_path = os.path.join(root, filename)
        destination_path = os.path.join(destination_folder, new_filename)

        # Add image metadata to the csv report
        image_size_kb = math.floor(os.path.getsize(source_path) / 1024)
        mod_date_unix = os.path.getmtime(source_path)
        mod_date_readable = datetime.datetime.utcfromtimestamp(mod_date_unix).strftime('%Y-%m-%d')

        with open('Report.csv', mode='a', newline='') as report:
            writer = csv.writer(report)
            writer.writerow([new_filename, image_size_kb, mod_date_readable])

        # copy the files into destination folder
        with open(source_path, 'rb') as src_file:
            with open(destination_path, 'wb') as dest_file:
                shutil.copyfileobj(src_file, dest_file)
