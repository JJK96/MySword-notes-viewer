books = [
    "Genesis",
    "Exodus",
    "Leviticus",
    "Numeri",
    "Deuteronomium",
    "Jozua",
    "Richteren",
    "Ruth",
    "1 Samuel",
    "2 Samuel",
    "1 Koningen",
    "2 Koningen",
    "1 Kronieken",
    "2 Kronieken",
    "Ezra",
    "Nehemia",
    "Ester",
    "Job",
    "Psalmen",
    "Spreuken",
    "Prediker",
    "Hooglied",
    "Jesaja",
    "Jeremia",
    "Klaagliederen",
    "Ezechiël",
    "Daniël",
    "Hosea",
    "Joël",
    "Amos",
    "Obadja",
    "Jona",
    "Micha",
    "Nahum",
    "Habakuk",
    "Sefanja",
    "Haggai",
    "Zacharia",
    "Maleachi",
    "Matteüs",
    "Marcus",
    "Lucas",
    "Johannes",
    "Handelingen",
    "Romeinen",
    "1 Korintiërs",
    "2 Korintiërs",
    "Galaten",
    "Efeziërs",
    "Filippenzen",
    "Kolossenzen",
    "1 Tessalonicenzen",
    "2 Tessalonicenzen",
    "1 Timoteüs",
    "2 Timoteüs",
    "Titus",
    "Filemon",
    "Hebreeën",
    "Jakobus",
    "1 Petrus",
    "2 Petrus",
    "1 Johannes",
    "2 Johannes",
    "3 Johannes",
    "Judas",
    "Openbaring",
]


def get_book(id):
    if id is None:
        return None
    return books[id-1]
