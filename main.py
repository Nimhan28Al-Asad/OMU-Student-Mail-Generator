from unidecode import unidecode
departement = 'Bilgisayar Mühendisliği' 
university = 'Ondokuz mayıs Üniversitesi'
# print(departement, faculty)

departement_short = unidecode(departement)[:3].lower()
university_short = ''.join(unidecode(word[0]).lower() for word in university.split())

# print (departement_short, university_short)

with open('file.txt', 'r', encoding="utf-8") as file:
    content = content = file.read().splitlines()
    for items in content:
        
        a = unidecode(items).split(',')
        
        id_number = a[0]
        names = a[1].lower().strip().split()
        if len(names) >= 2:
            name = names[1]
        else:
            name = names[0]
        surname = a[-1].lower().strip()
        student_amail = f'{name}.{surname}@{departement_short}.{university_short}.edu.tr'
        print(f'{id_number}, {student_amail}')
        
