def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return round(amount + gst, 2)


def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    return round(amount + gst, 2)


def calculateFoodGST(e):
    gst = e * 7 / 100
    return round(e + gst, 2)


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return round(electronics + fashion + food, 2)


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return round(total - discount, 2)


# Sample test values
a = 100
b = 100
c = 100
d = 100
e = 100

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)
total = totalBill(a, b, c, d, e)
discount = round(total * 20 / 100, 2)
final_amount = calculateDiscountedBill(a, b, c, d, e)

print("Electronics after GST = {:.2f}".format(electronics))
print("Fashion after GST = {:.2f}".format(fashion))
print("Food after GST = {:.2f}".format(food))
print("Total after GST = {:.2f}".format(total))
print("20% Discount = {:.2f}".format(discount))
print("Final payable amount = {:.2f}".format(final_amount))