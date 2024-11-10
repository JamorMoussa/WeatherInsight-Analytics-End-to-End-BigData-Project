from pathlib import Path
import requests as rq
import os.path as osp
import json 
import gzip


BASE_URL = "https://www1.ncdc.noaa.gov/pub/data/noaa" # 2023/601950-99999-2023.gz"
BASE_SAVE_DIR = "/home/moussa/Documents/S5/BigData/WeatherInsight-Analytics-End-to-End-BigData-Project/data"



def save_file(url, save_dir: str, city_name, year):

    save_file_path = Path(
        osp.join(save_dir, "-".join([city_name, year])) + ".txt",
    )

    if not save_file_path.exists():
        response = rq.get(url)

        if response.status_code == 200:
            decompressed_content = gzip.decompress(response.content)
            with open(save_file_path, "wb") as file:
                file.write(decompressed_content)


def save_station(station: dict):

    station_name = station["station_name"]
    min_year = station["min_year"]
    max_year = station["max_year"]
    station_id = station["id"]

    save_dir = Path(
        osp.join(BASE_SAVE_DIR, station_name)
    )

    if not save_dir.exists(): save_dir.mkdir()

    for year in range(min_year, max_year):
        year = str(year)
        url = "/".join([BASE_URL, year, "-".join([station_id, year]) + ".gz"]) 

        save_file(
            url=url , save_dir=save_dir, city_name=station_name, year=year
        )


if __name__ == "__main__":

    config = json.load(open("./src/config.json", "r"))

    for station in config["stations"]:
        save_station(station=station)