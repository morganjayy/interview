# create a python list of colors and assign to a variable named day of the week 
monday = ['green','yellow','green','brown','blue','pink','blue','yellow','orange','cream',
          'orange','red','white','blue','white','blue','blue','blue','green']

tuesday = ['arsh','brown','green','brown','blue','blue','blue','pink','pink','orange','orange',
           'red','white','blue','white','white','blue','blue','blue']

wednesday = ['green','yellow','green','brown','blue','pink','red','yellow','orange',
            'red','orange','red','blue','blue','white','blue','blue','white','white']

thursday = ['blue','blue','green','white','blue','brown','pink','yellow','orange','cream',
            'orange','red','white','blue','white','blue','blue','blue','green']

friday = ['green','white','green','brown','blue','blue','black','white','orange','red','red',
          'red','white','blue','white','blue','blue','blue','white']

# create varibles to take in each count of all colors worn by employees for the week but for now default to zero

count_of_green = 0
count_of_yellow = 0
count_of_brown = 0
count_of_blue = 0
count_of_pink = 0
count_of_orange = 0
count_of_cream = 0
count_of_red = 0
count_of_white = 0
count_of_arsh = 0
count_of_black = 0
uncaptured_color = 0
total_no_color = 11

# NOTE: Blew in Tuesday was changed to blue with assumption that the examiner wanted to write blue as no color named Blew exist

"""
Using a for loop to determine the exactly number of times each color was worn by an employee for each day of the week.
This will add to each count of colors.
"""

for color in monday:
    if color == 'green':
        count_of_green += 1
    elif color == 'yellow':
        count_of_yellow += 1
    elif color == 'brown':
        count_of_brown += 1
    elif color == 'blue':
        count_of_blue += 1
    elif color == 'pink':
        count_of_pink += 1
    elif color == 'orange':
        count_of_orange += 1
    elif color == 'cream':
        count_of_cream += 1
    elif color == 'red':
        count_of_red += 1
    elif color == 'white':
        count_of_white += 1
    elif color == 'arsh':
        count_of_arsh += 1
    elif color == 'black':
        count_of_black += 1
    else:
        uncaptured_color += 1

for color in tuesday:
    if color == 'green':
        count_of_green += 1
    elif color == 'yellow':
        count_of_yellow += 1
    elif color == 'brown':
        count_of_brown += 1
    elif color == 'blue':
        count_of_blue += 1
    elif color == 'pink':
        count_of_pink += 1
    elif color == 'orange':
        count_of_orange += 1
    elif color == 'cream':
        count_of_cream += 1
    elif color == 'red':
        count_of_red += 1
    elif color == 'white':
        count_of_white += 1
    elif color == 'arsh':
        count_of_arsh += 1
    elif color == 'black':
        count_of_black += 1
    else:
        uncaptured_color += 1

for color in wednesday:
    if color == 'green':
        count_of_green += 1
    elif color == 'yellow':
        count_of_yellow += 1
    elif color == 'brown':
        count_of_brown += 1
    elif color == 'blue':
        count_of_blue += 1
    elif color == 'pink':
        count_of_pink += 1
    elif color == 'orange':
        count_of_orange += 1
    elif color == 'cream':
        count_of_cream += 1
    elif color == 'red':
        count_of_red += 1
    elif color == 'white':
        count_of_white += 1
    elif color == 'arsh':
        count_of_arsh += 1
    elif color == 'black':
        count_of_black += 1
    else:
        uncaptured_color += 1

for color in thursday:
    if color == 'green':
        count_of_green += 1
    elif color == 'yellow':
        count_of_yellow += 1
    elif color == 'brown':
        count_of_brown += 1
    elif color == 'blue':
        count_of_blue += 1
    elif color == 'pink':
        count_of_pink += 1
    elif color == 'orange':
        count_of_orange += 1
    elif color == 'cream':
        count_of_cream += 1
    elif color == 'red':
        count_of_red += 1
    elif color == 'white':
        count_of_white += 1
    elif color == 'arsh':
        count_of_arsh += 1
    elif color == 'black':
        count_of_black += 1
    else:
        uncaptured_color += 1

for color in friday:
    if color == 'green':
        count_of_green += 1
    elif color == 'yellow':
        count_of_yellow += 1
    elif color == 'brown':
        count_of_brown += 1
    elif color == 'blue':
        count_of_blue += 1
    elif color == 'pink':
        count_of_pink += 1
    elif color == 'orange':
        count_of_orange += 1
    elif color == 'cream':
        count_of_cream += 1
    elif color == 'red':
        count_of_red += 1
    elif color == 'white':
        count_of_white += 1
    elif color == 'arsh':
        count_of_arsh += 1
    elif color == 'black':
        count_of_black += 1
    else:
        uncaptured_color += 1

# print variables to view numbers we captured so far

print('Green: ',count_of_green,'\nYellow: ',count_of_yellow,'\nBrown: ',count_of_brown,'\nBlue: ',count_of_blue,
      '\nPink: ',count_of_pink,'\nOrange: ',count_of_orange,'\nCream: ',count_of_cream,'\nRed: ',count_of_red,'\nWhite: ',count_of_white,
      '\nArsh: ',count_of_arsh,'\nBlack: ',count_of_black, '\nNone: ',uncaptured_color)

# QUESTION 1
"""
Sum up total appearance of all colors and divide by the total number of colors present, colors with that number will be the mean color
"""
total_no_color = 11
total_appearance_of_colors = count_of_green+count_of_yellow+count_of_brown+count_of_blue+count_of_pink+count_of_orange+count_of_cream+count_of_red+count_of_white+count_of_arsh+count_of_black
print(total_appearance_of_colors)
mean_appearance = total_appearance_of_colors/total_no_color
# round mean to an whole number to get exact figure without decimals
print("Mean number is: ", round(mean_appearance))
# mean_appearance = 9 Therefore, Mean color is Color RED and Color ORANGE as they both have the count of 9

# QUESTION 2

"""
Color BLUE is mostly worn throughout the week with a lead count of 31
"""

# QUESTION 3 

"""
Based on the order of occurence color ORANGE is the median color with total count of 9
"""

# QUESTION 4 

# import statistic python module 
import statistics

# use number of count of each color as data to be presented 
data = [10,5,6,31,5,9,2,9,16,1,1]

# statistics.variance function will automaticall calculate all required element 
print("Variance of colors: ",(statistics.variance(data)))

# QUESTION 5

"""
Divide possible times a red color can be chosen which is 9 by total number of appearance of all colors 
"""
total_appearance_of_colors = 95
count_of_red = 9
probability = count_of_red/total_appearance_of_colors
print("Probabillity that a red color is chosen: ", probability)


# QUESTION 9

def sum_fibonacci_sequence(n):
    if (n <= 0) :
        return 0
    fibonacci =[0] * (n+1)
    fibonacci[1] = 1
    
    sum = fibonacci[0] + fibonacci[1]

    for num in range(2,n+1) :
        fibonacci[num] = fibonacci[num-1] + fibonacci[num-2]
        sum = sum + fibonacci[num]
    
    return sum

print("Sum of first 50 fibonacci sequence: ", sum_fibonacci_sequence(50))
