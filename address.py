class Address:
    NUMBER_OF = 0

    def __init__(self, mesto, psc, zeme) -> None:
        Address.NUMBER_OF += 1
        self.id = Address.NUMBER_OF
        self.mesto = mesto
        self.psc = psc
        self.zeme = zeme

    def __str__(self) -> str:
        return f'INSERT INTO "DBREHAKVI1"."Adresa" ("Mesto", "Psc", "Zeme", "AdresaID") VALUES (N\'{self.mesto}\', N\'{self.psc}\', N\'{self.zeme}\', \'{self.id}\');'