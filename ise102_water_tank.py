litre = 20
res = []
for i in range(litre//100+1):
    for j in range(litre//50+1):
        for k in range(litre//20+1):
            for l in range(litre//10+1):
                for r in range(litre//5+1):
                    for t in range(litre//2+1):
                        for v in range(litre//1+1):
                            for a in range(litre*2+1):
                                if i*100 + j*50 + k*20 + l*10 + r*5 + t*2 + v + a*0.5 == litre:
                                    res.append([i, j, k, l, r, t, v, a])


print(res)
print("finished")