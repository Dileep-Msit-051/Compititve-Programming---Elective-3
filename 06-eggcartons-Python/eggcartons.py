# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
    if((eggs>0)and(eggs<12)):
        return 1
    elif(eggs%12 == 0):
        carton = eggs/12
        return(round(carton))
    else:
        carton = eggs/12
        return(round(carton)+1)
