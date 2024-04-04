import pandas as pd

data = pd.read_csv("qm9.csv")

data.sample(n=20000, random_state=31).to_csv("qm9_sample.csv", index=False)