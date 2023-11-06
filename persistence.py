import os

import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEASUREMENTS = os.path.join(BASE_DIR, "measurements.yml")


def read_measurements():
    """Read past measurements stored on disk as an .yml file"""

    result = []
    if os.path.exists(MEASUREMENTS):
        result = yaml.safe_load(open(MEASUREMENTS, "r"))
    return result


def write_measurements(measurements):
    """Write all measurements to disk as an .yml file"""

    with open(MEASUREMENTS, "w") as file:
        yaml.dump(measurements, file)
