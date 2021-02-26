class ContactInfo:
    NUMBER_OF = 0

    def __init__(self, email, fax, telefoni_cislo, zamestnanec_id, adresa) -> None:
        ContactInfo.NUMBER_OF += 1
        self.id = ContactInfo.NUMBER_OF
        self.email = email
        self.fax = fax
        self.telefoni_cislo = telefoni_cislo
        self.zamestnanec_id = zamestnanec_id
        self.adresa = adresa

    def __str__(self) -> str:
        return (f'INSERT INTO "DBREHAKVI1"."Kontaktniudaje" ("Email", "Fax", "Telefonicislo", "KontaktniudajeID", "ZamestnanecID", ADRESA)'
            f'VALUES (N\'{self.email}\', N\'{self.fax}\', N\'{self.telefoni_cislo}\', \'{self.id}\', \'{self.zamestnanec_id}\', \'{self.adresa}\');')