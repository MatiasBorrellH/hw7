import pandas as pd

class NaNRemover:
    def __init__(self,columns_with_nan = ["age", "gender", "ethnicity"]):
        self.columns_with_nan = columns_with_nan
    # Constructor that initializes the NaNRemover class with a list of columns we want to treat
    # Takes as argumant a list of columns from which we want to remove rows with NaN values.
        '''
        :Param: a list of columns from which we want to remove NaN values columns "age", "gender", "ethnicity" by default.
        '''
    def remove_nan(self, df):
        '''
        Removes rows with NaN values in specific columns.
        
        :param: DataFrame to clean.
        
        Return: Cleaned DataFrame with rows removed.
        '''
        return df.dropna(subset=self.columns_with_nan)

class NaNFiller:
    def __init__(self, columns_to_fill = ['height', 'weight']):
    # Constructor that initializes the NaNFiller class with columns to fill NaN values with the mean
        '''
        :Param: a list of columns from which we want to fill NaN values with the mean columns 'height', 'weight' by default.
        '''
        self.columns_to_fill = columns_to_fill
    
    def fill_nan(self, df):
        '''
        Fills NaN values in specific columns with the mean.
        
        :param: DataFrame to fill NaN values in.
        
        Returns a DataFrame with NaN values filled with the mean.
        '''
        for column in self.columns_to_fill:
            df[column].fillna(df[column].mean(), inplace=True)
        return df


