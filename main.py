
pip install sounddevice


import sounddevice as sd

# Ses parametreleri
samplerate = 44100  # Örnekleme oranı
channels = 1  # Mono kanal (bas gitar için)

# Ses verilerini gerçek zamanlı olarak al ve hoparlöre geri gönder
def guitar_amp(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata  # Giriş sesini direkt çıkışa yönlendir

# Gitar sesini yakala ve hoparlöre geri ver
with sd.Stream(callback=guitar_amp, channels=channels, samplerate=samplerate):
    print("Bas gitar sesi dinleniyor... CTRL+C ile çıkabilirsiniz.")
    sd.sleep(10000)  # 10 saniye boyunca sesi işler


