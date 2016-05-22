import os, sys
lib_path = os.path.abspath(os.path.join('..', 'Common'))
sys.path.append(lib_path)
import LibFunctions
list = LibFunctions.multiples_below_x_and_y(999, 3, 5)
total = 0
for i in list:
    total += i
print(total)