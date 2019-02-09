price = 24.95
print (price)
discount = 40
shipping = 3
addition_copy= .75
discount_price=price*discount/100
print(discount_price)
actual_price=price-discount_price
first_copy=actual_price+shipping
remaining_copy=(actual_price+addition_copy)*59
totalprice=first_copy+remaining_copy
print ('total price is %f euros' %totalprice)
