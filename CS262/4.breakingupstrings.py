def rsplit(string,pos=0):
    cache = string.find(" ", pos)
    if pos < len(string) and cache >=0:
        print cache
        pos = cache + 1
        rsplit(string,pos)

string = "Jose Mariz Melo Formiga Viana"
print "WHITE SPACES ON : "+string
rsplit(string)