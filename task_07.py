def celsius_to_fahrenheit(celsius):
    fahrenheit=9*celsius/5+32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return celsius
print(celsius_to_fahrenheit(90))
print(fahrenheit_to_celsius(194))
