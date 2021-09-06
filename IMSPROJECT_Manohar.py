#to open the json document
fd = open("/content/manu.json",'r')
r = fd.read()
fd.close()
import json
manu = json.loads(r)

#to get new prod_id,name,price,quantity
prod_id = str(input("Enter product id:"))
name = str(input("Enter name:"))
pr = int(input("Enter price:"))
qn = int(input("Enter quantity:"))

manu[prod_id] = {'name': name, 'pr': pr, 'qn': qn}

js = json.dumps(manu)

fd = open("/content/manu.json",'w')
fd.write(js)
fd.close()


#to open the updated document
import json

fd = open("/content/manu.json",'r')
r = fd.read()
fd.close()

manu = json.loads(r)

#to get prod_id and quantity from to buy
m_prod  = str(input("Enter the product_Id: "))
m_quant = int(input("Enter the quantity: "))

if manu[m_prod]['qn']<=0:
  print("Product is not available!")
elif m_quant>manu[m_prod]['qn']:
  print("Required quantity is not available")
else:
  print("Product: ", manu[m_prod]['name'])
  print("Price: ", manu[m_prod]['pr'])
  print("Billing Amount: ", manu[m_prod]['pr'] * m_quant)
  manu[m_prod]['qn'] = manu[m_prod]['qn'] - m_quant

#to update the file as per sales
js = json.dumps(manu)

fd = open("/content/manu.json",'w')
fd.write(js)
fd.close()

#To print the receipt
recepit={'prod' : m_prod, 'qn' : m_quant, 'amount': manu[m_prod]['pr'] * m_quant}
recepit