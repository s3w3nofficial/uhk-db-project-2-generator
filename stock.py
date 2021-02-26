class Stock:
    NUMBER_OF = 0

    def __init__(self, kontaktni_udaje, region) -> None:
        Stock.NUMBER_OF += 1
        self.id = Stock.NUMBER_OF
        self.kontaktni_udaje = kontaktni_udaje
        self.region = region

    def __str__(self):
        return f'INSERT INTO "DBREHAKVI1"."Sklad" ("SkladID", "kontaktniUdaje", "region") VALUES (\'{self.id}\', \'{self.kontaktni_udaje}\', \'{self.region}\');'