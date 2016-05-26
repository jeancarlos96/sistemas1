x = int(input("ingrese el valor de la cena a comer : ")) ##INGRESO DE DATOS
def pago():  ## DEFINICION DE FUNCION
	a = (x * 12)/100  ## SACAR EL PORCENTAJE DEL TOTAL
	print (a) ## IMPRIMIMOS EL TANTO POR CIENTO 
	return x + a ## RETORNO DEL RESULTADO 
calculo = pago() ## LLAMANDO A LA FUNCION
print (calculo) ## IMPRIMIMOS EL RESULTADO FINAL
print (x)