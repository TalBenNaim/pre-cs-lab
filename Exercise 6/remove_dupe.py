def main():
    arr = [1,2,2,3]
    copy = arr[:] # so python doesn't redirect
    
    for num in arr:
        counter = 0
        for x in range(0,len(arr)):
            if num == arr[x]:
                counter += 1
            if counter > 1:
                copy.pop(x)
                counter = 0
    print(copy)
if __name__ == "__main__":
    main()