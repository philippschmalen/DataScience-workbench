from workbench import Time as t
from workbench import Lists as l

alist = [i for i in range(5)]
batched = l.list_batch(alist)
print(batched)
t.sleep_countdown(2, print_step=1)

