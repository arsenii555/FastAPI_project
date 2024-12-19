import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("data/kc_house_data.csv")

columns_to_drop = ['date', 'sqft_above', 'id', 'long']
data = data.drop(columns=columns_to_drop)

train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

test_data = test_data.drop(columns=['price'])

train_data.to_csv('train.csv', index=False)
test_data.to_csv('test.csv', index=False)

print("train.csv и test.csv были успешно созданы.")