thelist = [1,2,3,4,5,6,7,8,9,8,7,7,6,5,3,2,1,0]

thelist.insert(0, len(thelist))

datasize = thelist[0]

i=j=1;

while j <= (datasize-1):

	if thelist[j] == thelist[j+1]:

            j+=1

            continue

	if i==j:

            i+=1

            j+=1

            continue

	thelist[i]=thelist[j]

	i+=1

        j+=1

                
