Vrachtwagen_rijbewijs = input("Heeft u een Vrachtwagen rijbewijs? (ja/nee): ")
hoge_hoed = input("Bent u in bezit van een hoge hoed? (ja/nee): ")
gewicht = input("Bent u zwaarder dan 90 kg en lichter dan 120 kg? (ja/nee): ")
ervaring_dieren_dressuur = int(input("Hoeveel jaar ervaring heeft u met dieren-dressuur (voer het als een getal in): "))
ervaring_jongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren (voer het als een getal in): "))
ervaring_acrobatiek = int(input("Hoeveel jaar ervaring heeft u met acrobatiek? (voer het als een getal in): "))

if (Vrachtwagen_rijbewijs == "ja") and (hoge_hoed == "ja") and (gewicht == "ja") and (ervaring_dieren_dressuur >=4 or ervaring_jongleren >=5 or ervaring_acrobatiek >=3):
    print("Aangenomen!")
else: 
    print("Niet aangenomen")