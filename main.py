import pandas as pd

COUNTRIES = ["Germany"]
raw = pd.read_excel("emdat_public_2023_09_04_query_uid-OqHvd3.xlsx")

# print(raw.keys())

df = raw[[
    "Country",
    "Geo Locations",

    "Start Year",
    "Start Month",
    "Start Day",
    "End Year",
    "End Month",
    "End Day",

    "Disaster Type",
    "Total Damages, Adjusted ('000 US$)",
    "Total Deaths",
    "Total Affected",
]]

df = df.rename(columns={
    "Total Damages, Adjusted ('000 US$)": "Total Damages",
}, errors="raise")


# now we select only those events we are interested in
df = df.loc[df["Start Year"] >= 2022]
df = df.loc[df["Country"].isin(COUNTRIES)]

print(df.head())
print(df.shape)
