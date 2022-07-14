# آریا توانا، تکلیف مبحث اعداد، سوال 1

from decimal import Decimal

radius = int(input("Please, Enter the radius: "))

circumference = float((radius * 2) * Decimal('3.14'))
area = float((radius * radius) * Decimal('3.14'))

print("Circumference", circumference, sep=" : ")
print("Area", area, sep=" : ")
