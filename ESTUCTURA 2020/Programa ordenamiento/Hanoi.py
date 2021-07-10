def mover(altura,a,c,b):
    if altura>=1:
        mover(altura-1,a,b,c)
        print("mover : " + a + ":"+c)
        mover(altura-1,b,c,a)

mover(4, "Torre1","Torre3","Torre2")