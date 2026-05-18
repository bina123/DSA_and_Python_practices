def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit"""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius"""
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    """Convert Celsius to Kelvin"""
    return c + 273.15

def kelvin_to_celsius(k):
    """Convert Kelvin to Celsius"""
    return k - 273.15

def convert_temperature(value, from_unit, to_unit):
    """
    Universal temperature converter
    Units: 'C', 'F', 'K'
    """
    # First convert to Celsius as intermediate
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == 'K':
        celsius = kelvin_to_celsius(value)
    
    # Then convert from Celsius to target
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return celsius_to_fahrenheit(celsius)
    elif to_unit == 'K':
        return celsius_to_kelvin(celsius)

# Test
print(convert_temperature(100, 'C', 'F'))  # 212.0
print(convert_temperature(32, 'F', 'C'))   # 0.0
print(convert_temperature(273.15, 'K', 'C'))  # 0.0