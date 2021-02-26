class ProductOrder:
    NUMBER_OF = 0

    def __init__(self, objednavka, mnozstvi, zbozi, cena) -> None:
        ProductOrder.NUMBER_OF += 1
        self.id = ProductOrder.NUMBER_OF
        self.objednavka = objednavka
        self.mnozstvi = mnozstvi
        self.zbozi = zbozi
        self.cena = cena

    def __str__(self):
        return f'INSERT INTO "DBREHAKVI1"."ZboziObjednavka" ("ObjednavkaID", MNOZSTVI, "ZboziID", CENA) VALUES (\'{int(self.objednavka)}\', \'{int(self.mnozstvi)}\', \'{int(self.zbozi)}\', \'{int(self.cena)}\');'