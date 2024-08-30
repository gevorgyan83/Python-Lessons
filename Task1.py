def product_sum(x,y):
    result = 1000
    if x * y <= result:
        return(f"{x} * {y} Is Not Greater Than {result}")
    else:
        return(x + y)

x = int(input("Print An Integer For X: "))
y = int(input("Print An Integer For Y: "))

print(product_sum(x,y))