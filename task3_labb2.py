import errno
import os
def write_textfile(filename):
    try:
        f = open(filename,"w")
        text_input = raw_input("enter some text: ")
        try:
            f.write(text_input)
            f.close()
        except IOError as e:
            print e
    except IOError as ee:
        if ee.errno == errno.EACCES:  # 13
            print("cant write to file")
        else:
            print ee
            return False
    
def read_textfile(filename):
    f= open(filename,"r")
    print "texten i filen ar: " + f.read()
    f.close()

def permission_file(filename):
    if os.access(filename, os.F_OK) == True:
        print "file: " + filename + " exists"
    else:
        print "file: " + filename + " does not exist"
        
    if os.access(filename, os.R_OK) == True:
        print "Read permission: OK"
    else:
        print "Read permission: Not OK"

    if os.access(filename, os.W_OK) == True:
        print "Write permission: OK"
    else:
        print "Write permission: Not OK"

permission_file("hejsan1.py")
write_textfile("hejsan1.py")
permission_file("hejsan1.py")
read_textfile("hejsan1.py")

