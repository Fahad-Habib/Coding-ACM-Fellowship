def sort(data_list, first, last):
    if first < last:
        splitpoint = partition(data_list, first, last)

        sort(data_list, first, splitpoint-1)
        sort(data_list, splitpoint+1, last)
        

def partition(data_list, first, last):
    pivotvalue = data_list[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and data_list[leftmark] <= pivotvalue:
            leftmark += 1
        
        while data_list[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        
        if rightmark < leftmark:
            done = True
        else:
            data_list[leftmark], data_list[rightmark] = (data_list[rightmark], data_list[leftmark])

    data_list[first], data_list[rightmark] = (data_list[rightmark], data_list[first])

    return rightmark
