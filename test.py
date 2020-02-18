lst = [2,4,3,55,32,11,23,9,17,15,1000,99,101,100,60,40,39,32,77,20,19,15,1000,20,20,20,20,1999987]

h = 0




def filter(list,level=2):
  def listt(list):
    list = list
    k = 0
    for i in range(0, len(list)):

        for j in range(k + 1, len(list)):

            if list[k] > list[j]:
                list[k], list[j] = list[j], list[k]
                k = j

        k = i

    return list
  for n in range(level):
      list1=listt(list)

  return list1
print("sorted", filter(lst))
