#simple recursion example
def recursion(times):
    if times < 3:
        print times
        times+=1
        recursion(times)

recursion(0)