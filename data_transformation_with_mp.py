import pandas as pd
import multiprocessing as mp

"""
CPU Intensive Tasks / Heavy Transformation Or Aggregation
"""
class DataTransformationWithMP:

    @staticmethod
    def setup():
        df = pd.DataFrame({"group": ["A"] * 500000 + ["B"] * 500000, "value": range(1, 1000001)})
        grouped_data = {name: group for name, group in df.groupby("group")}
        return grouped_data

    # Function to compute mean
    @staticmethod
    def compute_mean(group_df):
        return group_df["value"].mean()


if __name__ == "__main__":
    dt = DataTransformationWithMP()
    grouped_data = dt.setup()

    with mp.Pool(mp.cpu_count()) as pool:
        results = pool.map(dt.compute_mean, grouped_data.values())  # Only pass DataFrames

    print(results)
