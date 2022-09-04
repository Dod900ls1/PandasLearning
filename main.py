import pandas as pd


myDataSet = {
    "Lexa": ["BMW", "Audi"],
    "Sasha": ["Honda", "Ferari"]
}

myDataSet0 = pd.Series(myDataSet)
print(myDataSet0)
print(myDataSet0[0])

