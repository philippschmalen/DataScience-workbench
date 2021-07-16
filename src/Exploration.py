
import pandas as pd
import numpy as np


def inspect_core_specifications(data, descriptives=False):
	"""Inspect data types, shape and descriptives

	:param data: pandas dataframe 
	:param descriptives: boolean, print descriptive statistics (default=False)
	:return: None
	"""

	# check if data is list of dataframes
	if isinstance(data, list):
		for d in data:
			print('-'*40)
			print(d.info())

			if descriptives:
				print('-'*40)
				print(round(d.describe(include='all', percentiles=[])))

	else:
		print('-'*40)
		print(data.info())

		if descriptives:
			print('-'*40)
			print(round(data.describe(include='all', percentiles=[])))
	print('*'*40)



# 
# Inspect and handle missings
# 

def inspect_missings(data, verbose=True):
	"""Inspect missings across rows and across columns

	Args 
		data: pandas dataframe 

	Returns
		:return : dataframe with info on column missings  
	"""
	if verbose:
		print("MISSINGS")
		print('-'*40)

	# check rows
	rows_all = data.shape[0]
	rows_nomiss = data.dropna().shape[0]

	rowmiss_count = rows_all - rows_nomiss
	rowmiss_share = rowmiss_count/rows_all*100

	if verbose:
		print("Any missing in any row: {}/{} ({} %)".format(rowmiss_count,rows_all, rowmiss_share))
		print()

	# check columns
	col_miss = [col for col in data.columns if data[col].isna().any()]
	# no missings for any column
	if not col_miss:
		print("No missings for any column.")
	else:
		# print share of missings for each column
		print("Return info on column missings")
		ds_colmiss = data.loc[:,col_miss].isna().sum()
		ds_colmiss_relative = data.loc[:,col_miss].isna().sum()/rows_all*100

		df_colmiss = pd.concat([ds_colmiss, ds_colmiss_relative], axis=1, keys=['missing_count', 'share'])\
						.sort_values("share", ascending=False)
		if verbose:
			print(df_colmiss)
			print('*'*40)

		return df_colmiss

def row_missing_count(df, top_n=None):
	"""Inspect absolute and relative missings across rows
	Args
		df: pandas DataFrame
		top_n: restrict output to top_n indices with most missings across columns 
	Return
		pandas dataframe with indices and their absolute and relative missings across columns

	"""

	df_colmiss_idx = df.T.isna().sum().sort_values(ascending=False)[:top_n]
	df_colmiss_idx_share = df_colmiss_idx/df.shape[1]

	return pd.concat([df_colmiss_idx, df_colmiss_idx_share], axis=1, keys=['missing_count', 'missing_share'])


def inspect_drop_rows_retain_columns(data, max_missing=3):
    """Dropping rows with many missings for certain columns 
	to keep columns
    :param data: dataframe
    :param max_missing: defines until which column-wise missing count should be iterated
    :return list with indices to drop, tuple of numpy arrays for plotting: Columns to keep vs. rows dropped (%)
    """
    # count missings per column, store in series
    count_column_missing = data.isna().sum(axis=0).sort_values(ascending=False)
    column_missing_names = count_column_missing.index

    # get array of missing count with unique values to loop over
    count_column_missing_unique = count_column_missing[count_column_missing >= 0].sort_values().unique()

    # define until which column-wise missing count should be iterated
    plot_x, plot_y = np.zeros(max_missing), np.zeros(max_missing)
    print("Trade off rows against columns\nDrop rows and modifiy original dataframe to keep more columns\n")
    print("i\tKeep Columns\tDrop Rows [%]\n"+'-'*40)

    drop_rows = []
    for arr_idx, i in enumerate(count_column_missing_unique[:max_missing]):
	select_columns = count_column_missing[count_column_missing <= i].index

	# return indices (=ticker) where the 1 missing per column occurs
	indices_many_missings = list(data.loc[data[select_columns].isnull().any(1),:].index)
	drop_rows.append(indices_many_missings)

	## compare modified vs. raw dropped missings
	# modified df 
	df_fin_mod = data.drop(indices_many_missings).dropna(axis=1)
	df_fin_nomiss = df_fin_mod
	# raw df
	df_raw = data.dropna(axis=1)

	### Benefits of dropping x rows
	## comparison of dropping and keeping
	# original 
	n_row_orig, n_col_orig = data.shape
	# modified & cleaned 
	n_row_mod, n_col_mod = df_fin_mod.shape
	# raw & cleaned
	n_row_nomod, n_col_nomod = df_fin_raw_nomiss.shape

	## STATISTICS
	# dropped rows to modify df (count and %)
	n_dropped_rows_mod = len(indices_many_missings)
	pct_dropped_rows_mod = round(n_dropped_rows_mod/n_row_orig*100)

	# dropped cols for modified df (count and %)
	n_dropped_cols_mod = n_col_orig - n_col_mod
	pct_dropped_cols_mod = round(n_dropped_cols_mod/n_col_orig*100)

	# dropped cols for non-modified df (count and %)
	n_dropped_cols_nomod = n_col_orig - n_col_nomod
	pct_dropped_cols_nomod = round(n_dropped_cols_nomod/n_col_orig*100)

	# plot dropped rows against retained columns 
	# (x=100-pct_dropped_rows_mod, y=pct_dropped_rows_mod)
	plot_x[arr_idx], plot_y[arr_idx] = 100-pct_dropped_cols_mod, pct_dropped_rows_mod
	print("{}\t{}\t\t{}".format(i, plot_x[arr_idx], plot_y[arr_idx])) 


    return drop_rows, plot_x, plot_y

def plot_histograms(df, column_list):
    """Show histograms for specified columns"""

    f, axes = plt.subplots(len(column_list), 1, figsize=(12,6*len(column_list)))
    f.suptitle("Distributions", fontsize=18)
    
    for row, column in enumerate(column_list):
        try:
            sns.histplot(df[column], ax=axes[row])
        
        # older seaborn versions do not have histplot
        # use distplot instead
        except AttributeError:
            logging.warning("Using distplot instead of histplot. Consider updating seaborn")
            sns.distplot(df[column], ax=axes[row])
        
def plot_relative_count(df, column_list):
    """Relative count for specified columns in ascending order"""
    
    f, axes = plt.subplots(len(column_list), 1, figsize=(12,6*len(column_list)))
    f.suptitle("Relative counts", fontsize=18)
    
    for plot_row, column in enumerate(column_list):
        relative_count = (df[column]
                          .value_counts(normalize=True)
                          .mul(100)
                          .reset_index()
                          .rename(columns={'index': column, column: '%'}))
        
        # with only 1 column, 'axes' is not a list and axes[plot_row] would return TypeError
        if len(column_list) == 1:
            sns.barplot(x=column, y="%", data=relative_count, order=relative_count[column], ax=axes)
        elif len(column_list) > 1:
            sns.barplot(x=column, y="%", data=relative_count, order=relative_count[column], ax=axes[plot_row])

def plot_correlation_heatmap(df):
    """Return correlation heatmap"""
    fig = plt.figure(figsize=(20,10)) 
    fig.suptitle("Relative counts", fontsize=18)
    
    sns.heatmap(df.corr(), annot=False, cmap='Dark2_r', linewidths = 2, square=True, annot_kws={"size":14})
    
