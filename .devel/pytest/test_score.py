import numpy as np
import genieclust
import clustbench

# more tests in sphinx/weave!

def test_score():
    n = 10000
    k = 5
    y1 = np.random.randint(1, k, n)
    y2 = np.random.randint(1, k, n)
    assert genieclust.compare_partitions.adjusted_asymmetric_accuracy(y1, y2) == clustbench.get_score(y1, y2)


if __name__ == "__main__":
    test_score()
