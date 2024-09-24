import pandas as pd
data_file_1 = pd.read_csv("zomato.csv")
data_file_1.head(3)
data_file_1.drop(data_file_1.columns[0],axis=1,inplace=True)
data_file_1.isnull().sum()
data_file_1["rate (out of 5)"] = data_file_1["rate (out of 5)"].fillna(0)
data_file_1.describe()
data_file_1.shape
data_file_1.info()

def Boolean_Conversion(x):
    if x == "No":
        return 0
    else:
        return 1

data_file_1["table booking"] = data_file_1["table booking"].apply(Boolean_Conversion)
data_file_1["online_order"] = data_file_1["online_order"].apply(Boolean_Conversion)
data_file_1['online_order'] = data_file_1['online_order'].astype(bool)
data_file_1['table booking'] = data_file_1['table booking'].astype(bool)
data_file_1.head(5)

data_file_1.drop(data_file_1.columns[-2],axis=1,inplace=True)
data_file_1.rename(columns={'num of ratings': 'Average Customer Per Week'}, inplace=True)
data_file_1.info()
data_file_1['Average income per Week'] = data_file_1["Average Customer Per Week"] * data_file_1["avg cost (two people)"]
data_file_1.to_csv('zomato_bangalore.csv', index=False)  # Set index=False to avoid saving the index
