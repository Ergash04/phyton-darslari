print('do`stlaringizni yoshini saqlaymiz')
dostlar = {}
ishora = True
while ishora:
    ism = input('do`stingizni ismini kiriting:')
    yosh = input(f"{ism.title()} ning yoshini kiriting:")
    dostlar[ism] = int(yosh)
    javob = input('yana ism qo`shasizmi? (ha/yo`q)')
    
    
    if javob == "yo`q":
        ishora = False
                              

