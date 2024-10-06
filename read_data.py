import pandas as pd
from numpy import float64

data = pd.read_csv("data/fruits_and_vegatables.csv", dtype={"copper": float64})
data.fillna(0)

units = pd.read_csv("data/units.csv")


def search(name: str) -> dict | None:
    result = data.loc[data["food"] == name]
    if result.empty:
        return None
    else:
        result = result.drop(["Source", "Comments", "Other Names"], axis=1)
        return result.loc[result.first_valid_index()].to_dict()


def get_units_as_names():
    return units.loc[0].to_dict()


def get_units_as_floats():
    NUMBER_TABLE = {
        "mg": 10**-3,
        "g": 1,
        "µg": 10**-6,
        "IU": 1,
        "kCal": 10**3,
    }
    return dict(
        (key, NUMBER_TABLE[value]) for key, value in get_units_as_names().items()
    )


print(search("apple"))
