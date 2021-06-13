from math import isclose
import random
import time

class Kumanda():
    def __init__(self, tv_durum = "Kapalı", tv_ses = 3, kanal_listesi = ["TRT"], kanal = "TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tv_ac(self):
        if self.tv_durum == "Açık" :
            print("TV zaten açık")
        else:
            print("TV açılıyor...")
            self.tv_durum = "Açık"
    def tv_kapat(self):
        if self.tv_durum == "Kapalı" :
            print("TV zaten kapalı")
        else:
            print("TV kapatılıyor...")
            self.tv_durum = "Kapalı"
    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi azalt: '<'\nSesi Artır: '>' \nÇıkış : 'q'\n : " )
            if cevap == "<":
                if self.tv_ses != 0 :
                    self.tv_ses -= 1
                    print("Ses:", self.tv_ses)
            elif cevap == ">":
                if self.tv_ses != 31 :
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)
            else:
                print("Ses güncellendi:", self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("{} kanalı eklendi...".format(kanal_ismi))
    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi))
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal : ", self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv Durumu : {}\nTv Ses : {}\nKanal Listesi : {}\nŞu anki kanal : {}\n".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)
Kumanda = Kumanda()
print("""
      Televizyon Uygulaması
      
      1. TV Aç
      2. TV Kapat
      3. Ses ayarları
      4. Kanal Ekle
      5. Kanal sayısını öğrenme
      6. Rastgele kanala geçme
      7. Tv Bilgileri
      
      Çıkmak için q'ya basın
      
      """)

while True:
    işlem = input("İşlem Seçiniz : ")
    if işlem == "q" :
        print("Program Sonlandırılıyor...")
        break
    elif işlem == "1" :
        Kumanda.tv_ac()
    elif işlem == "2" :
        Kumanda.tv_kapat()
    elif işlem == "3" :
        Kumanda.ses_ayarlari()
    elif işlem == "4" :
        kanal_isimleri = input("Kanal İsimlerini ',' ile ayırarak girin :")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            Kumanda.kanal_ekle(eklenecekler)
    elif işlem == "5" :
        print("Kanal sayısı", len(Kumanda))
    elif işlem == "6" :
        Kumanda.rastgele_kanal()
    elif işlem == "7" :
        print(Kumanda)
    else :
        print("Geçersiz işlem girdiniz...")