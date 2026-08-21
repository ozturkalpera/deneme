@app.get("/")
def ana_sayfa():
    return {"mesaj": "Python backend canlıda ve sorunsuz çalışıyor!"}from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Mobil uygulamadan gelecek verinin kalıbını (şablonunu) tanımlıyoruz
class HesaplamaIsteği(BaseModel):
    kullanici_adi: str
    sayi1: int
    sayi2: int

# 1. Var olan GET adresi (Veri okumak için)
@app.get("/mobil/profil")
def profil_getir():
    return {
        "kullanici_adi": "Ahmet",
        "app_versiyon": "1.0.0",
        "bildirim_sayisi": 3
    }

# 2. Yeni POST adresi (Mobil uygulamadan veri almak için)
@app.post("/mobil/topla")
def sayilari_topla(veri: HesaplamaIsteği):
    toplam = veri.sayi1 + veri.sayi2
    
    # Mobil uygulamaya dönen cevap
    return {
        "mesaj": f"Merhaba {veri.kullanici_adi}, işlemin tamamlandı!",
        "sonuc": toplam
    }
