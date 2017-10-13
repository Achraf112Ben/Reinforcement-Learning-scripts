va = vb = vc = vd =0

err_voulu = 0.001

it=0
err_max=0
while True: 
    qbc = 1+(vb+vc)/4
    qcd = (vc + vd)/4
    qbd = -0.5 + (vb + vd)/4
    va2 = max(qbc, qcd, qbd)
    vb2 = va/2 - 1
    vc2 = va/2 
    vd2 = va/2 + 1
    err_max= abs(va - va2)
    err_max= max(err_max, abs(vb - vb2))
    err_max= max(err_max, abs(vc - vc2))
    err_max= max(err_max, abs(vd - vd2))
    va=va2
    vb=vb2
    vc=vc2
    vd=vd2
    it+=1
    print("itteration: ",it)
    print("va = ",va)
    print("vb = ",vb)
    print("vc = ",vc)
    print("vd = ",vd)
    print("err_max = ",err_max)
    if (err_max < err_voulu):
        break
