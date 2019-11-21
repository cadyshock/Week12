 #   Cady Shock
        #  ​CSCI 101 – Section A 
        #   Python Lab 1B
def fibi(x):
    n=0
    n1=1
    runs=0
    while runs < x:
        if runs == 1:
            lst=1
        else:
            lst=n+n1
            n=n1
            n1=lst
        print (lst)
        runs=runs+1

fibi(100)
