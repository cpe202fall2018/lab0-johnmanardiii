def weight_on_planets():
   # write your code here
   weight = float(input('What do you weigh on earth? '))  # Asks the user for their weight.
   mars = weight * .38  # Converts to weight on Mars.
   jupiter = weight * 2.34  # Converts to weight on Jupiter.
   print("\nOn Mars you would weigh", mars, "pounds.\n"\
         "On Jupiter you would weigh", jupiter, "pounds.", end='')
   
if __name__ == '__main__':
   weight_on_planets()