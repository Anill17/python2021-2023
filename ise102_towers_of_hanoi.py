def hanoi(disk,start,middle,destination):
    if disk == 0:
        print("disk {} from {} to {}".format(disk,start,destination))
        return
    else:
        hanoi(disk-1,start,destination,middle)
        print("disk {} from {} to {}".format(disk,start,destination))
        hanoi(disk-1,middle,start,destination)

hanoi(2,"A","B","C")
