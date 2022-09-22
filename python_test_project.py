#PYTHON BASIC DEVELOPER TEST

import random
import re
colors = {"green":10, "blue": 30, "yellow": 5, "brown": 6, "pink": 5, "orange": 9, "cream": 2, "red": 9, "white": 16, "arsh": 1, "blew": 1, "black": 1}
input = "0101101011101011011101000111"



#1 calculate the mean value
def themean(thecolors):
    sum_of_color = 0;
    for val in thecolors.values():
        sum_of_color += val

    total_color = len(colors)
    mean = sum_of_color / total_color
    return mean



#2 calculate the most worn color
def themode(thecolors):
    max_value = 0;
    for k, v in thecolors.items():
        if max_value < v:
            max_value = v
        else:
            max_value = max_value
        if v == max_value:
            most_color = k
    return most_color



#3 calculate the median value
def themedian(thecolors):
    list_of_colors = []
    for v in colors.values():
        list_of_colors.append(v)

    n = len(list_of_colors)
    list_of_colors.sort()

    if n % 2 == 0:
        median1 = list_of_colors[n//2 - 1]
        median2 = list_of_colors[n//2]
        median = (median1 + median2)/2
    else:
        median = list_of_colors[n//2]
    for k, v in colors.items():
        if v == round(median):
            medianColor = k
    return medianColor



#4 calculation of the variance
def thevariance(colors, mean):
    list_of_colors = []
    n = len(colors)
    for v in colors.values():
        list_of_colors.append(v)

    sum_of_deviations = 0
    for x in list_of_colors:
        x -= mean
        x *= x
        sum_of_deviations += x
    variance = sum_of_deviations / (n-1)
    return variance




#5 the probability that red will be chosen
def theprobability(thecolors):
    for k, v in thecolors.items():
        if k == "red":
            probability = v / len(colors)
    return probability



#7 using recursive search to get a particular output from an input
def get_output(input):
    check_input = re.compile(r'\d\d\d')
    output = ""
    for i in range(len(input)):
        if i == 26:
            break
        else:
            check = check_input.search(input[i] + input[i+1] + input[i+2])
            if check.group() == "111":
                output += '1'
            else:
                output += '0'
    return output



#8 generating 4 randoms number of 0's and 1's and convert the number to base 10:
def generate_number():
    generated_number = ""
    for x in range(4):
         random_number = round(random.randint(0,1))
         generated_number += str(random_number)
    return generated_number
def convert_binary_to_decimal(number):
    y = len(number)
    decimal_value = 0
    for x in range(y):
        a = int(number[x]) * (2**(y-(x+1)))
        decimal_value += a
    return decimal_value



#9 the sum of the first 50 fibonnacci sequence:
def fibonacci_sequence(x):
    sequence = []
    sum_of_sequence = 0
    for i in range(x):
        if i == 0:
            sequence.append(0)
        if i == 1:
            sequence.append(1)
        if i > 1:
            a = sequence[i-2] + sequence[i-1]
            sequence.append(a)
    for y in sequence:
        sum_of_sequence += y
    return sum_of_sequence



print("1) The mean of the colors is " + str(themean(colors)) + ".")
print("\n2) The most worn color is " + themode(colors) + ".")
print("\n3) The median color is " + themedian(colors) + ".")
print("\n4) The variance of the colors is " + str(thevariance(colors, themean(colors))) + ".")
print("\n5) The probability of red being chosen is " + str(theprobability(colors)) + ".")
print("\n7) The output from the recursive search of the input given is " + get_output(input) + ".")
print("\n8) The decimal value gotten from converting the random generated number is " +
      str(convert_binary_to_decimal(generate_number())) + ".")
print("\n9) The sum of the first 50 fibonacci sequence is " + str(fibonacci_sequence(50)) + ".")
