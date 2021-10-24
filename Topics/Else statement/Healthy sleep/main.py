A = int(input())
B = int(input())
H = int(input())
if H >= A:
    if H <= B:
        print("Normal")
    else:
        print("Excess")
else:
    print("Deficiency")
