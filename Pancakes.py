def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


#opens the f file
f = open('C:\\Users\\Kostas\\Downloads\\A-small-practice.in', 'r')
str = f.read()

#initialisation
T=""
i=0
#read num. of cases
while str[i]!='\n':
    T=T+str[i]
    i=i+1
    
#a list whith the num. of every case
cases=range(1, int(T)+1)

#initialisation
buf=''

#borders of pancakeRow
posStart=str.index('\n')
posEnd=str.index(' ')
#borders of K
KStart=posEnd
KEnd=find_nth(str,'\n',2)

#case counter initialisation
cc=1
#basic loop
for c in cases:

    #reads the pancakeRow string in every case
    pancakeRow=(str[posStart+1:posEnd] )
    
    #reads fliper's size in every case
    K=int(str[KStart+1:KEnd] )
    
    #main algorithm
    
    
    
    
    
    cc=cc+1
    #sets the new values-Borders of pancakeRow and K
    posStart=find_nth(str,'\n',cc)
    posEnd=find_nth(str,' ',cc)
    KStart=posEnd
    KEnd=find_nth(str,'\n',cc+1)
    
    #end of main algorithm
    
    print('Case #',c,': ', sep="")
    print(pancakeRow,K)

#end of basic loop
#closes the f file
f.close()


s="---+-++-"
kapa=3
L=len(s)
a = ['-','-','-','+','-','+','+','-']
pin=[]
i=0


while i<L:
    
    if(a[i]=='-'):
        j=0
        while(j<kapa and i<L):
            if(a[i]=='-'):
                pin.append('+')
                a[i]='+'
            else:pin.append('-')
            a[i]='-'
            i=i+1
            j=j+1
    else:
        pin.append('+')
        a[i]=='+'
        i=i+1
    print(a,'\n')

