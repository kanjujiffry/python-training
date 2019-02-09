tup1=(
    {"key1":"val1"},
    {"key2":"val2"}
)print(type(tup1))
print(tup1[0])
print()
print(type(tup1[0]))
tup1[0]]["key3"] = "val3"
tup1[0]="new string"

 #unpacking read and write files
 from sys import argv
 script, first_val,second_val,thrid_val =argv
 print ("first argument  is {}".format(first_val))
 print ("first argument  is {}".format(second_val))
 print ("first argument  is {}".format(thrid_val))
 print ("you are running the scirpt {}".format(script))
