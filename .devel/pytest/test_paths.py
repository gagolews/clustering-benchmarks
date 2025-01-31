import numpy as np
import genieclust
import clustbench
import os.path
import glob

# more tests in sphinx/weave!

def test_paths():
    path = "~/Projects/clustering-data-v1"
    path = os.path.expanduser(path)

    if os.path.exists(path):
        assert "wut" in clustbench.get_battery_names(path)
        assert "x1" in clustbench.get_dataset_names("wut", path)

        os.chdir(os.path.expanduser(path))
        assert "wut" in clustbench.get_battery_names()
        assert "x1" in clustbench.get_dataset_names("wut")

        assert "wut" in clustbench.get_battery_names(path)
        assert "x1" in clustbench.get_dataset_names("wut", path)

        assert clustbench.load_dataset("wut", "x2").data.flags["C_CONTIGUOUS"]

        assert len(clustbench.load_dataset("wut", "x2").labels) == 2

        assert len(clustbench.load_dataset("wut", "x2", url="https://github.com/gagolews/clustering-data-v1/raw/v1.1.0").labels) == 2


if __name__ == "__main__":
    test_paths()
