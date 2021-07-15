"""
Methods that assist in loading data from source
"""

def map_dtypes(categorical=[], string=[], numeric=[]):
    """Create dtype mapper for pd.read_csv to parse columns as specified dtypes
    
    Args:
        categorical, string, numeric (list): Column names to parse as their specified type
    
    Usage:
        >>> dtype_mapper = map_dtypes(categorical_columns=['gender', 'mood'])
        >>> df = pd.read_csv(csv_file.csv, dtype=dtype_mapper)
    """
    
    dtype_categorical = dict(zip(categorical, ["category" for i in range(len(categorical))]))
    dtype_numeric = dict(zip(quant_columns, ["float" for i in range(len(numeric))]))
    dtype_str = dict(zip(string, ["str" for i in range(len(string))]))
    
    dtype_mapper = {**dtype_categorical, **dtype_numeric, **dtype_str}
    
    return dtype_mapper
