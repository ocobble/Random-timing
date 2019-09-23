from StringIO import StringIO
import urllib2
import sys
import time
#output = urllib2.urlopen("http://python-rng.appspot.com/")
#html = output.read()
#print(html)
#print(sys.argv[1])
for i in range(1, len( sys.argv)):
    start = time.time()
    output = urllib2.urlopen(sys.argv[i])
    html = output.read()
    end = time.time()
    print(sys.argv[i] + " returned a number in " + str(end - start) + " seconds")
    #print(html)

