import subprocess as sp
import shlex as sh
from pathlib import Path

import pandas as pd

SHARED_DIR = Path("./shared_volume")
OUT_DIR = SHARED_DIR / "outputs" / "midelt"

if not OUT_DIR.exists(): OUT_DIR.mkdir()

def get_date(x: str, mode=None):
    x = str(x)
    date = ""
    if mode == 0:
        date = "-".join([x[:4], x[4:6], x[6:8]])
    elif mode == 1:
        date = "-".join([x[:4], x[4:6], "01"])
    else: 
        date = "-".join([x[:4], "01", "01"])
    return pd.Timestamp(date)


# Load the CSV files
day_data = pd.read_csv("./shared_volume/results/midelt/day.csv", sep="\t")
month_data = pd.read_csv("./shared_volume/results/midelt/month.csv", sep="\t")
year_data = pd.read_csv("./shared_volume/results/midelt/year.csv", sep="\t")

# Rename columns and apply date transformation for month data
day_data.columns = ["date", "temp"]
month_data.columns = ["date", "temp"]
year_data.columns = ["date", "temp"]

day_data["date"] = day_data["date"].map(lambda x: get_date(x, mode=0))
month_data["date"] = month_data["date"].map(lambda x: get_date(x, mode=1))
year_data["date"] = year_data["date"].map(lambda x: get_date(x))

day_data["year"] = day_data["date"].map(lambda x: x.year)

max_data = day_data.groupby("year").max()
min_data = day_data.groupby("year").min()

day_data.to_csv(OUT_DIR / "day.csv")
month_data.to_csv(OUT_DIR / "month.csv")
year_data.to_csv(OUT_DIR / "year.csv")
max_data.to_csv(OUT_DIR / "max.csv")
min_data.to_csv(OUT_DIR / "min.csv")




