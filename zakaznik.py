class Zakaznik:
    NUMBER_OF = 0

    def __init__(self, jmeno, kontaktni_udaje, region) -> None:
        Zakaznik.NUMBER_OF += 1
        self.id = Zakaznik.NUMBER_OF
        self.jmeno = jmeno
        self.kontaktni_udaje = kontaktni_udaje
        self.region = region

    def __str__(self):
        return f'INSERT INTO "DBREHAKVI1"."Zakaznik" (JMENO, "kontaktniUdaje", "region", "ZakaznikID") VALUES (N\'{self.jmeno}\', \'{int(self.kontaktni_udaje)}\', \'{int(self.region)}\', \'{int(self.id)}\');'