def print_harvest_days(day):
    if day > 1:
        print_harvest_days(day - 1)
    print(f"Day {day}")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    print_harvest_days(days)
    print("Harvest time!")
