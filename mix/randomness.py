import random
from collections import Counter


def rand5():
    return random.randint(1, 5)


def rand7():
    while True:
        i = 5 * (rand5() - 1) + rand5()
        if i <= 7:
            return i


def test_rand7():
    number = 100000
    expected_probability = 1/7
    allowed_deviation = 0.005
    c = Counter([rand7() for _ in range(number)])
    for element, count in c.items():
        current_probability = count/number
        current_deviation = abs(current_probability - expected_probability)
        assert current_deviation < allowed_deviation, \
          "Element %s distibution is wrong. Expeted %s, got %s" % (element, current_probability, expected_probability) # noqa
