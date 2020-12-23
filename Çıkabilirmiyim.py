#Yunus Emre Dışarı çıkabilirmiyim uygulaması 1.gün 23.12.2020



gun = str(input("Lütfen günü giriniz: "))

if gun == "cumartesi":
    print("Dışarı çıkmanız yasak")

elif gun == "pazar" :
    print("Dışarı çıkmanız yasak")

if gun == "pazartesi" or "salı" or "carsamba" or "persembe" or "cuma"   :
    
    yas = int(input("Lütfen yaşınızı giriniz: "))
    
    if yas <= 18 :
         saat = int(input("Lütfen saati giriniz"))
         if 0 <= saat <= 12 :
            print("Dışarıya çıkamazsınız")
         elif 13 <= saat <= 17:
            print("Dışarıya çıkabilirsiniz")
         elif 18 <= saat <= 24 :      
            print("Dışarı çıkmanız yasak")
         
    elif 65 <= yas:
            print("Dışarıya çıkmanız yasak")
    elif 19 <= yas <= 64 :
        saat = 0<=int(input("Lütfen saati giriniz"))<=24
        if saat <= 5:
                print("Dışarı çıkmanız yasak")
        elif saat >= 21:
                print("Dışarı çıkmanız yasak")
        elif 5 <= saat <= 21 :
                print("Dışarıya çıkabilirsiniz")  
         
            
            
            












