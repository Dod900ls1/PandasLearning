import pandas as pd


def create_series():
    myDataSet = {
        "Lexa": ["BMW", "Audi"],
        "Sasha": ["Honda", "Ferari"]
    }

    myDataSet0 = pd.Series(myDataSet)
    print(myDataSet0)
    print(myDataSet0[0])


def create_dataFrame():
    students = [{'Name': 'Alice',
                 'Class': 'Physics',
                 'Score': 85},
                {'Name': 'Jack',
                 'Class': 'Chemistry',
                 'Score': 82},
                {'Name': 'Helen',
                 'Class': 'Biology',
                 'Score': 90}]
    df = pd.DataFrame(students, index=["school1", "school2", "school3"])
    print(df)
    print(df.iloc[1])


def DataFrame_Experements():
    df1 = pd.read_csv("AAPL.csv")
    cols = list(df1.columns)
    cols = [i.lower().strip() for i in cols]
    df1.columns = cols
    print(df1.head())
    print("------------------------------------------------------------------------------")
    df2 = df1["volume"] > 75555200
    print(df1.where(df2).head())
    print("------------------------------------------------------------------------------")
    print(df1.where(df2).dropna().head())
    print("------------------------------------------------------------------------------")
    print(df1[(df1["volume"] > 70000000) & (df1["high"] > 60.4)].head())
    print("Nothing")


DataFrame_Experements()
