def QuickPas(s, aL, aR):
    l, r=aL, aR
    mid = (s[l]+s[(l+r)/2]+s[r])/3
    while lmid:r-=1
        if l<=r:
            if s[l]>s[r]:
                s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
    if r>aL: QuickPas(s, aL, r)
    if l<aR: QuickPas(s, l, aR)