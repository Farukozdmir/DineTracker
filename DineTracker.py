import komut

import time

komut = komut.restoranlar()
komut.bağlantı()

global username
username = komut.kullanıcı_adı()


print("""
    ************************************************
                      
                    Welcome, {}
           Personal Map Assistant
           
    To view restaurants: 1
    To add a restaurant: 2
    To delete a restaurant: 3
    To search for a restaurant by location: 4
    To change username: 5
    To delete all restaurants: 6
    To exit: q
    
    ************************************************""".format(username))



    
while True:
    
    key = input("Select the action you want to perform: ")
    
    
    
    if key == "1":
      komut.restoranları_göster()
    elif key == "2":
        komut.restoran_ekle()
    elif key == "3":
        komut.restoran_sil()
    elif key == "4":
        komut.konumda_ara()
    elif key == "q":
        break
    elif key == "5":
        username = komut.kullanıcı_adı_degis()
        print("Username is changing...")
        time.sleep(1)
        
        print("""
           ************************************************
                             
                           Welcome, {}
                  Personal Map Assistant
                  
           To view restaurants: 1
           To add a restaurant: 2
           To delete a restaurant: 3
           To search for a restaurant by location: 4
           To change username: 5
           To delete all restaurants: 6
           To exit: q
           
           ************************************************""".format(username))
           
    elif key == "6":
        komut.kütüphaneyi_sıfırla()
    else:
        print("Invalid input...")
        
        
komut.bağlantıyı_kes()