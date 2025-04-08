import pandas as pd
from controllers.futures_controller import MarketDataScraper
from configs import EXECUTION_TIME



class FuturesDataCleaner(MarketDataScraper):
    def __init__(self):
        super().__init__(execution_time=EXECUTION_TIME)
        self.initialize_browser()
        self.raw_text = self.fetch_market_data_text()
        self.shutdown_browser()


    def extract_headers_and_rows(self):
        lines = [line.strip() for line in self.raw_text.strip().split('\n') if line.strip()]
        headers = lines[:7]
        data = lines[8:]  
        rows = [data[i:i + 7] for i in range(0, len(data), 7)]
        return headers, rows


    def convert_to_dataframe(self):
        headers, rows = self.extract_headers_and_rows()
        return pd.DataFrame(rows, columns=headers)
