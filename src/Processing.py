import pandas as pd
import os
from glob import glob

class Processing:

  def __init__(self):

  	""" Class with methods to handle data processing 
  	"""

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




  def make_csv(x, filename, data_dir, append=False, header=False, index=False):
    '''Merges features and labels and converts them into one csv file with labels in the first column
    
    	Input
       		x: Data features
       		file_name: Name of csv file, ex. 'train.csv'
       		data_dir: The directory where files will be saved
       	
       	Return
       		None: Create csv file as specified
    '''
    
    # create dir if nonexistent
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # make sure its a df
    x = pd.DataFrame(x)
    
    # export to csv
    if not append:
        x.to_csv(os.path.join(data_dir, filename), 
                                     header=header, 
                                     index=index)
    # append to existing
    else:
        x.to_csv(os.path.join(data_dir, filename),
                                     mode = 'a',
                                     header=header, 
                                     index=index)        
    
    # nothing is returned, but a print statement indicates that the function has run
    print('Path created: '+str(data_dir)+'/'+str(filename))


  def series_set_difference(ds1,ds2):
    """Obtain the set difference of two Series

    :param ds1: Pandas Series 1
    :param ds2: Pandas Series 2
    :return : set_difference
    """

    set_difference = pd.concat([ds1, ds2, ds2]).drop_duplicates(keep=False)

    return set_difference

  def series_duplicate(s, times=2, axis=0, reset_index=True):
    """Create a dataframe by repeating series multiple times

    :param s: pandas series
    :param times: how often the series should be repeated 
    :param axis: repeat over rows (axis=0) or over columns (=1)
    :param reset_index: reset index to consecutive integer

    :return : pandas DataFrame or Series with repeated Series from args 
    """
    df_dup = pd.concat([s] * times, axis=axis)

    if reset_index:
      df_dup = df_dup.reset_index(drop=True)

    return df_dup 