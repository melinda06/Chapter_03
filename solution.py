def calculate_temp(num_clicks):
# TODO calculate the temperature (use the variable name of temp)
    print(num_clicks)
    return temp

if __name__ == '__main__':
    clicks_str = input("By how many clicks has the dial been turned? ")
    clicks = int(clicks_str)
    print(calculate_temp(clicks))
