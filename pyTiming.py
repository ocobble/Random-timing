from StringIO import StringIO
import urllib2
import sys
import time
#output = urllib2.urlopen("http://python-rng.appspot.com/")
#html = output.read()
#print(html)
#print(sys.argv[1])
'''
I need to take in the imput given in the format specified by the file on canvas:
    [region]_[zone]_[VM|app]_[Java|Python]@(the address of the website)

then return in the format:
    (the given IP address): [region]_[zone]_[VM|App]_[Java|Python]@(the website) time random_number

so I can rn through the given input until I hit and @, then take in the rest of the imput as a string and run the code
below on it. for the output, I need to give the entire output back, with the new information
'''
print("\n START: \n")
for i in range(1, len( sys.argv)):
    strlist = str.split(sys.argv[i], '@')
    start = time.time()
    if(strlist[1][:4] != "http"):
        strlist[1] = ("http://" + strlist[1])
    try:
        output = urllib2.urlopen(strlist[1],timeout =  5)
    except urllib2.URLError as e:
        print("got an error on " + strlist[1] + " of " + str(e.reason))
        continue
    html = output.read()
    end = time.time()
    number = ''.join(i for i in html if i.isdigit())
    formatStrings = str.split(strlist[0], "_")
    print(strlist[1] + " : " + formatStrings[0] + "_" + formatStrings[1] + "_" + formatStrings[2] + "_" + formatStrings[3] + "@" + strlist[1] + " " + str(end - start) + " " +  str(number))
    #print(sys.argv[i] + " returned a number " + str(html) +  " in " + str(end - start) + " seconds")
    #print(html)

print("\n FINISH \n")

