# Task (1):
# Unpack the archive to extract the directory containing the profiles

# Import necessary modules 
import shutil 
from pathlib import Path

print("Unpacking archive...")

# Set path to the archive file
archive_file = Path.cwd()/"profiles.tar.gz"

# Set path to destination directory
extract_dir = Path.cwd()

# Define the archive format (.tar.gz) 
archive_format = "gztar"

# Extract the contents of the archive
shutil.unpack_archive(archive_file, extract_dir, archive_format) 

print("<< Archive file unpacked successfully. Profiles have been extracted >>") 
