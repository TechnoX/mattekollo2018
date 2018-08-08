n = 7 #antal kunder före dig i kön, 1<=n<=100
m = 3 #antal kassor öppna, 1<=m<=10

tid_för_varje_kund = [2, 5, 6, 2, 4, 5, 3] #lista över antalet minuter det tar per kund

from numpy import zeros
kassor = zeros(m) #skapar en array (lista) där alla elementen är 0, med lika många element som antalet kassor

for i in range(n):
    kassor.sort() #sorterar så att kassan med minst total tid kommer först
    kassor[0] += tid_för_varje_kund[i] #lägger till en ny person i kassan som blir klar fortast
kassor.sort() #sorterar den en sista gång för att se vilken kö som är kortast när vi står först i kön
print("Väntetid: ",kassor[0], " minuter") # Vi tar kön med kortast tid av dessa.
