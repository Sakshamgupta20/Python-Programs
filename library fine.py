


from datetime import date
def libraryFine(d1, m1, y1, d2, m2, y2):
    if(int((date(y2,m2,d2)-date(y1,m1,d1)).days)>=0): return 0
    else:
        if y2!=y1:
            return abs((y2-y1)*10000)
        elif m2!=m1:
            return abs((m2-m1)*500)
        else:
            return abs((d2-d1)*15)
print(libraryFine(2,7,2015,1,2,2014))