# NBA-strelci-2017-18

Analiziral bom najboljših 259 strelcev v ligi NBA iz sezone 2017/2018.
Podatke bom zajel iz strani ESPN (http://www.espn.com/nba/statistics/player/_/stat/scoring-per-game/sort/avgPoints/year/2018/count/)

Za vsakega izmed najboljših 259 igralcev bom zajel povprečno število točk na tekmo, igralno pozicijo,  ekipo, število odigranih tekem v sezoni, povprečno število odigranih minut na tekmo, procent zadetih metov, procent zadetih metov za 3 točke, procent zadetih prostih petov in ptevilo metov ter število zadetih metov.
V analizi bom poskušal najti povezave med številom doseženih točk in igralno pozicijo, povezavo med igralno pozicijo in zadetimi meti za 2 oz. 3 točke, iz katere ekipe prihaja največ igralcev, ki doseželo največ točk, ali imajo igralci ki povprečno na tekmo odigrajo več minut slabši procent meta od tistih, ki imajo manjšo minutažo,... 
Hipoteze so, da imajo igralci iz zunanjih pozicij (G, PG, SG) boljši odstotek meta za 3 točke in boljši odstotek prostih metov. Povprečno na tekmo odigrajo več minut kot višji igralci (C, PF). Predvidevam da bodo imeli najslabši odstotek prostih metov višji igralci, vendar bodo zaradi bližine koša imeli tudi najboljši skupen odstotek meta iz igre. 


V datoteki "zajemalnik" je program ki iz interneta pobere 7 posameznih strani in jih shrani kot "stran_i". V datoteki "zdruzevanje" je program ki kodo vseh 7 strani zdruzi v eno datoteko z imenom "zdruzeno".

V datoteki "naredi_csv" je program ki naredi csv datoteko z imenom "podatki".

V datoteki "naredi_pravi_csv" je enak program kot "naredi_csv" le da v imena stolpcev ne doda znaka % ki povrzroča probleme pri analizi podatkov. 

V datoteki "podatki_pravi" so enaki podatki kot v datoteki "podatki" le da  imenih stolpcev ni znaka %.
