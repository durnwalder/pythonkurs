def FaToCe (fahrin):
	celsiusout = 5./9 * (fahrin - 32) # conversion
	return(celsiusout)
lower = 0
upper = 300
step = 20

fahr = lower
while ( fahr < upper ): 
    
    print "Fahrenheit ", fahr," = Celsius ", FaToCe(fahr)
    fahr += step  # increment

# end of loop
