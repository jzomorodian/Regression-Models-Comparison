from xml.dom import NotFoundErr
import pandas as pd
from os.path import exists
from src.Exception.FileNotSupported import FileNotSupported


class DataLoader:
    file_path: str
    df: pd.DataFrame

    def __init__(self, file_path) -> None:
        self.file_path = file_path
        if not exists(file_path):
            raise FileNotFoundError

        self.__read_data()

    def __read_data(self):
        if self.file_path[-4:-1].lower() == 'xls':
            self.df = pd.read_excel(self.file_path)
        elif self.file_path[-3:].lower() == 'csv':
            self.df = pd.read_csv(self.file_path)
        else:
            raise FileNotSupported

    def get_df(self):
        return self.df

    def get_np(self):
        return self.df.to_numpy()

    def remove_nans(self):
        init_len = len(self.df)
        nan_cols = self.df.columns[self.df.isna().any()].tolist()
        if len(nan_cols):
            df_nan_rows = self.df.isna()[nan_cols]
            df_nan_rows = df_nan_rows.any(axis=1)
            self.df = self.df[~df_nan_rows]

        self.df.reset_index(drop=True, inplace=True)

        print('After dropping NaN cells we have: Remained Len: {} | Init Len: {}'.format(
            len(self.df), init_len))
