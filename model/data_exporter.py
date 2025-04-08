import pandas as pd

class ExcelExporter:
    def export(self, df: pd.DataFrame, file_name="futures_data.xlsx", sheet_name="Raw Data"):
        with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)


