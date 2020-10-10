# Import classes for convenient utility functions
from workbench import Lists as wl
from workbench import Time as wt
from workbench import Processing as wp


# list utilities
int_list = [i for i in range(20)]
str_list = [s for s in "abcdefg"]

int_list_batched = wl.batch(int_list)
str_list_corrected = wl.string_manual_correction(str_list)

# time utilities
print("Current timestamp {}".format(wt.timestamp_now()))
# wt.date_add_year()
sleep_countdown(5)

#