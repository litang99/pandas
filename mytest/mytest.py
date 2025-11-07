import numpy as np

import pandas as pd

# print("Pandas version:", pd.__version__)


def test():
    # Create a sample DataFrame
    df = pd.DataFrame(
        {
            "datet": [
                pd.Timestamp("2025-10-30 10:10:00").as_unit("ns"),
                pd.Timestamp("2025-10-26 01:12:13"),
            ],
            "consumption": [2.5, 5.0],
        }
    )

    print("DataFrame:")
    print(df)
    df.info()

    df["datetime"] = np.array(df.datet.dt.to_pydatetime())
    print("2")
    # df["datetime1"] = np.array(df.datet.dt.astype(datetime))

    print("\nDataFrame after converting datetime to numpy array of pydatetime:\n", df)
    df.info()


if __name__ == "__main__":
    test()
