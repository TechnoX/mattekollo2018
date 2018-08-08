tal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for s in tal[1:]:
    tal_e = tal[:]; del tal_e[tal_e.index(s)]
    for e in tal_e[:]:
        tal_n = tal_e[:]; del tal_n[tal_n.index(e)]
        for n in tal_n[:]:
            tal_d = tal_n[:]; del tal_d[tal_d.index(n)]
            for d in tal_d[:]:
                tal_m = tal_d[:]; del tal_m[tal_m.index(d)]
                for m in tal_m[:]:
                    if m != '0':
                        tal_o = tal_m[:]; del tal_o[tal_o.index(m)]
                        for o in tal_o[:]:
                            tal_r = tal_o[:]; del tal_r[tal_r.index(o)]
                            for r in tal_r[:]:
                                tal_y = tal_r[:]; del tal_y[tal_y.index(r)]
                                for y in tal_y[:]:
                                    send = int(s+e+n+d)
                                    more = int(m+o+r+e)
                                    money = int(m+o+n+e+y)
                                    if (send + more) == money:
                                        #print('s = ', s, ', e = ', e, ', n = ', n, ', d = ', d, ', m = ', m, ', o = ', o, ', r = ', r, ', y = ', y)
                                        print("send = ", send, " more = ", more, ", money = ", money)
                                    
                                    
                                
