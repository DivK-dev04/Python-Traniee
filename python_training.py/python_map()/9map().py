fahrenheit_temps = [32, 68, 104, 122]

def to_celsius(f):
    return (f - 32) * 5 / 9

celsius_temps = list(map(to_celsius, fahrenheit_temps))

print(celsius_temps)