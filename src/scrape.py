from pathlib import Path
import requests as rq
import os.path as osp
import json 
import gzip


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


def save_station(bsave_dir, base_url, station: dict):

    station_name = station["station_name"]
    min_year = station["min_year"]
    max_year = station["max_year"]
    station_id = station["id"]

    save_dir = Path(
        osp.join(bsave_dir, station_name)
    )

    if not save_dir.exists(): save_dir.mkdir()

    try:
        for year in range(min_year, max_year):
            year = str(year)
            url = "/".join([base_url, year, "-".join([station_id, year]) + ".gz"]) 

            save_file(
                url=url , save_dir=save_dir, city_name=station_name, year=year
            )
    except:
        pass 


if __name__ == "__main__":

    config = json.load(open("./src/config.json", "r"))

    base_url = config["noaa_url"]
    bsave_dir = config["data_dir"]

    for station in config["stations"]:
        save_station(bsave_dir=bsave_dir, base_url=base_url, station=station)