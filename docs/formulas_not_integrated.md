#Berekenen meest voordelige prijs
Berekent de meest voordelige prijs tussen twee gelijke producten, in verschillende hoeveelheden.

## Variabelen
* price1: Prijs eerste product
* price2: Prijs tweede product
* weight1: Hoeveelheid 1e product
* weight2: Hoeveelheid 2e product

*basevalue: Basiswaarde voor berekeningen (b.v 100 gram, 1 stuk, 1l)
* baseprice1: Basisprijs (resultaat) 1e product
* baseprice2: Basisprijs (resultaat) 2e product
* basediff: Prijsverschil tussen producten, @basisprijs

## Formule
baseprice = (price1 * (basevalue / price1)
baseprice2 = (price2 * (basevalue / price2)

Uitkomst: Product (X) is het voordeligst, je bespaart (basediff) per (basevalue)

Vergelijking: if baseprice1 > baseprice2

# Split the bill
Berekent hoeveel iedereen moet betalen om een rekening te splitsen

## variabelen
* party: aantal leden
* bill: totaal van de rekening
* party(x): Aantal leden in party
* partybill(x): Rekening voor de party
* partyname(x): Naam voor de party

## Formule

partybill(x): bill * (party(X) / party)

Resultaat(?): (Partyname(x)) moet (partybill(x)) betalen
