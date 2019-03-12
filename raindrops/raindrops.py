def raindrops(number):
    # gameplan: check if number can be divided by 3, 5, 7
    # use modulo to check
    # edge case: number = 0
    # check if not int?
    no_factor_found = True
    result = ""
    if(number>0 and number % 3 == 0):
        result = "Pling"
        no_factor_found = False
    if(number>0 and number % 5 == 0):
        result += "Plang"
        no_factor_found = False
    if(number>0 and number % 7 == 0):
        result += "Plong"
        no_factor_found = False
    if(no_factor_found):
        result = str(number)
    return result
