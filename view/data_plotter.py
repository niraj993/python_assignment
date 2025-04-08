import matplotlib.pyplot as plt
from model.data_analyzer import FuturesDataAnalyzer
import os

class FuturesDataPlotter(FuturesDataAnalyzer):
    def __init__(self):
        super().__init__()
        self.df = self.df
        self.plot_high_low_mean()

    def plot_high_low_mean(self):
        plot_df = self.df[["Contract Name", "High", "Low", "Mean"]].dropna()
        plot_df.set_index("Contract Name")[["High", "Low", "Mean"]].plot(
            kind='line', figsize=(12, 6), marker='o'
        )
        plt.xticks(rotation=45, ha='right')
        plt.title("High, Low, and Mean Comparison", fontsize=14)
        plt.xlabel("Contract Name")
        plt.ylabel("Price")
        plt.grid(True)
        plt.tight_layout()

        # Save the figure in the same directory as the script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(current_dir, "futures_comparison_plot.png")
        plt.savefig(save_path)

        print(f"Plot saved at: {save_path}")
        plt.show()
