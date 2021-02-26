class Product:
    NUMBER_OF = 0

    def __init__(self, cena, nazev, popis, obrazek) -> None:
        Product.NUMBER_OF += 1
        self.id = Product.NUMBER_OF
        self.cena = cena
        self.nazev = nazev
        self.popis = popis
        self.obrazek = obrazek

    def __str__(self):
        return f'INSERT INTO "DBREHAKVI1"."Zbozi" ("Cena", "Nazev", "Popis", OBRAZEK, "ZboziID") VALUES (\'{self.cena}\', N\'{self.nazev}\', N\'{self.popis}\', N\'{self.obrazek}\', \'{self.id}\');'