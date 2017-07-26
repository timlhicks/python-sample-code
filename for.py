# for i in range (1, 65):
#    print ("2 to the power of %s = %s" % (i, (2**i)))
#    print ("2 to the power of %s = (%04.03e) %s" % (i, (2**i), (2**i)))

n = 65
i = 1
while i < n:
#    print ("2 to the power of %s = %s" % (i, (2**i)))
    i += 1
    print ("While: 2 to the power of %s = (%04.03e) %s" % (i, (2**i), (2**i)))
