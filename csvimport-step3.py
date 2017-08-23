import csv

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

with open('good_dataset2.csv') as f:
    reader = csv.reader(f)
    my_list = list(reader)

print len(my_list)
print (my_list[105][5])

count = 0
pile = zerolistmaker(50)
taille = 0
while count <50:
	for i in range(len(my_list)):
		if my_list[i][5] == str(count) :
			my_list[i][11] = pile[count]
			my_list[i][12] = 10
			pile[count] += 1
			print pile[count]
			taille += 1
			print taille
	count +=1

print pile
print my_list[150]
print my_list[266]

#output in csv
# data = []
# for i in range(len(my_list)):
# 	for j in range(len(my_list[i])):
# 		data.append(my_list[i][j])
# out = csv.writer(open("myfile.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
# out.writerow(data)


with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(my_list)