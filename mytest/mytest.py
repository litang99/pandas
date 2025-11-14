import numpy as np

import pandas as pd

print("Pandas version:", pd.__version__)


def test_to_pydatetime():
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


def test_dtype_change():
    s = pd.Series([10, 20, 30], index=list("abc"), dtype=np.uint16)
    s1 = pd.Series([100, 200], index=list("ab"), dtype=np.uint8)
    print(s.dtype)
    print(s1.dtype)
    s.loc["a":"b"] = np.array([100, 200], dtype=np.uint8)
    print(s.dtype)


def test_multi_indexes():
    # wrong behavior whenever slice is used
    # My best guess is that ideally, the code that maps a (tuple of) key(s)
    # to one or more positions and the code that determines what will
    # the new index be should all be MultiIndex or _LocationIndexer
    # (not Series or DataFrame) code.
    df = pd.DataFrame(np.arange(20).reshape((4, 5))).set_index([0, 1, 2])
    print(df)
    # print(df.loc[(slice(None), 1,), :].index) # wrong output
    # print(df[3].loc[(slice(None), 1,)].index) # correct output
    # print(df.loc[(0,), :].index) # correct output
    print("== A ==")
    df.loc[(0, 1), :]  # correct output
    print("== B ==")
    df.loc[
        (
            slice(0, 5),
            6,
        ),
        :,
    ]  # wrong output
    print("== C ==")
    df[3].loc[
        (
            slice(None),
            1,
        )
    ]  # correct output


if __name__ == "__main__":
    # test_to_pydatetime()
    # test_dtype_change()
    test_multi_indexes()
