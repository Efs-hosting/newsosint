# 🌍 Bölgesel Haber OSINT Aracı

Bu proje, Python ve Flask kullanılarak geliştirilmiş hafif ve hızlı bir **Açık Kaynak İstihbaratı (OSINT)** aracıdır. Kullanıcıların belirlediği il veya bölgeye ait en güncel haberleri Google News RSS altyapısı üzerinden çekerek sade bir web arayüzünde sunar.

## ✨ Özellikler

* **Bölge Bazlı Arama:** İstediğiniz ili yazarak sadece o bölgeye ait son gelişmelere anında ulaşın.
* **Otomatik Kurulum ve Başlatma:** `baslat.bat` dosyası sayesinde eksik Python kütüphanelerini (`flask`, `requests`) otomatik kurar ve yerel sunucuyu ayağa kaldırır.
* **Tarayıcı Entegrasyonu:** Sunucu başladığında varsayılan web tarayıcınızı otomatik olarak açar ve arayüzü karşınıza getirir.
* **Sade ve Modern Arayüz:** Göz yormayan karanlık tema (Dark Mode) tasarımı ile haberleri rahatça okuyun.

## 🚀 Kurulum ve Kullanım

Sistemi çalıştırmak oldukça basittir. Bilgisayarınızda [Python](https://www.python.org/downloads/)'un (PATH'e eklenmiş şekilde) kurulu olması yeterlidir.

1. Projeyi bilgisayarınıza indirin (ZIP olarak indirebilir veya `git clone` kullanabilirsiniz).
2. Klasörün içindeki `baslat.bat` dosyasına çift tıklayın.
3. Terminal ekranı açılacak, gerekli kontroller yapılacak ve birkaç saniye içinde tarayıcınızda uygulama başlayacaktır.
4. Arama kutusuna bir il adı (Örn: *Muğla, İzmir, Ankara*) yazıp aratın.

## 🛠️ Kullanılan Teknolojiler

* **Backend:** Python 3, Flask, Requests, XML ElementTree
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
* **Otomasyon:** Windows Batch Script (.bat)
* **Veri Kaynağı:** Google News RSS

## 📌 Notlar
Bu araç, tamamen halka açık (public) verileri derlemek için eğitim ve araştırma amaçlı geliştirilmiştir. Herhangi bir veritabanı bağlantısı veya veri saklama işlemi (loglama) yapmaz; tamamen anlık çalışır.
