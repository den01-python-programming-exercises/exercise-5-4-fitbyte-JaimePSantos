class FitByte:
  def __init__(self,age,resting_heart_rate):
    self.age = age
    self.resting_heart_rate = resting_heart_rate

  def target_heart_rate(self,percentage_of_maximum):
    maximumHR = 206.3 - (0.711 * self.age)
    return (maximumHR - self.resting_heart_rate) * (percentage_of_maximum) + self.resting_heart_rate