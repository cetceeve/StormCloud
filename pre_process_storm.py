import pandas as pd

OUTAGE_COUNTRIES = ["Germany"]
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
# df = df.loc[df["Start Year"] >= 2022]
# df = df.loc[df["Country"].isin(COUNTRIES)]

# format dates
df = df.dropna(subset=["Start Year", "Start Month", "Start Day", "End Year", "End Month", "End Day"])
df["Start Date"] = df.apply(lambda row : f"{int(row['Start Year'])}-{int(row['Start Month'])}-{int(row['Start Day'])}", axis=1)
df["End Date"] = df.apply(lambda row : f"{int(row['End Year'])}-{int(row['End Month'])}-{int(row['End Day'])}", axis=1)
df["Start Date"] = pd.to_datetime(df["Start Date"])
df["End Date"] = pd.to_datetime(df["End Date"])
# duplicating each row over it's date range
df = df.assign(date=lambda dfa: dfa.apply(lambda r: pd.date_range(r["Start Date"], r["End Date"]), axis=1)).explode("date")

# create full timeseries x countries and join with disaster events
dates = pd.DataFrame({"date": pd.date_range(start="2022-09-15", end="2023-09-19", freq="D")})
countries = df["Country"].drop_duplicates()
dates_countries = dates.merge(countries, how='cross')
df = dates_countries.merge(df, on=['date', "Country"], how='left')


# final selection of columns to write
df = df[[
    "date",
    "Country",
    "Start Date",
    "End Date",
    "Geo Locations",
    "Disaster Type",
    "Total Damages",
    "Total Deaths",
    "Total Affected",
]]

print(df.head())
print(df.shape)
df.to_csv("storms_pre_processed.csv")
