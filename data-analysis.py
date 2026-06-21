import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os



# Aufgabe 1




# Aufgabe 2





# Aufgabe 3







#Aufgabe 4
df = pd.read_csv("/drive/notebooks/fhwkw/daten/wien-bezirke.csv", header=1, sep=";", thousands='.', decimal=',')
df = pd.read_csv("/drive/notebooks/fhwkw/daten/vie-bez-inc-sex-2002f.csv", sep=";", skiprows=1)
district = "Innere Stadt"

district_code = 90100 

district_df = df[df["DISTRICT_CODE"] == district_code].copy()

district_df = district_df.sort_values("REF_YEAR")

district_df["TOTAL_AVERAGE_NETINCOME_RATIO"] = (
    district_df["AVERAGE_NETINCOME_TOTAL"] /
    district_df["AVERAGE_NETINCOME_FULLTIME_WHOLEYEAR_TOTAL"]
)

district_df["AVERAGE_NETINCOME_TOTAL_DIFF_PREV"] = (
    district_df["AVERAGE_NETINCOME_TOTAL"].diff().fillna(0)
)

result = district_df[
    [
        "REF_YEAR",
        "AVERAGE_NETINCOME_TOTAL",
        "AVERAGE_NETINCOME_FULLTIME_WHOLEYEAR_TOTAL",
        "TOTAL_AVERAGE_NETINCOME_RATIO",
        "AVERAGE_NETINCOME_TOTAL_DIFF_PREV"
    ]
]
result

income_df = pd.read_csv(
    "/drive/notebooks/fhwkw/daten/vie-bez-inc-sex-2002f.csv",
    sep=";",
    skiprows=1
)

districts_df = pd.read_csv(
    "/drive/notebooks/fhwkw/daten/wien-bezirke.csv",
    sep=";"
)

district_code = 90100

district_df = income_df[
    income_df["DISTRICT_CODE"] == district_code
].copy()

district_df = district_df.sort_values(
    by="REF_YEAR",
    ascending=True
)

district_df["TOTAL_AVERAGE_NETINCOME_RATIO"] = (
    district_df["AVERAGE_NETINCOME_TOTAL"]
    /
    district_df["AVERAGE_NETINCOME_FULLTIME_WHOLEYEAR_TOTAL"]
)

district_df["AVERAGE_NETINCOME_TOTAL_DIFF_PREV"] = (
    district_df["AVERAGE_NETINCOME_TOTAL"]
    .diff()
    .fillna(0)
)

result = district_df[
    [
        "REF_YEAR",
        "AVERAGE_NETINCOME_TOTAL",
        "AVERAGE_NETINCOME_FULLTIME_WHOLEYEAR_TOTAL",
        "TOTAL_AVERAGE_NETINCOME_RATIO",
        "AVERAGE_NETINCOME_TOTAL_DIFF_PREV"
    ]
]

result = district_df[
    [
        "REF_YEAR",
        "AVERAGE_NETINCOME_TOTAL",
        "AVERAGE_NETINCOME_FULLTIME_WHOLEYEAR_TOTAL",
        "TOTAL_AVERAGE_NETINCOME_RATIO",
        "AVERAGE_NETINCOME_TOTAL_DIFF_PREV"
    ]
].copy()

result["TOTAL_AVERAGE_NETINCOME_RATIO"] = (
    result["TOTAL_AVERAGE_NETINCOME_RATIO"].round(2)
)

result

result.to_csv("time_series_analysis.csv", sep=";", index=False)





# Bonus
district1 = income_df[income_df["DISTRICT_CODE"] == 90100].copy()  
district2 = income_df[income_df["DISTRICT_CODE"] == 91000].copy()  

district1 = district1.sort_values("REF_YEAR")
district2 = district2.sort_values("REF_YEAR")

plt.figure(figsize=(10, 6))

plt.plot(
    district1["REF_YEAR"],
    district1["AVERAGE_NETINCOME_TOTAL"],
    marker="o",
    label="Innere Stadt"
)

plt.plot(
    district2["REF_YEAR"],
    district2["AVERAGE_NETINCOME_TOTAL"],
    marker="o",
    label="Favoriten"
)

plt.title("Average Net Income Over Time")
plt.xlabel("Year")
plt.ylabel("Average Net Income")
plt.legend()
plt.grid(True)

plt.show()
