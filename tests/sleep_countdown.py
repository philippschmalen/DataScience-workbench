import time
import sys

def sleep_countdown(duration, steps=1):
	"""Sleep that prints a countdown in specified steps

	Input
		duration: int for seconds of sleep duration
		steps: in which steps the countdown is printed

	Return
		None: sys.stdout output in console

	"""

	sys.stdout.write("\r Seconds remaining:")

	for remaining in range(duration, 0, -1):
		# display only steps
		if remaining % steps == 0:
		    sys.stdout.write("\r")
		    sys.stdout.write("{:2d}".format(remaining))
		    sys.stdout.flush()

		time.sleep(1)

	sys.stdout.write("\r Complete!\n")


sleep_countdown(5, steps=2)