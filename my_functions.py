# custom-functions/my_functions.py

# TODO: define temperature conversion function here

# TODO: define gradebook function here

def celsius_to_fahrenheit(celsius_temp):
    f_temp = 9/5 * celsius_temp + 32
    return  f_temp

def numeric_to_letter_grade(n):
    if n < 60:
        return "F"
    elif n < 70:
        return "D"
    elif n < 80:
        return "C"
    elif n < 90:
        return "B"
    else:
        return "A"



if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")

    print("--------------------")
    c = 0
    print("THE CELSIUS TEMP IS:", c, "DEGREES")
    f = celsius_to_fahrenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")

    print("--------------------")
    score = input("Please input a numeric letter grade (from 0 to 100):")
    
    score = float(score)
    #print("THE NUMERIC SCORE IS:", score)
    #grade = numeric_to_letter_grade(score)
    #print("THE LETTER-GRADE EQUIVALENT IS:", grade)

print("--------------------")
""" c = 0



print("THE CELSIUS TEMP IS:", c, "DEGREES")
f = celsius_to_fahrenheit(c)
print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES") """



# print("--------------------")
# score = 87.5

# def numeric_to_letter_grade(score):
#     if score > 90:
#         return "A"
#     elif 90 > score >= 80:
#         return "B"

print("THE NUMERIC SCORE IS:", score)
grade = numeric_to_letter_grade(score)
print("THE LETTER-GRADE EQUIVALENT IS:", grade)

""" 
x = input("Please input a number:")
print(x) """