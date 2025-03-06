def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Masukkan suhu dalam derajat Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius} derajat Celsius sama dengan {fahrenheit:.2f} derajat Fahrenheit.")


