import fractions as fc

Vb = Vr = Vj = Vg = Vo = Vv = Vm = fc.Fraction(0)

err_voulu = 0.001

it=0
err_max=0
while True: 
    Vb2 = max(Vg/2, Vv/2)
    Vr2 = max(Vv/2, Vo/2)
    Vj2 = max(Vo/2, Vg/2)
    Vg2 = max((3 + Vm/2), Vj, Vb)
    Vo2 = max((5 + Vm/2), Vj, Vr)
    Vv2 = max((7 + Vm/2), Vb, Vr)
    Vm2 = max(Vr/2, Vb/2, Vj/2)
    err_max= abs(Vb - Vb2)
    err_max= max(err_max, abs(Vr - Vr2))
    err_max= max(err_max, abs(Vj - Vj2))
    err_max= max(err_max, abs(Vg - Vg2))
    err_max= max(err_max, abs(Vo - Vo2))
    err_max= max(err_max, abs(Vv - Vv2))
    err_max= max(err_max, abs(Vm - Vm2))
    Vb = Vb2
    Vr = Vr2
    Vj = Vj2
    Vg = Vg2
    Vo = Vo2
    Vv = Vv2
    Vm = Vm2
    it+=1
    print("itteration: ",it)
    print("Vb = ",Vb)
    print("Vr = ",Vr)
    print("Vj = ",Vj)
    print("Vg = ",Vg)
    print("Vo = ",Vo)
    print("Vv = ",Vv)
    print("Vm = ",Vm)
    print("err_max = ",err_max)
    if (err_max < err_voulu):
        break
