a = [int(x) for x in open('17_2309.txt')]

krat11 = [x for x in a if x%11==0]
krat17 = [x for x in a if x%17==0]

if len(krat11)>len(krat17):
    print(len(krat11), min(krat11))
else:
    print(len(krat17), min(krat17))