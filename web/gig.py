from bs4 import BeautifulSoup
import pandas as pd

with open('gigantti_laptop.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

containers = soup.find_all("div", class_="mini-product")
csv_file = "gigantti_laptop.csv"

file= open(csv_file, "w")
headers = "Product Name, Product Number,Product Price\n"
file.write(headers)


for cont in containers:
    product_number = cont.findChild('div',class_="product-number").text
    product_name =cont.findChild('span',class_="table-cell").text
    product_price=cont.findChild('div',class_="product-price").text

    file.write("{},{},{},{}\n".format(product_name.replace(",","."),
                                   product_number,
                                   product_price))

file.close()
print('Done')


# container_1 =containers[200]
# product_1_number = container_1.findChild('div',class_="product-number")
# product_1_number_1 =product_1_number.text
# prod_name =container_1.findChild('span',class_="table-cell").text
# print(prod price)


# f.write(headers)
#
# for container in containers:
#     product_name = container.findChild('a', class_="product-name")['title']
#
#     selling_price = container.findChild('div', class_="product-price").text
#
#     normal_price_tag = container.findChild(
#         'div', class_="mini-product-content").findChild('span', class_="sales-point")
#
#     if normal_price_tag:
#         try:
#             normal_price = int(normal_price_tag.text.split()[-1])
#         except ValueError:
#             normal_price = selling_price
#         print(normal_price)
#     else:
#         normal_price = selling_price
#
#     check_amout = container.findChild('div', class_="product-in-stock").span.span
#     if check_amout:
#         amount_in_stock = check_amout.text.split()[1]
#     else:
#         amount_in_stock = "Out of Stock"
#
#     f.write("{},{},{},{}\n".format(product_name.replace(',', '.'),
#                                    selling_price.replace(',', '.'),
#                                    normal_price,
#                                    amount_in_stock))
#
# f.close()
#
# col = ['Product', 'Selling Price', ' Normal Price', 'Stock', 'Extra']
# df = pd.read_csv("gigantti_puhelin.csv", names=col, sep=',', encoding='ISO-8859-1')
# df.to_html('h.html')
