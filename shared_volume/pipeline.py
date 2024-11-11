import subprocess as sp
import shlex as sh
from pathlib import Path


OUTPUT_DIR = Path("output/")

TMP_DIR = OUTPUT_DIR / "temp"


# sp.call(
#     sh.split(f"hdfs dfs -mkdir -p {OUTPUT_DIR}")
# )


# sp.call(
#     sh.split(
#         f"hadoop jar /shared_volume/jars/weather-hadoop-day.jar data/midelt/*.txt {TMP_DIR}/day"
#     )
# )

# sp.call(
#     sh.split(
#         f"hadoop jar /shared_volume/jars/weather-hadoop-month.jar {TMP_DIR}/day/part-r-00000 {TMP_DIR}/month"
#     )
# )

# sp.call(
#     sh.split(
#         f"hadoop jar /shared_volume/jars/weather-hadoop-year.jar {TMP_DIR}/month/part-r-00000 {TMP_DIR}/year"
#     )
# )

# sp.call(
#     sh.split(
#         f"hdfs dfs -rm {TMP_DIR}/*.csv"
#     )
# )

# sp.call(
#     sh.split(
#         f"hdfs dfs -mv {TMP_DIR}/day/part-r-00000 {TMP_DIR}/day.csv"
#     )
# )

# sp.call(
#     sh.split(
#         f"hdfs dfs -mv {TMP_DIR}/month/part-r-00000 {TMP_DIR}/month.csv"
#     )
# )

# sp.call(
#     sh.split(
#         f"hdfs dfs -mv {TMP_DIR}/year/part-r-00000 {TMP_DIR}/year.csv"
#     )
# )

# sp.call(
#     sh.split(
#         f"hdfs dfs -rm -r -f {TMP_DIR}/day/"
#     )
# )

# sp.call(
#     sh.split(
#         f"hdfs dfs -rm -r -f {TMP_DIR}/month/"
#     )
# )

# sp.call(
#     sh.split(
#         f"hdfs dfs -rm -r -f {TMP_DIR}/year/"
#     )
# )


sp.call(
    sh.split(
        f"mkdir /shared_volume/results/"
    )
)

sp.call(
    sh.split(
        f"rm -rf /shared_volume/results/*"
    )
)


sp.call(
    sh.split(
        f"mkdir /shared_volume/results/midelt/"
    )
)

sp.call(
    sh.split(
        f"hdfs dfs -copyToLocal {TMP_DIR}/*.csv /shared_volume/results/midelt/"
    )
)

sp.call(
    sh.split("hdfs dfs -rm -r -f {TMP_DIR}")
)
