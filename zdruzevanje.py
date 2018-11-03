filenames = ["stran1.html", "stran2.html", "stran3.html", "stran4.html", "stran5.html", "stran6.html", "stran7.html"]

with open("zdruzeno.html", 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
