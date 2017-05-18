def calculate_temp(num_clicks):
    
    clicks_dial = num_clicks % 50
    temp = clicks_dial + 40
    return temp
    


    




if __name__ == '__main__':

    clicks_str = input("By how many clicks has the dial been turned? ")
    clicks = int(clicks_str)
    print(calculate_temp(clicks))
