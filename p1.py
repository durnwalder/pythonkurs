def FaToCe (fahrin):
	celsiusout = 5./9 * (fahrin - 32) # conversion
	return(celsiusout)
def CeToFa (celsin):
	fahrout = celsin*9./5+32
	return(fahrout)
lower = 0
upper = 300
step = 20
cels = lower
fahr = lower
while ( fahr < upper ): 
    
	print "Fahrenheit ", fahr," = Celsius ", FaToCe(fahr)
	print "Celsius ", cels," = Fahrenheit ", CeToFa(cels)
	cels += step  # increment
	fahr += step

# end of loop
