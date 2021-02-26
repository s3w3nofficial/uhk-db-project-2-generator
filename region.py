class Region:
    NUMBER_OF = 0

    def __init__(self, nazev) -> None:
        Region.NUMBER_OF += 1
        self.id = Region.NUMBER_OF
        self.nazev = nazev

    def __str__(self):
        return f'INSERT INTO "DBREHAKVI1"."Region" ("Nazev", "RegionID") VALUES (N\'{self.nazev}\', \'{self.id}\');'