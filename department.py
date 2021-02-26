class Department:
    NUMBER_OF = 0

    def __init__(self, nazev) -> None:
        Department.NUMBER_OF += 1
        self.id = Department.NUMBER_OF
        self.nazev = nazev

    def __str__(self) -> str:
        return f'INSERT INTO "DBREHAKVI1"."Oddeleni" ("Nazev", "OddeleniID") VALUES (N\'{self.nazev}\', \'{self.id}\');'