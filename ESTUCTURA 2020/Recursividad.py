def soyRecursivo(num):
    if num>1:
        num=num*soyRecursivo(num-1)
        return num
    else:
        return num

print(soyRecursivo(100))
