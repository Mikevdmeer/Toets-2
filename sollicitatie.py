def gender(man, vrouw, anders):
    return gender
gender = input("Bent u een man, vrouw of anders?: ")
Vrachtwagen_rijbewijs_ok = "ja"
hoge_hoed_ok = "ja"
gewicht_ok = "ja"
ervaring_dieren_dressuur_ok = 4
ervaring_jongleren_ok = 5
ervaring_acrobatiek = 3
Vrachtwagen_rijbewijs = input("Heeft u een Vrachtwagen rijbewijs? (ja/nee): ")
if Vrachtwagen_rijbewijs == "banaan":
    raise NameError('een banaan is geen rijbewijs!')
hoge_hoed = input("Bent u in bezit van een hoge hoed? (ja/nee): ")
if hoge_hoed == "lage hoed":
    raise TypeError('dat is niet de bedoeling')
gewicht = input("Bent u zwaarder dan 90 kg en lichter dan 120 kg? (ja/nee): ")
if gewicht == "10":
    raise ValueError('dat is niet gezond')
ervaring_dieren_dressuur = int(input("Hoeveel jaar ervaring heeft u met dieren-dressuur (voer het als een getal in): "))
ervaring_jongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren (voer het als een getal in): "))
ervaring_acrobatiek = int(input("Hoeveel jaar ervaring heeft u met acrobatiek? (voer het als een getal in): "))
reden_1 = Vrachtwagen_rijbewijs != Vrachtwagen_rijbewijs_ok
reden_2 = hoge_hoed != hoge_hoed_ok
reden_3 = gewicht != gewicht_ok
reden_4 = ervaring_dieren_dressuur != ervaring_dieren_dressuur_ok
reden_5 = ervaring_jongleren != ervaring_jongleren_ok
reden_6 = ervaring_acrobatiek != ervaring_acrobatiek
if gender == "man":
    snor = input("Heeft u een snor? (ja/nee): ")
    if snor == "nee":
        print("U bent niet aangenomen omdat u geen snor heeft.")
        exit()
elif gender == "vrouw":
    rood_krulhaar = input("Heeft u rood knulhaar? (ja/nee): ")
    if rood_krulhaar == "nee":
        print("U bent niet aangenomen omdat u geen rood knulhaar heeft.")
        exit()
else:
    brede_glimlach = input("Heeft u een brede glimlach? (ja/nee): ")
    if brede_glimlach == "nee":
        print("U bent niet aangenomen omdat u geen brede glimlach heeft.")
        exit()

if (Vrachtwagen_rijbewijs == "ja") and (hoge_hoed == "ja") and (gewicht == "ja") and (ervaring_dieren_dressuur >=4 or ervaring_jongleren >=5 or ervaring_acrobatiek >=3):
    print("Aangenomen!")
elif reden_1:
    print("U bent niet aangenomen oomdat u geen vrachtwagen rijbewijs heeft.")
elif reden_2:
    print("U bent niet aangenomen omdat u geen hoge hoed heeft.")
elif reden_3:
    print("U bent niet aangenomen omdat u gewicht niet voldoet aan onze eisen.")
elif reden_4 or reden_5 or reden_6:
    print("U bent niet aangenomen omdat u te weinig of geen ervaring heeft met dieren dressuur, jongleren en acrobatiek.") 
else: 
    print("Niet aangenomen")