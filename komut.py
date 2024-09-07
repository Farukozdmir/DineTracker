import sqlite3

import time

class restoran():
    
    def __init__(self,isim,konum,mutfak,ek_bilgi):
        
        self.isim = isim
        self.konum = konum
        self.mutfak = mutfak
        self.ek_bilgi = ek_bilgi
        
    def __str__(self):
        
        return "Restaurant Name: {}\nLocation: {}\nFood Type: {}\nNotes: {} ".format(self.isim, self.konum,self.mutfak,self.ek_bilgi)




class restoranlar():
    
    def __init__(self):
        
        self.bağlantı()
        
    def bağlantı(self):
        
        self.con = sqlite3.Connection("data1.db")
        
        self.cursor = self.con.cursor()
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Restoranlar(isim TEXT,konum TEXT,mutfak TEXT,ek_bilgi TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kullanıcı(isim TEXT)")
        self.con.commit()
    
    def bağlantıyı_kes(self):
        
        self.con.close()
        
    def restoranları_göster(self):
        self.cursor.execute("SELECT * FROM Restoranlar")
        restoranlar = self.cursor.fetchall()
        

        
        
        print("Searching for restaurants...")
        time.sleep(2)
        
        if len(restoranlar) == 0:
            print("It seems no restaurants have been added yet...")
            
        else:
            print("***************************************\n")
            for i in restoranlar:
                
                print(restoran(i[0],i[1],i[2],i[3]),"\n")
                
    def restoran_ekle(self):
        
        isim = input("Restaurant Name: ")
        sanatçı = input("Location: ")
        albüm = input("Food Type: ")
        süre = input("Notes: ")
        print("Saving...")
        time.sleep(2)
        
        self.cursor.execute("INSERT INTO Restoranlar VALUES(?,?,?,?)",(isim,sanatçı,albüm,süre))
        self.con.commit()
        print("The restaurant has been successfully saved.")
        
    def restoran_sil(self):
        b = False
        isim = input("Please enter the name of the restaurant you want to delete: ")
        isim = isim
        self.cursor.execute("SELECT isim from Restoranlar")
        names = self.cursor.fetchall()

        for i in names:
            if (i[0]) == isim:
                b = True

        if b:
            
            self.cursor.execute("DELETE FROM Restoranlar where isim = ?",(isim,))
            self.con.commit()
            print(isim+" Deleting...")
            time.sleep(2)
            print(isim+" Successfully deleted.")
            
        else:
            print(isim+" Deleting...")
            time.sleep(2)
            
            print(" A restaurant named"+isim + " could not be found...")
        
    def konumda_ara(self):
        b = True
        konumu = input("Search with location: ")
        self.cursor.execute("SELECT * FROM Restoranlar")
        
        yer = self.cursor.fetchall()
        print("Searching for restaurants in the" + konumu)
        print("\n*********************************************\n")
        
        for i in yer:
            if  (i[1]) == konumu:
                print(restoran(i[0],i[1],i[2],i[3]),"\n")
                b = False
        if b:
            print("No restaurants found at the location you searched for...")
            
    def kullanıcı_adı(self):
        
        global ilk_isim
        self.cursor.execute("Select isim from kullanıcı")
        isimi = self.cursor.fetchall()
        
        if len(isimi) == 0:
            
            ilk_isim = input("How would you like me to address you: ")
            self.cursor.execute("Insert into kullanıcı values(?)",(ilk_isim,))
            self.con.commit()
        self.cursor.execute("Select isim from kullanıcı")
        isimi = self.cursor.fetchall()
        
        return isimi[0][0]
    
    def kullanıcı_adı_degis(self):
        
        self.cursor.execute("Select isim from kullanıcı")
        isimi = self.cursor.fetchall()
        
        if len(isimi) == 1:
            
            ilk_isim = input("How would you like me to address you: ")
            self.cursor.execute("update kullanıcı set isim=?",(ilk_isim,))
            self.con.commit()
            
    def kütüphaneyi_sıfırla(self):
        
       
        
        while True:
            a = input("Are you sure you want to delete all information? (YES/NO):")
            if a == "YES":
                b = input("Are you sure? (YES/NO): ")
                if b == "YES":
                    self.cursor.execute("delete from restoranlar")
                    break
                elif b == "NO":
                    break
                else:
                    print("Invalid input...")
                    continue
            elif a == "NO":
                 break
            else:
                 print("Invalid input...")
                 continue
        print ("Resetting...")
        time.sleep(2)
    