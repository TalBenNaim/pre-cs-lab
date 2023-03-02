def arr_have_dupes(arr):
    copy_arr = arr
    
    counter = 0

    for elm in arr:
        counter = 0
        for num in copy_arr:
            if elm == num:
                counter += 1
            if counter > 1: # we found more than one copy
                return True
    return False

def main():
    arr = [1,2,3,4,5]

    print(arr_have_dupes(arr))

if __name__ == "__main__":
    main()