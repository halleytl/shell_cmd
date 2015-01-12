import sys
try:
    tmp1 = raw_input("q")
    print (tmp1,)
    tmp2 = raw_input("w")
    print (tmp2,)
    tmp3 = raw_input("w")
    print (tmp3,)
except EOFError, e:
    sys.stderr.write("missing answers\n")
    sys.exit(1)
