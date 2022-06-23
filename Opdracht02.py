with open("EerstePagina.html", "r") as fin:
    with open("EerstePaginaKopie.html", "w") as fin2:
        for line in fin:
            fin2.write(line)
