# Exercise 5.4 Fitbyte

[The Karvonen method](https://en.wikipedia.org/wiki/Heart_rate#Karvonen_method) allows you to calculate your target heart rate for physical exercise. The target heart rate is calculated with the formula `(maximum heart rate - resting heart rate) * (target heart rate percentage) + resting heart rate`, where the target heart rate is given as a percentage of the maximum heart rate.

For example, if a person has a maximum heart rate of `200`, a resting heart rate of `50`, and a target heart rate of `75%` of the maximum heart rate, the target heart rate should be about `((200-50) * (0.75) + 50)`, i.e., `162.5` beats per minute.

Create a class called `FitByte` in a file called `fit_byte.py`. Its constructor takes both an age and a resting heart rate as its parameters. The exercise assistant should provide a method target_heart_rate, which is passed a number of type double as a parameter that represents a percentage portion of the maximum heart rate. The proportion is given as a number between zero and one. The class should have:

- A constructor `def __init__(self, age, resting_heart_rate)`
- A method `def target_heart_rate(self,percentage_of_maximum)` that calculates and returns the target heart rate.

Use the `206.3 - (0.711 * age)` formula to calculate the maximum heart rate.

Use case:

```python
assistant = Fitbyte(30, 60)

percentage = 0.5

while (percentage < 1.0):
    target = assistant.target_heart_rate(percentage)
    print("Target " + str((percentage * 100)) + "% of maximum: " + str(target))
    percentage = percentage + 0.1
```

```plaintext
Target 50.0% of maximum: 122.48500000000001
Target 60.0% of maximum: 134.98200000000003
Target 70.0% of maximum: 147.479
Target 80.0% of maximum: 159,976
Target 89.99999999999999% of maximum: 172.473
Target 99.99999999999999% of maximum: 184.97000000000003
```
