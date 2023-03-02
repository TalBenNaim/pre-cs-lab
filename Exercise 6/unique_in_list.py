def in_array(num, arr):
    for elm in arr:
        if elm == arr:
            return True
    return False

def main():
    unique = []
    arr1 = [1,2]
    arr2 = [1,5,7,3]
    
    for elm2 in arr2:
        if in_array(elm2,arr1) == False and in_array(elm2, unique):
            unique.append[elm2]
        

if __name__ == "__main__":
    main()