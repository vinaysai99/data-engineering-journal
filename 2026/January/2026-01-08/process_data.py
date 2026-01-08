import pandas as pd

data = pd.read_csv("motel_logs.csv")
#print(data)

# Data Validation ( bill_amount > 50.0)
data = data[data["bill_amount"]>50]
print(data)

data["bill_amount"].describe() # We see o rows removed because if we see describe function results we can see min value is >50.0

#Adding new metric columns
data["taxes"] = data["bill_amount"]*0.1
data["total_charge"]= data["bill_amount"] + data["taxes"]
print(data)

data.to_json("clean_logs.json",orient="records",indent=4)
