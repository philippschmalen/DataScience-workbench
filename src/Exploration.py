
import pandas as pd

class Exploration:
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
			

def inspect_missings(data):
	"""Inspect missings across rows and across columns
	
	:param data: pandas dataframe 
	:return: List with column names that contain missings 
	"""
	print("MISSINGS")
	print('-'*40)
	# check rows
	rows_all = data.shape[0]
	rows_nomiss = data.dropna().shape[0]

	rowmiss_count = rows_all - rows_nomiss
	rowmiss_share = rowmiss_count/rows_all*100

	print("Missings per row: {}/{} ({} %)".format(rowmiss_count,rows_all, rowmiss_share))
	print()
	
	# check columns
	col_miss = [col for col in data.columns if data[col].isna().any()]
	# no missings for any column
	if not col_miss:
		print("No missings for any column.")
	else:
		# print share of missings for each column
		print("Column missings")
		ds_colmiss = data.loc[:,col_miss].isna().sum()
		ds_colmiss_relative = data.loc[:,col_miss].isna().sum()/rows_all*100
		
		print(pd.concat([ds_colmiss, ds_colmiss_relative], axis=1, keys=['Count', 'Share (%)']))
			
	print('*'*40)
	
	return list(ds_colmiss.index)