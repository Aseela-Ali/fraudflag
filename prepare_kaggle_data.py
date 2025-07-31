import pandas as pd

df = pd.read_csv("creditcard.csv")
from faker import Faker
import random
import datetime

fake = Faker()

# Keep only relevant columns
df = df[['Amount', 'Class']].copy()
df.rename(columns={'Amount': 'Order_Amount', 'Class': 'Is_Flagged'}, inplace=True)

# Add new columns
df['Order_ID'] = range(1, len(df)+1)
df['Customer_Name'] = [fake.name() for _ in range(len(df))]
df['Email'] = [fake.email() for _ in range(len(df))]
df['Order_Date'] = [fake.date_between(start_date='-90d', end_date='today') for _ in range(len(df))]
df['City'] = [fake.city() for _ in range(len(df))]
df['IP_Address'] = [fake.ipv4_public() for _ in range(len(df))]
df['Orders_Last_Month'] = [random.randint(0, 6) for _ in range(len(df))]
df = df[[
    'Order_ID', 'Customer_Name', 'Email', 'Order_Amount', 'Order_Date',
    'City', 'IP_Address', 'Orders_Last_Month', 'Is_Flagged'
]]
df.to_csv("fraudflag_from_kaggle.csv", index=False)
