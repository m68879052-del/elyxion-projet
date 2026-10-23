import os

html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Plan d'Architecte Expert - Villa 25x20m</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #1e1e24; margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; color: #fff; }
        h1 { color: #f5f6fa; margin-bottom: 5px; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; }
        p { color: #a4b0be; margin-bottom: 20px; font-size: 14px; }
        .container { background-color: #ffffff; padding: 25px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        svg { border: 3px solid #2f3640; background-color: #ffffff; }
        .legend { margin-top: 20px; display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; width: 1000px; }
        .legend-item { display: flex; align-items: center; font-size: 13px; color: #dcdde1; }
        .color-box { width: 18px; height: 18px; margin-right: 8px; border-radius: 4px; border: 1px solid #718093; }
    </style>
</head>
<body>
    <h1>Plan d'Exécution Architectural - Version Meublée Pro</h1>
    <p>Échelle 1:50 — Cotations en Mètres — Trame modulaire de 1.00m</p>
    
    <div class="container">
        <svg width="1000" height="800" viewBox="0 0 1000 800">
            <defs>
                <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
                    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#f1f2f6" stroke-width="1"/>
                </pattern>
            </defs>
            <rect width="1000" height="800" fill="url(#grid)" />
            
            <rect x="0" y="0" width="320" height="280" fill="#f5f6fa" /> <rect x="0" y="640" width="320" height="160" fill="#fcf5d9" /> <rect x="320" y="480" width="400" height="320" fill="#ebf5fb" /> <rect x="720" y="0" width="280" height="240" fill="#f4f1ea" /> <rect x="800" y="240" width="200" height="200" fill="#fbfaf7" /> <rect x="720" y="600" width="280" height="200" fill="#fbfaf7" /> <g stroke="#7f8c8d" stroke-width="1.5" fill="none">
                
                <rect x="60" y="110" width="70" height="130" rx="15" stroke="#718093" stroke-width="2"/>
                <rect x="65" y="140" width="60" height="70" rx="5" stroke="#718093"/>
                <circle cx="70" cy="125" r="4" fill="#718093"/><circle cx="120" cy="125" r="4" fill="#718093"/>
                <rect x="190" y="110" width="70" height="130" rx="15" stroke="#718093" stroke-width="2"/>
                <rect x="195" y="140" width="60" height="70" rx="5" stroke="#718093"/>
                <circle cx="200" cy="125" r="4" fill="#718093"/><circle cx="250" cy="125" r="4" fill="#718093"/>

                <rect x="360" y="520" width="100" height="160" rx="5" stroke="#2c3e50" stroke-width="2" fill="#fff"/>
                <text x="410" y="605" font-size="10" fill="#7f8c8d" text-anchor="middle">TABLE RPT</text>
                <rect x="335" y="535" width="25" height="25" rx="3"/><rect x="335" y="570" width="25" height="25" rx="3"/><rect x="335" y="605" width="25" height="25" rx="3"/><rect x="335" y="640" width="25" height="25" rx="3"/>
                <rect x="460" y="535" width="25" height="25" rx="3"/><rect x="460" y="570" width="25" height="25" rx="3"/><rect x="460" y="605" width="25" height="25" rx="3"/><rect x="460" y="640" width="25" height="25" rx="3"/>

                <path d="M 560,760 L 560,660 L 680,660" stroke-width="3" stroke="#2c3e50"/> <rect x="590" y="690" width="60" height="40" rx="2"/> <line x1="500" y1="710" x2="500" y2="770" stroke-width="4" stroke="#2c3e50"/> <rect x="730" y="150" width="40" height="40" fill="#f5f6fa"/> <circle cx="750" cy="170" r="3"/>
                <rect x="785" y="150" width="20" height="12" rx="2" fill="#fff"/> <ellipse cx="795" cy="172" rx="10" ry="12" fill="#fff"/> <rect x="730" y="210" width="35" height="25" rx="2"/>
                <ellipse cx="747" cy="222" rx="10" ry="6"/>

                <rect x="730" y="490" width="45" height="45"/> <circle cx="752" cy="512" r="3"/>
                <rect x="795" y="490" width="20" height="12" rx="2" fill="#fff"/>
                <ellipse cx="805" cy="512" rx="10" ry="12" fill="#fff"/>
                <rect x="730" y="565" width="45" height="25" rx="2"/>
                <ellipse cx="752" cy="577" rx="12" ry="6"/>

                <rect x="880" y="20" width="80" height="64" stroke-width="2" fill="#fff"/>
                <rect x="885" y="25" width="20" height="54" fill="#f1f2f6"/> <rect x="880" y="340" width="80" height="64" stroke-width="2" fill="#fff"/>
                <rect x="885" y="345" width="20" height="54" fill="#f1f2f6"/>
                <rect x="880" y="700" width="80" height="64" stroke-width="2" fill="#fff"/>
                <rect x="885" y="705" width="20" height="54" fill="#f1f2f6"/>
            </g>

            <g fill="#2c3e50" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="600">
                <text x="20" y="35" font-size="13" font-weight="bold" fill="#2f3542">GARAGE / PARKING HORS-ŒUVRE</text>
                <text x="20" y="52" fill="#747d8c">Surf: 56.00 m² — Dalle béton lissé</text>
                
                <text x="340" y="505" font-size="13" font-weight="bold" fill="#0984e3">SÉJOUR / SALLE À MANGER</text>
                <text x="340" y="522" fill="#747d8c">Surf: 80.00 m² — Revêtement Grès Cérame</text>

                <text x="830" y="115" font-size="12" font-weight="bold" fill="#6c5ce7">CH. 1 PARENTALE</text>
                <text x="830" y="130" fill="#747d8c">Surf: 42.00 m²</text>
                
                <text x="830" y="265" font-size="12" font-weight="bold" fill="#6c5ce7">CHAMBRE 2</text>
                <text x="830" y="280" fill="#747d8c">Surf: 25.00 m²</text>

                <text x="835" y="625" font-size="12" font-weight="bold" fill="#6c5ce7">CHAMBRE 3</text>
                <text x="835" y="640" fill="#747d8c">Surf: 35.00 m²</text>

                <text x="400" y="370" font-size="13" font-weight="bold" fill="#2f3542" opacity="0.6">HALL / VESTIBULE CENTRAL</text>
                <text x="20" y="670" font-size="13" font-weight="bold" fill="#e1b12c">TERRASSE EXTÉRIEURE</text>
            </g>

            <g stroke="#1e272e" stroke-width="8" stroke-linecap="square" fill="none">
                <path d="M 320 0 L 1000 0 L 1000 800 L 320 800 L 320 640 L 0 640 L 0 280 L 320 280 L 320 0" />
                <line x1="0" y1="280" x2="0" y2="0" stroke-width="6"/> 
                <line x1="0" y1="0" x2="320" y2="0" stroke-width="6"/>
                <line x1="0" y1="800" x2="320" y2="800" stroke-width="6"/>
                
                <line x1="320" y1="280" x2="720" y2="280" />
                <line x1="320" y1="480" x2="720" y2="480" />
                <line x1="720" y1="0" x2="720" y2="800" />
                <line x1="800" y1="240" x2="1000" y2="240" />
                <line x1="720" y1="600" x2="1000" y2="600" />
                
                <line x1="720" y1="140" x2="840" y2="140" stroke-width="5"/>
                <line x1="840" y1="140" x2="840" y2="240" stroke-width="5"/>
                <line x1="720" y1="480" x2="840" y2="480" stroke-width="5"/>
                <line x1="840" y1="480" x2="840" y2="600" stroke-width="5"/>
            </g>

            <g stroke="#ea2027" stroke-width="3" fill="none">
                <line x1="320" y1="680" x2="320" y2="720" stroke="#fff" stroke-width="12" /> <line x1="320" y1="680" x2="355" y2="680" /> <path d="M 355,680 A 35,35 0 0,1 320,715" stroke-dasharray="3,3"/> <line x1="720" y1="70" x2="720" y2="110" stroke="#fff" stroke-width="12" />
                <line x1="720" y1="110" x2="755" y2="110" />
                <path d="M 720,75 A 35,35 0 0,1 755,110" stroke-dasharray="3,3"/>

                <line x1="800" y1="310" x2="800" y2="350" stroke="#fff" stroke-width="12" />
                <line x1="800" y1="350" x2="765" y2="350" />
                <path d="M 800,315 A 35,35 0 0,0 765,350" stroke-dasharray="3,3"/>

                <line x1="720" y1="710" x2="720" y2="750" stroke="#fff" stroke-width="12" />
                <line x1="720" y1="710" x2="755" y2="710" />
                <path d="M 720,745 A 35,35 0 0,1 755,710" stroke-dasharray="3,3"/>
                
                <line x1="840" y1="180" x2="840" y2="215" stroke="#fff" stroke-width="10" />
                <line x1="840" y1="215" x2="815" y2="215" />
                
                <line x1="840" y1="520" x2="840" y2="555" stroke="#fff" stroke-width="10" />
                <line x1="840" y1="555" x2="815" y2="555" />
            </g>

            <g stroke="#0652dd" stroke-width="5">
                <line x1="440" y1="800" x2="620" y2="800" />
                <line x1="440" y1="796" x2="530" y2="796" stroke-width="2"/>
                <line x1="525" y1="804" x2="620" y2="804" stroke-width="2"/>
            </g>

            <g fill="#1e272e" font-size="13" font-family="monospace" font-weight="bold">
                <line x1="0" y1="-15" x2="1000" y2="-15" stroke="#1e272e" stroke-width="1.5"/>
                <line x1="0" y1="-20" x2="0" y2="-10" stroke="#1e272e" stroke-width="1.5"/>
                <line x1="1000" y1="-20" x2="1000" y2="-10" stroke="#1e272e" stroke-width="1.5"/>
                <text x="480" y="-25">CÔTE TOTALE : 25.00 m</text>
                
                <line x1="-15" y1="0" x2="-15" y2="800" stroke="#1e272e" stroke-width="1.5"/>
                <line x1="-20" y1="0" x2="-10" y2="0" stroke="#1e272e" stroke-width="1.5"/>
                <line x1="-20" y1="800" x2="-10" y2="800" stroke="#1e272e" stroke-width="1.5"/>
                <text x="-35" y="430" transform="rotate(-90 -35 430)">CÔTE TOTALE : 20.00 m</text>
            </g>
        </svg>
    </div>

    <div class="legend">
        <div class="legend-item"><div class="color-box" style="background-color: #ebf5fb;"></div>Séjour / Aménagement Variable</div>
        <div class="legend-item"><div class="color-box" style="background-color: #f4f1ea;"></div>Chambres à Coucher</div>
        <div class="legend-item"><div class="color-box" style="background-color: #ffffff; border: 1px dashed stroke;"></div>Sanitaires (WC / Douche / Vasque)</div>
        <div class="legend-item"><div class="color-box" style="background-color: #fcf5d9;"></div>Espaces Communs / Extérieurs</div>
        <div class="legend-item"><div class="color-box" style="background-color: #f5f6fa;"></div>Zone Logistique Véhicules</div>
    </div>
</body>
</html>"""

bureau = os.path.join(os.path.expanduser("~"), "Desktop")
with open(os.path.join(bureau, "plan_architecte.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print("--- LE PLAN HTML TECHNIQUE ET MEUBLÉ A ÉTÉ CRÉÉ SUR LE BUREAU ! ---")