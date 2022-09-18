def return_10():
    return 10

def add(n_1, n_2):
    return n_1 + n_2

def subtract(n_1, n_2):
    return n_1 - n_2

def multiply(n_1, n_2):
    return n_1 * n_2

def divide(n_1, n_2):
    return n_1 / n_2    

def length_of_string(str):
    return len(str)

def join_string(str_1, str_2):
    return str_1 + str_2

def add_string_as_number(str_1, str_2):
    if type(int(str_1)) is int and type(int(str_2)) is int:
        return int(str_1) + int(str_2)

def number_to_full_month_name(month_number):
    
        if month_number == 1:
            return "January"
        elif month_number == 2:
            return "February"    
        elif month_number == 3:
            return "March"
        elif month_number == 4:
            return "April"
        elif month_number == 5:
            return "May"
        elif month_number == 6:
            return "June"
        elif month_number == 7:
            return "July"
        elif month_number == 8:
            return "August"
            
        elif month_number == 9:
            return "September"
        elif month_number == 10:
            return "October"
        elif month_number == 11:
            return "November"
        elif month_number == 12:
            return "December"
        


def number_to_short_month_name(number):
    
        if number == 1:
            return "Jan"
        elif number == 2:
            return "Feb"    
        elif number == 3:
            return "Mar"
        elif number == 4:
            return "Apr"
        elif number == 5:
            return "May"
        elif number == 6:
            return "Jun"
        elif number == 7:
            return "Jul"
        elif number == 8:
            return "Aug"
            
        elif number == 9:
            return "Sep"
        elif number == 10:
            return "Oct"
        elif number == 11:
            return "Nov"
        elif number == 12:
            return "Dec"
def volume_cube(side):
    return side * side * side         
def test_rev_str(str):
    #result in stringBiuld object
    obj = reversed(str)
    #turn obj into list
    obj_to_list = list(obj)
    #turn list into string
    reversed_str = "".join(obj_to_list)
    return reversed_str 

def far_to_cel(num):
   cel = (num - 32) * .5556
   return round(cel)