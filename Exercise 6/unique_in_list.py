def in_array(num, arr):
    for elm in arr:
        if elm == num:
            return True
    return False

def main():
    unique = []
    arr1 = [1,2]
    arr2 = [1,5,7,3]
    
    for elm1 in arr1:
        if in_array(elm1,arr2) == False and in_array(elm1, unique) == False:
            unique.append(elm1)

    for elm2 in arr2:
        if in_array(elm2,arr1) == False and in_array(elm2, unique) == False:
            unique.append(elm2)
    
    print(unique)

if __name__ == "__main__":
    main()