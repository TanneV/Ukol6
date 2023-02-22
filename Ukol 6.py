import re

regularni_vyraz = re.compile(r"(\d|\d\d)(\.|\/)( )?(\d|\d\d)(\.|\/)( )?\d\d\d\d")

vstup = input("Zadej datum: ")

vstup_ok = regularni_vyraz.fullmatch(vstup)

print(vstup_ok)

if vstup_ok: 
    print("Datum je v pořádku")
else:  
    print("Nesprávný format datumu")

\d{3} \d{2}  ?(.+) ?(\d)*