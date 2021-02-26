class Order:
    NUMBER_OF = 0

    def __init__(self, datum_dodani, datum_objednani, typ_platby, zakaznik, zamestnanec, addressa_doruceni, addressa_fakturace) -> None:
        Order.NUMBER_OF += 1
        self.id = Order.NUMBER_OF
        self.datum_dodani = datum_dodani
        self.datum_objednani = datum_objednani
        self.typ_platby = typ_platby
        self.zakaznik = zakaznik
        self.zamestnanec = zamestnanec
        self.addressa_doruceni = addressa_doruceni
        self.addressa_fakturace = addressa_fakturace

    def __str__(self):
        return (f'INSERT INTO "DBREHAKVI1"."Objednavka" ("Datumdodani", "Datumobjednani", "Typplatby", "zakaznik", "ObjednavkaID", "ZamestnanecID", ADRESADORUCENI, ADRESAFAKTURACE) VALUES' 
        f'(TO_DATE(\'{self.datum_dodani}\', \'YYYY-MM-DD HH24:MI:SS\'), TO_DATE(\'{self.datum_objednani}\', \'YYYY-MM-DD HH24:MI:SS\'), N\'{self.typ_platby}\', \'{int(self.zakaznik)}\', \'{int(self.id)}\', \'{int(self.zamestnanec)}\', \'{int(self.addressa_doruceni)}\', \'{int(self.addressa_fakturace)}\');')