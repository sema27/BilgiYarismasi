
para = 0
konular = ["BİLİŞİM","KÜLTÜR-SANAT","SPOR"]
yazilim_sorulari = konular[0]
yazilim_sorulari = ["1 - Hangisi üst seviye bir yazilim dili değildir ? \n A : Python   B : Assembly   C : Java   D : C++",
                    "2 - Aşağıdakilerden hangisi doğrudur ? \n A : 1 Kilobyte = 8 Bit   B : 1024 MB = 1 KB   C : 1 MB = 1024 KB   D : 1 GB = 1024 KB",
                    "3 - Hangisi programlama dili değildir ? \n A : HTML   B : Pascal   C : Kotlin   D : PHP",
                    "4 - Aşağıdakilerden hangisi virüs çeşitlerinden değildir ?  \n A : Truva Atları   B : Solucanlar   C : Dosya Virüsleri   D : Kelebekler",
                    "5 - jpg hangi dosyaların dosya uzantısıdır ? \n A : Video   B : Resim   C : Word   D : Hiçbiri",
                    "6 - Hangisi bir veritabanı yönetim sistemi (DBMS) değildir ? \n A : MySQL   B : Windows   C : Oracle   D : SQLServer",
                    "7 - En büyük açık kaynaklı işletim sistemi nedir? ? \n A : OpenBSD   B : Linux   C : BlackArch   D : ReactOS",
                    "8 - Amazon, hangi yıl kurulmuştur ve ilk olarak ne tür bir ürün satmıştır ? \n A : 1988 - Ayakkabı   B : 1991 - Cep Telefonu   C : 1994 - Kitap   D : 1997 - Oyuncak",
                    "9 - Tübitak tarafından geliştirilen milli işletim sisteminin adı nedir ? \n A :  Dos   B : Amiga   C : Truva   D : Pardus",
                    "10 - Türkiye’de ilk internet kaç yılında hangi kurumdan bağlanılmıştır ? \n A :1993 – ODTÜ   B : 1989 - YTÜ   C : 1995 - İTÜ   D : 1988 - HACETTEPE"]
yazilim_cevaplari = ["B","C","A","D","B","B","B","C","D","A"]

kultur_sanat_sorulari = konular[1]
kultur_sanat_sorulari = ["1 - Yaprak Dökümü romanının yazarı aşağıdakilerden hangisidir ? \n A : Reşat Nuri Güntekin   B : Halide Edip Adıvar   C : Ziya Gökalp   D : Ömer Seyfettin",
                         "2 - 1912–1948 yılları arasında yapılan Yaz Olimpiyatları'nın “Sanat Yarışmaları” kısmında hangi branş yoktur ? \n A : Edebiyat   B : Mimari   C : Müzik   D : Sinema",
                         "3 - Halide Edip Adıvar, “Sinekli Bakkal” romanını ilk olarak hangi dilde yazmıştır ? \n A : Latince   B : İngilizce   C : Fransızca   D : Almanca",
                         "4 - Eurovision şarkı yarışmasına 1975 yılında ilk hangi ünlü isim katılmıştır ?  \n A : Ajda Pekkan   B : Semiha Yankı   C : Çetin Alp   D : Nilüfer ve Grup Nazar",
                         "5 - Louvre Müzesi’nde çalışmaları ölmeden önce sergilenen ilk ressam hangisidir ? \n A : Amedeo Modiglani   B : Salvador Dali   C : Georges Braque   D :  Paul Gauguin",
                         "6 - Oscar ödülü alan ilk kadın yönetmen kimdir ? \n A : Nora Ephron   B : Kathryn Bigelow   C : Vera Chytilova   D : Tomris Giritlioğlu",
                         "7 - Bedenini bilimsel araştırmalara, kafatasını ise “Hamlet” oyununda kullanılmak üzere bağışlayan besteci kimdir ? \n A : Beethoven   B : Bach   C : Çaykovski   D : Mozart",
                         "8 - Antik ve Orta Çağ yüksek eğitiminin temeli olan 7 özgür sanattan biri hangisidir ? \n A : Anatomi   B : Fizik   C : Gökbilim   D : Politika",
                         "9 - James Cameron, yazdığı hangi filmin senaryosu 1 Dolar'a satmıştır ? \n A : Yaratıklar   B : Terminatör   C : Titanik   D : Avatar",
                         "10 - Broadway'de sergilenen ilk Türk müzikali hangisidir ? \n A : Hisseli Harikalar Kumpanyası   B : Mucizeler Komedisi   C : Tahir ile Zühre   D : Zümrüdü Anka"]
kultur_sanat_cevaplari = ["A","D","B","B","C","B","C","C","B","A"]

spor_sorulari = konular[2]
spor_sorulari = ["1 - Bir maraton ne kadar sürer ? \n A : 34.118 kilometre (21.2 mil)   B : 42.195 kilometre (26.2 mil)   C : 50.211 kilometre (31.2 mil)   D : 58.258 kilometre (36.2 mil)",
                 "2 - Bir beyzbol takımında kaç oyuncu vardır ? \n A : 7   B : 8   C : 9   D : 10",
                 "3 - 2018 Dünya Kupası'nı hangi ülke kazanmıştır ? \n A : Fransa   B : İngiltere   C : Kanada   D : Türkiye",
                 "4 - Kanada'nın iki ulusal sporu hangileridir ?  \n A : Buz Hokeyi - Tenis   B : Beyzbol - Buz Hokeyi   C : Lakros - Futbol   D : Lakros - Buz Hokeyi",
                 "5 - 1946'da ilk NBA maçını hangi takım kazanmıştır ? \n A : Boston Celtics   B : New York Knicks   C : Washington Capitols   D : Chicago Stags",
                 "6 - Aşağıdaki dövüş sporlarından hangisi Bruce Lee tarafından uygulanmadı ? \n A : Jeet Kune Do   B : Wushu   C : Boks   D : Eskrim",
                 "7 - 2010 yılında ülkemizde düzenlenen kış olimpiyatları hangi şehirde yapılmıştır ? \n A : Kars   B : Erzurum   C : Ağrı   D : Van",
                 "8 - Hangi spor dalında -Hole in one- terimi kullanılır ? \n A : Valeybol   B : Beyzbol   C : Golf   D : Tenis",
                 "9 - Hangi şehir, 2020 Yaz Olimpiyatları'na ev sahipliği yapacaktı ancak COVID-19 pandemisi nedeniyle 2021'e ertelendi ? \n A :  Rio de Janeiro   B : Pekin   C : Seul   D : Tokyo",
                 "10 - 2021 Tokyo Olimpiyatlarında Türkiye hangi branşlarda altın madalya kazanmıştır ? \n A :Okçuluk – Boks   B : Boks - Jimnastik   C : Güreş - Okçuluk   D : Karete - Güreş"]
spor_cevaplari = ["B","C","A","D","B","B","B","C","D","A"]

print("""\n\n*****KİM MİLYONER OLMAK İSTER BİLGİ YARIŞMASINA HOŞGELDİNİZ*****
KATEGORİLER :

1 ) BİLİŞİM
2 ) KÜLTÜR - SANAT
3 ) SPOR

""")
kategori = int(input("Yarışmak İstediğiniz Kategoriyi Tuşlayınız : \n"))
if kategori == 1:
  for i in range(10):
    print(yazilim_sorulari[i])
    yanit = input("CEVAP : ")
    if yanit.upper() == yazilim_cevaplari[i] :
        para = (i+1) * 100000 
        print(f"Tebrikler, {para} TL kazandınız.")
    else:
        print("Yanlış Cevap, Elendiniz.")
        break
elif kategori == 2:
  for i in range(10):
    print(kultur_sanat_sorulari[i])
    yanit = input("CEVAP : ")
    if yanit.upper() == kultur_sanat_cevaplari[i] :
      para = (i+1) * 100000
      print(f"Tebrikler, {para} TL kazandınız.")
    else:
        print("Yanlış Cevap, Elendiniz.")
        break
elif kategori == 3:
  for i in range(10):
    print(spor_sorulari[i])
    yanit = input("CEVAP : ")
    if yanit.upper() == spor_cevaplari[i] :
      para = (i+1) * 100000 
      print(f"Tebrikler, {para} TL kazandınız.")
    else:
        print("Yanlış Cevap, Elendiniz.")
        break
else :
   print("Hatalı Tuşlama !")
   
    