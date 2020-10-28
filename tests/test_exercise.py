import pytest
import os

def test_exercise():
    os.chdir('src')

    from fit_byte import FitByte
    age = 25
    resting_heart_rate = 56
    maximum_heart_rate = 206.3 - (0.711 * age)
    target_heart_rate = (maximum_heart_rate - resting_heart_rate) * 100 + resting_heart_rate

    heart = FitByte(age,resting_heart_rate)

    assert heart.target_heart_rate(100) == target_heart_rate
