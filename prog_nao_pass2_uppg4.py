kuber = [[4, 2, 3, 1],[2, 1, 0, 1],[0, 0, 0, 1]]
kuber = [[1,3],[4,5]]
kuber = [[4, 6, 2, 7, 8, 3, 5, 12, 9], [5, 7, 6, 2, 4, 3, 1, 4, 7], [3, 2, 6, 3, 9, 6, 5, 3, 8], [10, 25, 13, 7, 7, 0, 0, 1, 9], [4, 36, 12, 4, 18, 3, 5, 0, 0]]

antal_kuber = 0
antal_sidor_bredvid_annan_kub = 0
for i in range(len(kuber)):
    for j in range(len(kuber[i])):
        if kuber[i][j] != 0:
            antal_kuber += kuber[i][j]
            antal_sidor_bredvid_annan_kub += (kuber[i][j] - 1)*2
            if i < len(kuber)-1:
                if kuber[i+1][j] != 0:
                    if kuber[i+1][j] >= kuber[i][j]:
                        antal_sidor_bredvid_annan_kub += kuber[i][j]
                    else:
                        antal_sidor_bredvid_annan_kub += kuber[i+1][j]
            if i > 0:
                if kuber[i-1][j] != 0:
                    if kuber[i-1][j] >= kuber[i][j]:
                        antal_sidor_bredvid_annan_kub += kuber[i][j]
                    else:
                        antal_sidor_bredvid_annan_kub += kuber[i-1][j]
            if j < len(kuber[i])-1:
                if kuber[i][j+1] != 0:
                    if kuber[i][j+1] >= kuber[i][j]:
                        antal_sidor_bredvid_annan_kub += kuber[i][j]
                    else:
                        antal_sidor_bredvid_annan_kub += kuber[i][j+1]
            if j > 0:
                if kuber[i][j-1] != 0:
                    if kuber[i][j-1] >= kuber[i][j]:
                        antal_sidor_bredvid_annan_kub += kuber[i][j]
                    else:
                        antal_sidor_bredvid_annan_kub += kuber[i][j-1]


#print("Antal kuber: ", antal_kuber)
#print(antal_sidor_bredvid_annan_kub)
print("Begreänsningsarea: ", antal_kuber*6 - antal_sidor_bredvid_annan_kub)
