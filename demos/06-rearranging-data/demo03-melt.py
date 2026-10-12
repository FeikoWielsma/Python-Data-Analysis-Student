import pandas as pd

trials = pd.read_csv("trials_01.csv")
wide = trials.pivot(index="treatment", columns="gender", values="response")
wide = wide.reset_index()
print(wide)

long = wide.melt(
    id_vars="treatment", value_vars=["F", "M"], var_name="gender", value_name="response"
)
print(long)
