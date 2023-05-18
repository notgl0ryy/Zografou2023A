ch=input("(C)elcius to Fahrenehit or (F)ahrenheit to Celcius-> ")
if  ch.upper()=='C':
    tempc=input("Give temperature in Celcius: ")
    find_f=float(tempc)*1.8+32
    print(f"{tempc}-->{find_f}")
elif ch.upper()=='F':
    tempf=input("Give temperature in Fahrenheit: ")
    find_c=(float(tempf)-32)*5/9
    print(f"{tempf}-->{find_c}")
else:
    print("ERROR")