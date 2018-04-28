for i in range(16):
    bin = "{0:b}".format(i)
    print('%d %s' % ((list(bin)).count('1'), bin))
