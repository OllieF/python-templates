import json
from typing import Dict, Any
import os
import requests
from dotenv import load_dotenv
import logging

logging_fp = os.path.join(".", "log", "log.log")

logging.basicConfig(filename=logging_fp, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

load_dotenv()


def get_data(id: int) -> Dict[str, Any]:
    res = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
    return res.json()


def log_info(log_data: Any):
    logging.info(log_data)


def run_get_data():
    min_id = int(os.getenv("MIN_ID"))
    max_id = int(os.getenv("MAX_ID"))
    for i in range(min_id, max_id + 1):
        data = get_data(i)
        log_info(data)


if __name__ == "__main__":
    run_get_data()
