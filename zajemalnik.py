import urllib.request


stevilo = 1

for i in range (1 , 8):
    
    niz = str(i)
    link = "http://www.espn.com/nba/statistics/player/_/stat/scoring-per-game/sort/avgPoints/year/2018/count/" + str(stevilo)
    stevilo = 1 + 40*i
    urllib.request.urlretrieve(link, "stran" + niz + ".html")

