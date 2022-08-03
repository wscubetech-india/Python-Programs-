employees = ["john","david","peter","lisa","john"]
emp_id = ["emp1","emp4","emp3","emp2","emp5"]


for index,(emp,empid) in enumerate(zip(employees,emp_id)):
    print (index,emp,empid)


# for i in zip(employees,emp_id):
#     print (i)