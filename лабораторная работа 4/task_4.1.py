# TODO решите задачу
import json


def task() -> float:
    with open("input.json", "r") as f:
        data = json.load(f)
    sum_ = 0
    for item in data:
        sum_ += item["score"] * item["weight"]
    return round(sum_, 3)

print(task())
