import re
i = 0
with open ("zdruzeno.html") as datoteka:
    vsebina = datoteka.read()

vzorec = r'/nba/player/(.*?)">(.*?)</a>, ([A-Z]{1,2})</td><td align="left">(.*?)</td><td >([0-9]{2})</td><td >(.*?)</td><td  class="sortcell">(.*?)</td><td >(.*?)</td><td >(.*?)</td><td >(.*?)</td><td >(.*?)</td><td >(.*?)</td><td >(.*?)</td>'

    
with open ("podatki_pravi.csv", "w") as csv:
    print ("ime,pozicija,ekipa,st_tekem,minute_na_tekmo,tocke,fgm-fga,fg,3pm-3pa,3p,ftm-fta,ft", file=csv)

    for ujemanje in re.finditer (vzorec, vsebina, re.DOTALL):
        print('{},{},{},{},{},{},{},{},{},{},{},{}'.format(ujemanje.group(2), ujemanje.group(3), ujemanje.group(4), ujemanje.group(5), ujemanje.group(6), ujemanje.group(7), ujemanje.group(8), ujemanje.group(9), ujemanje.group(10), ujemanje.group(11), ujemanje.group(12), ujemanje.group(13)), file=csv)
    
    
