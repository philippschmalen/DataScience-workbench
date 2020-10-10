import os 
from glob import glob

def get_files(filepath='./', filetype=None):
  """List all files of directory filepath with their absolute filepaths
  
  Args
    filepath: string specifying folder

  Return
    list: string list elements with filenames 
  
  """
  all_files = []



  for root, dirs, files in os.walk(filepath):
    # filetype not specified 
    if not filetype:
      files = glob(filepath)
      print(files)

    # specified filetype
    else:
      files = glob(os.path.join(root,filetype))

    for f in files :
        all_files.append(os.path.abspath(f))

  return all_files


# for root, dirs, files in os.walk('./'):
#   print(root, dirs, files)



print(glob('*.py')) # TODO: does not work, 


for root, dirs, files in os.walk("./"):
  print("Root: ", root)
  print("Dirs: ", dirs)
  print("Files: ", files)

print(get_files())

