# Ana Menü

menu = """
        - Python Restorant Uygulaması-

        1-) Masaları Görüntüle
        2-) Sipariş Ekle
        3-) Hesap Ödeme
        4-) Çıkış


"""
masalar = dict()
# Masa Oluşturma
for a in range(10):
    masalar[a] = 0

# Fonksiyonlar
def hesapekle():
    masa_no = int(input("Masa No: "))
    bakiye = masalar[masa_no]
    eklenecek_ucret = float(input("Eklenecek Ücret: "))
    guncel_bakiye = bakiye + eklenecek_ucret
    masalar[masa_no] = guncel_bakiye
    print("İşleminiz tamamlandı.")

def hesap_odeme():
    masa_no = int(input("Masa No: "))
    bakiye = masalar[masa_no]
    print("Masa {}'in hesabı: {}".format(masa_no, bakiye))
    masalar[masa_no] = 0
    print("Hesap Ödendi.")

def dosya_kontrolu(dosya_adi):
    try: 
        dosya = open(dosya_adi, "r", encoding="utf-8")
        veri = dosya.read()
        veri = veri.split("\n")
        veri.pop()
        dosya.close()
        for a in enumerate(veri):
            masalar[a[0]] = float(a[1])
    except FileNotFoundError:
        dosya = open(dosya_adi, "w" ,encoding="utf-8")
        dosya.close()
        print("Kayıt Oluşturuldu.")

def dosya_guncelle(dosya_adi):
    dosya = open(dosya_adi, "w", encoding="utf-8")
    for a in range(10):
        bakiye = masalar[a]
        bakiye = str(bakiye)
        dosya.write(bakiye+"\n")
    dosya.close()

# Ana Uygulama
while True:
    dosya_kontrolu("log.txt")

    print(menu)

    secim = input("İşlem Numarası Giriniz: ")
    if secim == "1":
        for a in range(10):
            print("Masa {} için hesap: {}".format([a],[masalar[a]]))
    elif secim == "2":
        hesapekle()
    elif secim == "3":
        hesap_odeme()
    elif secim == "4":
        print("Çıkış Yapılıyor...")
        quit()
    else: 
        print("Hatalı seçim yaptınız.")
    dosya_guncelle("log.txt")
    input("Ana menüye dönmek için enter'a basınız.")
