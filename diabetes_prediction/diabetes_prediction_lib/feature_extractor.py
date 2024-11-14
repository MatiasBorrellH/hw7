# %%
from abc import ABC, abstractmethod
import pandas as pd

class FeatureTransformer(ABC):
# Abstract base class for feature transformation
    @abstractmethod
    def transform(self, df):
        pass

class GenderBinaryTransformer(FeatureTransformer):
# Converts gender into binary (M/F)
    def transform(self, df, column_name='gender'):
        '''
        Converts gender into binary values (M:1/F:0).
        '''
        self.column_name = column_name
        df[self.column_name] = df[self.column_name].map({'M': 1, 'F': 0})
        return df

class EthnicityOneHotEncoder(FeatureTransformer):
    def transform(self, df, column_name='ethnicity'):
        '''
        Performs one hot encoding on the 'ethnicity' column
        '''
        return pd.get_dummies(df, column_name, drop_first=True)


