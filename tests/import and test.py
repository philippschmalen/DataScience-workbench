from workbench import Time as t
from workbench import Lists as l
import workbench
 

int_list = [i for i in range(5)]
str_list = [s for s in "abcdefg"]

print(int_list)

batched = [i for i in batch(int_list)]
print(batched)
t.sleep_countdown(2, print_step=1)

