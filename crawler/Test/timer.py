Python 3.4.0 |Anaconda 4.0.0 (64-bit)| (default, Mar 17 2014, 16:43:37) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import threading
>>> import time
>>> time.sleep(5)
>>> def timelaps(x,y):
	time.sleep(15)
	print('Time is gone')

	
>>> p1 = threading.Thread(target=timelaps, name="t1")
>>> p2 = threading.Thread(target=timelaps, name="t2")
>>> def timelaps():
	x = time.clock()
	time.sleep(15)
	print('Time is gone %s' % (time.clock()))

	
>>> timelaps()
Time is gone 14.993346613317106
>>> p1 = threading.Thread(target=timelaps, name="t1")
>>> p2 = threading.Thread(target=timelaps, name="t2")
>>> p1.start()
>>> p2.start()
>>> Time is gone 53.24282373787532
Time is gone 61.50271818688037
