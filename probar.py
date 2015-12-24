import sys, time

for i in range(10):
	sys.stdout.write(' ' * 10 + '\r')
	sys.stdout.flush()
	print i
	sys.stdout.write('#' * i + '\r')
	sys.stdout.flush()
	time.sleep(0.5)