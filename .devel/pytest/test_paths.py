import numpy as np
import genieclust
import clustbench
import os.path
import glob

# more tests in sphinx/weave!

def test_paths():
    path = "~/Projects/clustering-data-v1/"
    assert "wut" in clustbench.get_battery_names(path)
    assert "x1" in clustbench.get_dataset_names("wut", path)

    os.chdir(os.path.expanduser(path))
    assert "wut" in clustbench.get_battery_names()
    assert "x1" in clustbench.get_dataset_names("wut")

    assert "wut" in clustbench.get_battery_names("../clustering-data-v1/")
    assert "x1" in clustbench.get_dataset_names("wut", "../clustering-data-v1/")


if __name__ == "__main__":
    test_paths()
