for A in range(10):
    for B in range(10):
        if B==A: continue
        for C in range(10):
            if C==A or C==B: continue
            for D in range(10):
                if D==A or D==B or D==C: continue
                for E in range(10):
                    if E==A or E==B or E==C or E==D: continue
                    for F in range(10):
                        if F==A or F==B or F==C or F==D or F==E: continue
                        for G in range(10):
                            if G==A or G==B or G==C or G==D or G==E or G==F: continue
                            for H in range(10):
                                if H==A or H==B or H==C or H==D or H==E or H==F or H==G: continue
                                print(A,B,C,D,E,F,G,H)
                                print("Barn A, vänster ?", sum([]))
                                print("Barn A, höger ?",   sum([B>A, C>A, D>A, E>A, F>A, G>A, H>A]))
                                print("Barn B, vänster ?", sum([A>B]))
                                print("Barn B, höger ?",   sum([C>B, D>B, E>B, F>B, G>B, H>B]))
                                print("Barn C, vänster ?", sum([A>C, B>C]))
                                print("Barn C, höger ?",   sum([D>C, E>C, F>C, G>C, H>C]))
                                print("Barn D, vänster ?", sum([A>D, B>D, C>D]))
                                print("Barn D, höger ?",   sum([E>D, F>D, G>D, H>D]))
                                print("Barn E, vänster ?", sum([A>E, B>E, C>E, D>E]))
                                print("Barn E, höger ?",   sum([F>E, G>E, H>E]))
                                print("Barn F, vänster ?", sum([A>F, B>F, C>F, D>F, E>F]))
                                print("Barn F, höger ?",   sum([G>F, H>F]))
                                print("Barn G, vänster ?", sum([A>G, B>G, C>G, D>G, E>G, F>G]))
                                print("Barn G, höger ?",   sum([H>G]))
                                print("Barn H, vänster ?", sum([A>H, B>H, C>H, D>H, E>H, F>H, G>H]))
                                print("Barn H, höger ? ",  sum([]))
                                
                                

