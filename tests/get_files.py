import os 
from glob import glob

def get_files(filepath='./', name_contains="", absolute_path=True, subdirectories=True):
  """List all files of directory filepath with their absolute filepaths
  
  Args
    filepath:       string specifying folder
    name_containts: string with constraint on name, 
                    for example all python files "*.py"
    absolute_path:  return absolute paths of files or not
    subdirectories: include subdirectories or not  

  Return
    list: list with string elements of filenames 
  
  """

  all_files = []


  for (dirpath, dirnames, filenames) in os.walk(filepath):
      
    # filenames specified
    if name_contains: 
      all_files.extend(glob(os.path.join(dirpath,name_contains)))

    elif not name_contains:
      all_files.extend(filenames)
    
    # exclude subdirectories, break loop 
    if not subdirectories:
      break
    # otherwise continue with loop, walking down the directory

  # get absolute path
  if absolute_path: 
    all_files_absolute = [os.path.abspath(f) for f in all_files]
    return all_files_absolute

  else:
    return all_files


