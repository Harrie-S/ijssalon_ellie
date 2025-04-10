from algemene_functies import mijn_funtie_2

def aanbieding_1(smaak, prijs, korting):
    
    prijs_na_korting = "{:.2f}".format(prijs - (prijs *korting))
    prijs_na_korting = prijs_na_korting.replace(".",",")
    
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {prijs_na_korting} euro."

def inkomsten_totaal(inkomsten, btw):
    totaal =0
    for inkomst in inkomsten:
        totaal += inkomst
    bedrag = "{:.2f}".format(totaal *btw)
    bedrag = bedrag.replace(".",",")
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    return [
        max(mijn_lijst),
        min(mijn_lijst)
    ]

def gemiddelde(mijn_lijst):
    bedrag = "{:.2f}".format(sum(mijn_lijst)/len(mijn_lijst))
    bedrag = bedrag.replace(".",",")
    return f"De gemiddelde inkomsten deze week zijn {bedrag} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(mijnlijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_funtie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer