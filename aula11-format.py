a = 'AAAA'
b = 'BBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} a={nome1} c={nome3:.2f}'.format(a,b,c)
formato = string.format(nome1=a,nome2=b,nome3=c)

print(formato)
