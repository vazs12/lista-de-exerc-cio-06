prim = int(input(" Digite o primeiro termo da PG: "))
razao = int(input(" Digite a razão da PG: "))
for i in range (1,6):
    print("a", i, "...", prim)
    prim = prim * razao

