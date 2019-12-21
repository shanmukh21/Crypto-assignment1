a = [56211,43159,53947,19385]

for i in range(2):
    s=0
    old_s=1
    t=1
    old_t=0
    r=a[i+2]
    old_r=a[i]
    while(r!=0):
        q=old_r//r
        t1=r
        r=old_r-(q*r)
        old_r=t1
        t1=s
        s=old_s-(q*s)
        old_s=t1
        t1=t
        t=old_t-(q*t)
        old_t=t1
    print(old_t)