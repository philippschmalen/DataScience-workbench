"""
Methods to create features based on available columns.
Example: Median split on a column
"""

def median_split(df, columns, label_high='high', label_low='low'):
    """Split numeric column into two distinct sets based on its median value"""
    
    assert isinstance(columns, list), f"Columns has to be a list. Instead it is {type(columns)}"
    assert isinstance(df, pd.DataFrame), f"df has to be a pd.DataFrame. Instead it is {type(df)}"
    
    # calculate medians
    median_series = df[columns].median()
    
    assert set(columns).issubset(median_series.index) , "Not all columns have numeric dtype to calculate .median()"
    
    for column in columns:
        # split on median into high and low category
        df[column] = df[column].mask(df[column] >= median_series[column], label_high)
        df[column] = df[column].mask(df[column] != label_high, label_low)
    
    return df
