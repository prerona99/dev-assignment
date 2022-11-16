import csv
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec" ]
dathash = {}

for m in months:
    dathash[m] = {"total": 0}
# print(dathash)    

with open('files\dat.csv') as file_obj:
    heading = next(file_obj)
    reader_obj = csv.reader(file_obj)
    total_sales = 0
    for row in reader_obj:
        total_sales += int(row[-1])
        date = row[0].split("-") #date[0] = year, date[1] = month
        
        dathash[months[int(date[1]) - 1]]["total"] += int(row[-1])
        if dathash[months[int(date[1]) - 1]].get(row[1]) == None:
            dathash[months[int(date[1]) - 1]][row[1]] = {}
            dathash[months[int(date[1]) - 1]][row[1]]["Qty"] = int(row[3])
            dathash[months[int(date[1]) - 1]][row[1]]["Revenue"] = int(row[-1])
        else:
            dathash[months[int(date[1]) - 1]][row[1]]["Qty"] += int(row[3])
            dathash[months[int(date[1]) - 1]][row[1]]["Revenue"] += int(row[-1])
        
print("---------------------------------")
print("total sales :", total_sales )
print("---------------------------------")
print("Month wise sales total: \n")
popular = {}
revenue_max = {}
for m in months:
    if(dathash[m]['total'] > 0):
        print(m, " : ", dathash[m]['total'])
    
    qty = 0

    for k in dathash[m].keys():
        max_ = 0
        rev_ = 0
        # print(k)
        name_max_rev = ""
        name = ""
        if(k != "total"):
            # print(dathash[m])
            if dathash[m][k]["Qty"] > max_ and dathash[m]["total"] > 0:
                max_ = dathash[m][k]["Qty"]
                name = k
            if dathash[m][k]["Revenue"] > rev_ and dathash[m]["total"] > 0:
                rev_ = dathash[m][k]["Revenue"]
                name_max_rev = k
    if dathash[m]["total"] > 0:
        popular[m] = name
    if dathash[m]["total"] > 0:
        revenue_max[m] = name_max_rev

    
print("---------------------------------")
print("Most Popular item per month :\n")
print(popular)
print("---------------------------------")
print("Items generating max revenue per month :\n")
print(revenue_max)
