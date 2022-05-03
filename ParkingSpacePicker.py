import cv2
import pickle

width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)


while True:
    img = cv2.imread('carParkImg.png')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)

    ABDULSAMET ATAŞ
    ALPEREN AKBABA
    AHMET FURKAN AKDAMAR
    ESRA AKTÜRK
    SİNEM ALTAN
    BUSE ALTINDAĞ
    MEHMET ANIL
    GÖKÇE AŞCI
    BUKET ASLAN
    GÖRKEM AYDEMİR
    AYBERK AYDOĞUMU
    DOĞUKAN AYHAN
    AYSENUR BAHÇE
    CANAN CAN
    KADİR ZAHİD CİNTOSUN
    İREM YAĞMUR COŞKUN
    BÜŞRA CURA
    İBRAHİM MERT ÇAKICIOĞLU
    SAMED ÇAKIR
    BATUHAN ÇAKMAK
    ÜMİT ÇALIŞICI
    HÜSEYİN ÇALIŞKAN
    ASLI ÇIRACI
    SİNEM ÇOKAN
    MELİSA ÇÖĞEN
    YAĞMUR DALMIZRAK
    SERENAY DEVECİ
    YAĞMUR DİBEKTAŞ
    NURTEN DÖKMECİ
    BUSEM ÖYKÜ DUMAN
    JAHAN DURDYYEVA
    JAHAN DURDYYEVA YILDIRIM
    TUĞÇE DURMAZ
    ECE YAĞMUR EL
    BEDİRHAN ELÇİN
    FURKAN EMİR
    MERYEM ERBEY
    SEDEF ERBEY
    AHMET BEŞİR ERCAN
    MERT EROL
    YİĞİT ETHAN
    BUSE ETİLER
    RABİA EZEN
    ERAY GEDİOGLU
    RUKEN GİRİŞ
    GÜLCAN HIRLI
    EMİRCAN HIZARCI
    EREN İSHAKOĞLU
    DİDEM KAÇA
    TANER KAPLANER
    HİLAL KAPLANKARA
    ERKAN KARABAĞ
    ATAKAN KARAKOÇ
    BUĞRA KARAYİĞİT
    KÜBRA KAYA
    CEM KIRILMAZ
    ŞÜHEDA NUR KIVRAK
    ŞÜKRAN SELİN KIZILTAN
    KEREM KİLERCİ
    HANİFE FATMA KORKMAZ
    KÜBRA KOVAYÇİN
    ELİF BEYZA LERMİOĞLU
    ZÜLFÜKAR MİNAZ
    ZEYNEP ASELSU UYSAL
    ZEHRA ÜÇTEPE
    SÜMEYYE SARI
    SÜLEYMAN SAMET SAĞÖZ
    SERAY ŞAHLI
    SEHER ŞİMŞEK
    SEFA ÖZDEMİR
    ÖYKÜ YÜZBAŞIOĞLU
    AHMET CAN SANGI
    ALİ OSMAN ÜNAL
    ATAKAN PARÇAL
    AYTAÇ ÖZKAN
    BEKİR OCAK
    BERK MARAL
    BERK YİĞİT YURDAGÜL
    BİLGE TANRIKULU
    BURAK ÜTTECİEL
    DENİZ PARLAR
    DİLAN TUNÇ
    DİLEK HATİCE TOPAL
    DUYGU ÖZTÜRK
    ELANUR ŞİMŞEK
    EMİNE ÖZDEMİR
    EMRE ŞENGÜL
    ENES KAAN ŞAHBAZ
    EROL TANE
    FAHRETTİN TANRIVERDİ
    FEYZA TÜYSÜZ
    GİZEM ORAN
    GÜRCAN ÖZDEMİR
    HAKAN TUNCEL
    HATİCE YÜKSEL
    KADİR YILDIZ
    MELEK YILDIRIM
    MELİH ŞEKER
    MELİSA MALÇOK
    MİNE ŞAHİN
    NİLÜFER SARI
    NİMET ŞANAL
    OZAN TOPUZ
    BETÜL KERİMLER
    GÜL YILMAZ
    KADİR VELİBEYOĞLU
    GÜLSÜM BİLEKLİ
    GÜLCAN PORTAKAL
    BURAK CAN ALTUNOĞLU
    GÜLBEN DURSUN
    FURKAN DENİZ KARAKAŞ
    ECE UMUTLU
    GİZEM YILMAZ
    ANIL AKTARER
    RÜVEYDA ŞENEL
    KÜBRA KAYA
    NUR ERTAN
    ERAY TOSUN
    NURULLAH ALTINDAĞ
    ÜMRAN ARMAĞAN
    NASİM ALSEDRAMDAN
    DOĞUKAN GÜNER
