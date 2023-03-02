def main():
    arr = [10,11,13,14,15]
    follower = arr[0]

    for num in arr:
        if num != follower:
            lost_num = follower
            break 
        follower += 1

    print(lost_num)


if __name__ == "__main__":
    main()