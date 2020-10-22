
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
		
		Args 
			data: pandas dataframe 
			
		Returns
			:return : dataframe with info on column missings  
		"""
		print("MISSINGS")
		print('-'*40)
		# check rows
		rows_all = data.shape[0]
		rows_nomiss = data.dropna().shape[0]

		rowmiss_count = rows_all - rows_nomiss
		rowmiss_share = rowmiss_count/rows_all*100

		print("Any missing in any row: {}/{} ({} %)".format(rowmiss_count,rows_all, rowmiss_share))
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
			
			df_colmiss = pd.concat([ds_colmiss, ds_colmiss_relative], axis=1, keys=['missing_count', 'share'])\
							.sort_values("share", ascending=False)
			
			print(df_colmiss)
			return df_colmiss
			
		print('*'*40)

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


