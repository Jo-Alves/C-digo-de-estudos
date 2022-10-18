def removelines(value):
    return value.replace('\n','')

mystring = 'Minha string. \n\n\n oi'
# print("Atual string:",mystring)
print("Depois de excluir a nova linha:",removelines(mystring))