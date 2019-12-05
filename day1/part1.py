fuel = 0

def fuel_amount(mass):
    return (mass // 3) - 2

def calculate_total_fuel(mass, total_fuel = 0):
    fuel = fuel_amount(mass)
    if fuel <= 0:
        return total_fuel
    else:
        total_fuel = total_fuel + fuel 
        return calculate_total_fuel(fuel, total_fuel)

with open("day1.txt") as _file:
    for line in _file:
        mass = int(line.strip())
        fuel = fuel + calculate_total_fuel(mass)

print(fuel)