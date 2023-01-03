import os
import sys
import zipfile

def extract_zip(zip_path, destination_path):
  """
  Extract the zip file at the specified path to the specified destination.
  """
  # create destination folder if it doesn't exist
  if not os.path.exists(destination_path):
    try:
      os.makedirs(destination_path)
    except OSError:
      print(f"Error: Could not create destination folder at {destination_path}")
      return

  # extract zip file
  try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
      zip_ref.extractall(destination_path)
  except (zipfile.BadZipFile, IOError):
    print(f"Error: Could not extract zip file at {zip_path}")

def main():
  # check if a zip file path was passed as an argument
  if len(sys.argv) < 2:
    print("Please provide the path to a zip file as an argument")
    return

  # get zip file path from arguments
  zip_path = sys.argv[1]

  # create destination folder name by removing .zip from the zip file name
  destination_folder_name = os.path.splitext(os.path.basename(zip_path))[0]
  destination_path = os.path.join(os.path.dirname(zip_path), destination_folder_name)

  # extract zip file
  extract_zip(zip_path, destination_path)

  # print destination folder path
  print(destination_path)

if __name__ == '__main__':
  main()
