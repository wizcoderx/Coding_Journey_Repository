'''
What parameters should be sent to the `range` constructor, to produce a range with values `8`, `6`, `4`, `2`, `0`, `-2`, `-4`, `-6`, `-8`?
'''
listx= []
for i in range(8,-10,-2):
    listx.append(i)

result_string = ",".join(map(str,listx))
print(result_string)