class StockProduct:
    NUMBER_OF = 0

    def __init__(self, zbozi, mnozstvi, sklad, kapacita) -> None:
        StockProduct.NUMBER_OF += 1
        self.id = StockProduct.NUMBER_OF
        self.zbozi = zbozi
        self.mnozstvi = mnozstvi
        self.sklad = sklad
        self.kapacita = kapacita

    def __str__(self):
        return f'INSERT INTO "DBREHAKVI1"."SkladZbozi" ("zbozi", MNOZSTVI, "sklad", KAPACITA) VALUES (\'{int(self.zbozi)}\', \'{int(self.mnozstvi)}\', \'{int(self.sklad)}\', \'{int(self.kapacita)}\');'