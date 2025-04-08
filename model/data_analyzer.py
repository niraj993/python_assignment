import pandas as pd
import numpy as np
from model.data_cleaning import FuturesDataCleaner
from .data_exporter import ExcelExporter



class FuturesDataAnalyzer(FuturesDataCleaner):
    def __init__(self):
        super().__init__()
        dataframe: pd.DataFrame = self.convert_to_dataframe()
        self.df = dataframe.copy()
        self.add_mean_column()
        ExcelExporter().export(df=self.df)   


    def add_mean_column(self):
        self.df["High"] = pd.to_numeric(self.df["High"], errors="coerce")
        self.df["Low"] = pd.to_numeric(self.df["Low"], errors="coerce")
        self.df["Mean"] = self.df[["High", "Low"]].mean(axis=1)
        return self.df


    def get_largest_change_row(self):
        self.df["Change"] = pd.to_numeric(self.df["Change"].str.replace(",", ""), errors="coerce")
        max_change_row = self.df.loc[self.df["Change"].abs().idxmax()]
        return {
            "Contract Name": max_change_row["Contract Name"],
            "Last": max_change_row["Last"]
        }
