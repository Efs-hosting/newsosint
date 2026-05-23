from flask import Flask, render_template_string, request, jsonify
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Kullanıcı Arayüzü (HTML/CSS/JS)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bölgesel Haber OSINT Aracı</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background-color: #1e1e2f; color: #fff; }
        .container { max-width: 800px; margin: 0 auto; background: #2a2a40; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
        h1 { color: #00d2ff; text-align: center; border-bottom: 2px solid #3a3a5c; padding-bottom: 10px; }
        .search-box { display: flex; gap: 10px; margin-top: 20px; }
        input { flex: 1; padding: 12px; font-size: 16px; border: none; border-radius: 6px; background: #3a3a5c; color: #fff; outline: none; }
        input:focus { border: 1px solid #00d2ff; }
        button { padding: 12px 24px; font-size: 16px; font-weight: bold; background-color: #00d2ff; color: #1e1e2f; border: none; border-radius: 6px; cursor: pointer; transition: 0.3s; }
        button:hover { background-color: #00a8cc; }
        .news-item { background: #3a3a5c; margin-top: 15px; padding: 15px; border-radius: 8px; border-left: 4px solid #00d2ff; }
        .news-item a { color: #fff; text-decoration: none; font-size: 18px; font-weight: 600; display: block; margin-bottom: 5px; }
        .news-item a:hover { color: #00d2ff; }
        .date { font-size: 0.85em; color: #a1a1aa; }
        .loader { text-align: center; margin-top: 20px; color: #00d2ff; font-style: italic; display: none; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌍 Bölgesel Haber OSINT Aracı</h1>
        <p style="text-align: center; color: #a1a1aa;">Haberlerini çekmek istediğiniz ili yazın</p>
        
        <div class="search-box">
            <input type="text" id="cityInput" placeholder="Örn: Muğla, İzmir, İstanbul..." onkeypress="if(event.key === 'Enter') fetchNews()">
            <button onclick="fetchNews()">İstihbaratı Başlat</button>
        </div>
        
        <div id="loader" class="loader">Veriler çekiliyor...</div>
        <div id="results" style="margin-top: 20px;"></div>
    </div>

    <script>
        async function fetchNews() {
            const city = document.getElementById('cityInput').value.trim();
            const resultsDiv = document.getElementById('results');
            const loader = document.getElementById('loader');
            
            if (!city) {
                alert('Lütfen bir il adı girin.');
                return;
            }

            resultsDiv.innerHTML = '';
            loader.style.display = 'block';

            try {
                const response = await fetch(`/api/news?city=${city}`);
                const data = await response.json();
                
                loader.style.display = 'none';

                if (data.length === 0) {
                    resultsDiv.innerHTML = '<p style="text-align:center;">Bu bölgeye ait güncel haber bulunamadı.</p>';
                    return;
                }

                let html = `<h3 style="color:#00d2ff;">${city.toUpperCase()} - Son Gelişmeler</h3>`;
                data.forEach(item => {
                    // Tarih formatını düzenle
                    const dateObj = new Date(item.pubDate);
                    const formattedDate = dateObj.toLocaleString('tr-TR', { dateStyle: 'medium', timeStyle: 'short' });
                    
                    html += `
                        <div class="news-item">
                            <a href="${item.link}" target="_blank">${item.title}</a>
                            <span class="date">📅 ${formattedDate}</span>
                        </div>
                    `;
                });
                resultsDiv.innerHTML = html;
            } catch (error) {
                loader.style.display = 'none';
                resultsDiv.innerHTML = `<p style="color:#ff4d4d; text-align:center;">Bağlantı hatası: ${error}</p>`;
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/news')
def get_news():
    city = request.args.get('city', '')
    if not city:
        return jsonify([])
    
    # Google News RSS üzerinden bölge bazlı sorgu
    url = f"https://news.google.com/rss/search?q={city}+haberleri&hl=tr&gl=TR&ceid=TR:tr"
    
    try:
        response = requests.get(url)
        root = ET.fromstring(response.content)
        
        news_list = []
        # En güncel 15 haberi al
        for item in root.findall('.//item')[:15]:
            title = item.find('title').text
            link = item.find('link').text
            pubDate = item.find('pubDate').text
            
            # Kaynak adını başlıktan temizle (Opsiyonel ama daha temiz görünür)
            if " - " in title:
                title = title.rsplit(" - ", 1)[0]
                
            news_list.append({
                'title': title,
                'link': link,
                'pubDate': pubDate
            })
        return jsonify(news_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Sadece yerelde (localhost) çalışır
    app.run(host='127.0.0.1', port=5050)