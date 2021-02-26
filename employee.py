class Employee:
    NUMBER_OF = 0

    def __init__(self, 
        datum_nastupu, 
        jmeno, 
        prijmeni, 
        plat, 
        poznamka, 
        procento_provize, 
        titul, 
        oddleni,
        kotaktni_udaje) -> None:
        Employee.NUMBER_OF += 1
        self.id = Employee.NUMBER_OF
        self.datum_nastupu = datum_nastupu
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.plat = plat
        self.poznamka = poznamka
        self.procento_provize = procento_provize
        self.titul = titul
        self.oddeleni = oddleni
        self.kontaktni_udaje = kotaktni_udaje

    def __str__(self) -> str:
        self.datum_nastupu = self.datum_nastupu.replace("('", "").replace(",)'", "")
        return (f'INSERT INTO "DBREHAKVI1"."Zamestnanec" ("Datumnastupu", "Jmeno", "Prijmeni", "Plat",'
        f'"Pripominky", "Procentoprovize", "Titul", "ZamestnanecID", "oddeleni", KONTAKTNIUDAJE) VALUES (TO_DATE(\'{self.datum_nastupu}\', \'YYYY-MM-DD HH24:MI:SS\'), '
        f'N\'{self.jmeno}\', N\'{self.prijmeni}\', \'{self.plat}\', \'{self.poznamka}\', \'{self.procento_provize}\', N\'{self.titul}\', \'{self.id}\', \'{self.oddeleni}\', \'{self.kontaktni_udaje}\');')