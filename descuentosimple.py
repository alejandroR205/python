from doctest import OutputChecker


print("-----------------")
print("programa que calcula descuento con medio de pago en efectivo")
print("-------------------------")

#inputs
print("digite el valor de los zapatos:")
valorzapatos=float(input())
print("digite el medio de pago:")
mediodepago=input();

#process
#calcular el descuento

if(mediodepago=="efectivo"):
    descuento=(valorzapatos*10)/100
else:
    descuento=(valorzapatos*5)/100

#outputs 
print("tus zapatos valen:",valorzapatos-descuento)

