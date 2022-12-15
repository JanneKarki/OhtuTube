english_display = {
    "commands":(
    "Commands:"
    + "\n"
    + "-" * 117
    + "\n"
    + """[1]Add new reference
[2]Display all references
[3]Search
[4]Display selected references
[5]Create .bib file from selected references
[6]Import references from bibtex-file
[7]Remove reference
[8]Empty database
[9]Change Language
[0]Exit
"""
    + "-" * 117
),

"welcome":"\n Welcome to the OhtuTube reference application \n",
"no command":"Command not recognized, please enter a valid command",

"bibtex created":"Bibtex-file created!",

"add failed":"Failed to add!",
"add success":"Added successfully!",

"answer":"Answer y(yes) or n(no)",
"validate save":"\n Do you want to save this item to database? (y/n): ",

"input author":"> Author (Last name, First name): ",
"input title":"> Title: ",
"input year":"> Year: ",
"input publisher":"> Publisher: ",
"input address":"> Address: ",
"input id":"> Reference ID:",

"author error":"Error, enter the author like this: Bond, James",
"empty error":"Error, field is empty!",
"year error":"Error, enter the year like this: 2014",
"id error space":"Error, Reference ID should not contain spaces",
"id error uppercase":"Error, Reference ID should not contain uppercase letters",
"id error taken":"Error, Reference ID is already taken",

"validate delete selected":"Do you want to remove selected references? y/n: ",
"validate delete all":"Do you want to remove all references? y/n: ",

"delete complete":"Delete complete!",
"delete all":"All the references deleted",

"close":"\n Closing application",

"search keyword":"> Keyword: ",

"change language":"Changing language to finnish"
}
finnish_display = {
    "commands":(
    "Komennot:"
    + "\n"
    + "-" * 117
    + "\n"
    + """[1]Lisää uusi lähde
[2]Näytä kaikki lähteet
[3]Haku
[4]Näytä valitut lähteet
[5]Luo .bib tiedosto valituista lähteistä
[6]Tuo lähteet .bib tiedostosta
[7]Posta lähteet
[8]Tyhjennä lähteet
[9]Vaihda kieltä
[0]Poistu
"""
    + "-" * 117
),

"welcome":"\n Tervetuloa OhtuTube lähdesovellukseen \n",
"no command":"Komentoa ei tunnistettu, syötä oikea komento",

"bibtex created":"Bibtex-tiedosto luotu!",

"add failed":"Lisäys epäonnistui!",
"add success":"Lisäys onnistui!",

"answer":"Vastaa y(kyllä) tai n(ei)",
"validate save":"\n Haluatko tallentaa tämän lähteen tietokantaan? (y/n): ",

"input author":"> Tekijä (Sukunimi, Etunimi): ",
"input title":"> Nimi: ",
"input year":"> Vuosi: ",
"input publisher":"> Kustantaja: ",
"input address":"> Osoite: ",
"input id":"> Lähde ID:",

"author error":"Virhe, kirjoita tekijän nimi näin: Bond, James",
"empty error":"Virhe, kenttä on tyhjä!",
"year error":"Virhe, kirjoita vuosi näin: 2014",
"id error space":"Virhe, Lähde ID ei saa sisältää välilyöntejä",
"id error uppercase":"Virhe, Lähde ID ei saa sisältää isoja kirjaimia",
"id error taken":"Virhe, Lähde ID on jo käytössä",

"validate delete selected":"Haluatko poistaa valitut lähteet? (y/n): ",
"validate delete all":"Haluatko poistaa kaikki lähteet? (y/n): ",

"delete complete":"Poisto valmis!",
"delete all":"Kaikki lähteet poistettu",

"close":"\n Sovellus sulkeutuu",

"search keyword":"> Hakusana: ",

"change language":"Vaihdetaan kieli englanniksi"
}

english_attr = {
    "reference_id":"Reference ID",
    "author":"Author",
    "title":"Title",
    "year":"Year",
    "publisher":"Publisher",
    "address":"Address"
}

finnish_attr = {
    "reference_id":"Lähde ID",
    "author":"Tekijä",
    "title":"Nimi",
    "year":"Vuosi",
    "publisher":"Kustantaja",
    "address":"Osoite"
}

def build_id_display(id, lan):
    if lan == 1:
        return (f"> Automatically generated id: {id}."
                +" Do you want to manually create reference id? (y/n): ")
    else:
        return (f"> Automaattisesti luotu id: {id}."
                +" Haluatko luoda oman id:n manuaalisesti? (y/n): ")

