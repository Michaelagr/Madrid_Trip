import streamlit as st

st.set_page_config(page_title="Madrid Reiseplan", layout="wide")


# Titel
st.title("🌆 Madrid Reiseplan für 4 Tage")
st.markdown("**Für unsere Reise  ♥️ – mit viel Zeit für gutes Essen, Entspannung und Genuss.**")

# Seitenleiste für Navigation
days = ["Tag 1 – Klassiker & Altstadt", 
        "Tag 2 – Tostado, Farben-Museum, Salamanca & Squids",
        "Tag 3 – Lokale Viertel & Hidden Gems", 
        "Tag 4 – Abschied & Ausblick", 
        "Tag 5 - Montag - Abreise", 
        "Gestrichene Optionen"]
#selected_day = st.sidebar.radio("📅 Wähle einen Tag", days)

# Tagespläne
itinerary = {
    "Tag 1 – Klassiker & Altstadt": {
        "Frühstück": [
            "🥪 *Cafe Angelica*: Toast mit Avocado & Ziegenkäse und Toast mit Tomate + Cafe con Leche"
        ],
        "Vormittag": [
            "🍫 *Churros con Chocolate* bei San Gines"
            "🧭 *Plaza Mayor* – Flamenco Konzert",
            "🍃 *Pflanzen Shop* - Kurze Auszeit",
            "🏠 *Thyssen Museum* - Museumsshop",
            "📍 Puerta del Sol – das Herz Madrids"
        ],
        "Mittagessen": [
            "🦐 *La abuela* - Tapas Bar mit frittierten Scampi & Scampi mit Knoblauch + Sangria & Bier",
            "🌧️ *Regenpause* mit mehr Sangria",
            "🥧 *Manteigeria* - Pasteis de Nata am Plaza de Sol"
        ],
        "Nachmittag": [
            "🛍️ *Shopping Pause* - Zara & Corte Ingles (unerfolgreich)",
            "⛪ *San Idriso Prozession* - Trauermarsch-Feeling für Feiertag",
            "🚶‍♀️ *Spaziergang* durch die Stadt"
        ],
        "Abendessen": [
            "⛲ *Jardin de Santilles* - Unspektakuläres Konzert von Olga, aber nette Atmosphäre",
            "🏛️ *Palacio Real* - Sonnnenuntergang mit Aussicht",
            "🍤 Mercado de San Miguel – Tapas von verschiedenen Ständen (wiederholen mit Hunger)"
        ],
        "Night Entertainment": [
            "📺 *TV Night* - Eurovision Song Contest"
        ],
        "Gelaufene Distanz": [
            "🏆 17km 🏆"
        ]
    },
    
    "Tag 2 – Tostado, Farben-Museum, Salamanca & Squids": {
    "Frühstück": [
        "☕ *Cafe con Leche* zum Aufwachen im Hotel",
        "🍓 *Hanso Cafe* (Joghurt mit Früchten & Cafe con Leche)"
    ],
    "Vormittag": [
        "🏙️ *Corte Inglés*: Blick auf Hotelzimmer",
        "🥪 Erster Snack: *Tostado* (endlich!!)",
        "🍰 Erster Nachtisch: *Merengue Schaum-Törtchen* (🤍)",
        "🚶‍♀️ Spaziergang Richtung *Salamanca*",
        "🛍️ *Loewe Laden* mit komischem Verkäufer",
        "👩‍💻 Remote Work Session für Ela – gestresster Zoom Call im Café"
    ],
    "Mittagessen": [
        "🖼️ Besuch im *Juan March Museo* – Super toll, Fäden, Farben, riesiges Bild im Keller (Laokoon) !!!",
        "🚶‍♀️ Weiter Spaziergang durch Salamanca – Versuch, etwas zu essen zu finden",
        " 🛍️ Shopping Stopp: Dr. Bloom - grün gepunktete Bluse gekauft",
        "🥪 Unspektakulärer Markt -> gegenüber kleiner *Dosenthunfisch-Bocadillo*"
    ],
    "Nachmittag": [
        "📚 Empfehlung von Student: *Galeros Restaurant* (Corrupción Octopus-Bild; Empanada, Gebratene Squids & Jakobsmuscheln & leckerer Wein - sehr ungesalzen, sonst gut)",
        "📞 *Papa angerufen*",
        "🌇 Verzweifelte Suche nach Rooftop Bar für Sonnenuntergang – erfolglos (*UMusic* & *Radio Rooftop*)"
    ],
    "Sundownder": [
        "🍷 *Furchtbarer Essig-Sherry* in Bar mit sonst toller Atmosphäre"
    ],
    "Abendessen": [
        "😴 Zurück & sehr müde"
    ],
        "Gelaufene Distanz": [
            "🏆 16km 🏆"
        ]
    },
    "Tag 3 – Lokale Viertel & Hidden Gems": {
    "Frühstück": [
        "🏃‍♀️ Erster Jogging Run – *Retiro Park*, verdeckter *Palacio de Cristal*, *Statue of the Fallen Angel*, durch Südkurve zurück zum Hotel",
        "☕ Hotel-Frühstück mit Blick auf *Gran Via* und *Plaza de Callao*"
    ],
    "Vormittag": [
        "🏖️ *Lucha de Gran Canaria* – mit schwarzem Sand auf *Plaza de Callao*",
        "🖼️ Kleine Kunst-Läden in der Straße nördlich vom Hotel",
        "🍫 *Fred de Merveilleux* – Zwischensnack (Weiße Schokolade)",
        "👚 *Dr. Bloom* – Mama Bluse umtauschen"
    ],
    "Mittagessen": [
        "🍷 *Lokale Taberna* – Anchovies in Essig, Artischocken & Sangria",
        "🏛️ *Museo Arquitectura* – Untergeschoß mit Entwicklungsarbeit okay, Obergeschoß mit Modellen SEHR langweilig"
    ],
    "Nachmittag": [
        "🚶‍♀️ Zurück in die Innenstadt spaziert – wieder keine Rooftop Bar gefunden",
        "😩 Hunger! Ab zum *Mercado de San Miguel*:"
    ],
    "Snack/Dinner": [
        "🥟 *Empanadas* (Queso & Jamón, Provolone & dried tomato)",
        "🍳 *Tortilla* mit karamellisierten Zwiebeln & Camembert-Creme + *Cerveza*",
        "🫒 Spicy & Kräuter-Oliven & schlechter *Sangria*",
        "🥟 Mehr *Empanadas* (fried & 4 Queso)"
    ],
    "Abend": [
        "📺 Zurück ins Hotel & *Eurovision Song Contest* geguckt – aber schon sehr müde"
    ]
    },
    "Tag 4 – Abschied & Ausblick": {
    "Frühstück": [
        "🏃‍♀️ Zweite Jogging Runde: *Casa de Campo* mit Umweg um *Palacio Real* herum (7 km!)",
        "🥐 Frühstück in kleinem Café in Seitenstraße – *Farton*, Mini-Croissant & Gebäck mit *Café con Leche*"
    ],
    "Vormittag": [
        "🌬️ *Wim Hof* Atemübung im Hotel (bis ca. 12 Uhr)",
        "📱 Ausstellung in der *Fundación Telefónica* – erst im Handy-Shop gelandet, dann richtige Ausstellung: Ozean-Geräusche & Visualisierungen, Kunst von *Plensa* (?), Kopfskulpturen & Telefonentwicklung"
    ],
    "Mittagessen": [
        "🍽️ *Taberna 4 Tapas*: Cheese Sticks (*Tequeños*), Chorizo & Käseplatte, Beef & Kartoffeln, frittierte Aubergine mit Honig & Karaffe Sangria (sehr lecker)"
    ],
    "Nachmittag": [
        "💡 *Museo de la Luz* – Super tolle interaktive Ausstellung mit verschiedenen Werken",
        "🍖 *Jamonería* – Schinken als Mitbringsel gekauft",
        "🍷 Café am *Plaza de San Andrés* – schlechter Sangria & Chips, aber tolle Atmosphäre – so viele Leute auf der Straße"
    ],
    "Abend": [
        "🚶‍♀️ Langsam zurück ins Hotel – kurze Ruhepause, wieder keine Sunset Option",
        "🛍️ Snacks in *Carrefour* besorgt & illegale Taschenverkäufer beobachtet",
        "🍦 Letzter Spaziergang zur *Puerta del Sol* (zum ca. 30. Mal) & *Dulce de Leche* Eiscreme (sehr gut!)"
    ]
    },
    "Tag 5 - Montag - Abreise": {
        "Abreise": [
            "⏰ 4.20 Wecker - Uber um 4.50",
            "✈️ 6.20 Uhr Abflug Madrid --> Brüssel",
            "🛫 9.35 Uhr Abflug Brüssel --> München (mit leckerem Sandwich, Empanada, Kaffee & Cookie 🤩"
        ]
    },
    "Gestrichene Optionen": {
        "Cafés": [
            "☕ *Café de la Luz* oder *HanSo Café* (Malasaña, 10 Minuten zu Fuß vom Hotel)",
            "☕ *Café de Oriente* oder *Federal Café*"
        ],
        "Restaurants": [
            "🍽️ * La Maruca* - Empfehlung (nördlich von Retiro)",
            "🍷 *Los Gatos* oder *Bodega de los Secretos* (stylische Location!)",
            " 🌭 Option für *Snack*: Latino Arepa (Arepas, Empfehlung)",
            "🥘 *Lamucca de Pez* oder *Toma Jamón*"
        ], 
        "Aktivitäten": [
            "🌿 Spaziergang durch den *Retiro-Park* mit Kristallpalast",
            "🏛️ Almudena-Kathedrale & Palacio Real",
            "📖 Bummel durchs *Barrio de las Letras* (literarisches Viertel)",
            "🌳 Pause in den Gärten *Sabatini* oder *Campo del Moro*",
            "🖼️ Besuch im *Museo del Prado* oder *Reina Sofía* (für Picasso & Co.) - vielleicht auch nicht",
            "🎨 Erkundung von *Lavapiés*: Street Art, kleine Galerien, alternative Läden",
            "🌿 Spaziergang durch den Jardines del Conde Duque – ruhig & grün",
            "🖼️ Optional: Ausstellung im Centro Cultural Conde Duque – wechselnde moderne Kunst/Performance",
            "🚶 Spaziergang durch *La Latina* mit Plaza de la Paja",
            "🏛️ Optional: *Museo Cerralbo* – ein echter Geheimtipp!",
            "🕌 *Templo de Debod* – ägyptischer Tempel mit Sonnenuntergang",
            "Alternativ: 🌿 Jardín Botánico – herrlicher botanischer Garten neben dem Prado, ruhig und wunderschön angelegt",
            "🐢 Im Anschluss: Atocha Bahnhof – Tropenhalle mit Schildkröten & Palmen mitten im Bahnhof",
            "❌ Leider geschlossen: *Museo Sorolla* (klein & ruhig)"
        ],
        "Sundownder": [
            "🍷 Danach: Sundowner auf der Dachterrasse des Círculo de Bellas Artes (kleiner Eintritt, grandiose Aussicht)"
        ],
         "Abendessen": [
            "🍷 *La Venencia* – authentisch, Sherry-Bar, keine Fotos erlaubt",
            "🍽️ Alternativ: *Casa Revuelta* – legendärer Bacalao",
            "🍹 Rooftop-Aperitif: *Picalagartos* oder *Doña Luz*",
            "🍷 Abendessen Option 1: *La Taberna de Elisa* (klassisch & lokal)",
            "🍷 Abendessen Option 2: *Kuoco* (Empfehlung Maria)",
            "⭐ Alternative: La Maruca - Velazquez (Empfehlung)",
            "🔥 *Sobrino de Botín* – ältestes Restaurant der Welt (vorher reservieren!)",
            "🍷 Alternative 1: *Taberna Tempranillo* auf der *Cava Baja*",
            "⭐ Alternative 2: *Manero* (Empfehlung Maria)"
        ]
    }
}

# Anzeige des ausgewählten Tages
#day_plan = itinerary[selected_day]

tabs = st.tabs(list(itinerary.keys()))

#st.header(selected_day)

for tab, (day_name, sections) in zip(tabs, itinerary.items()):
    with tab:
        st.subheader(day_name)
        for section, items in sections.items():
            with st.expander(section, expanded=True):
                for item in items:
                    st.markdown(f"- {item}")


#for section, items in day_plan.items():
#    with st.expander(f"**{section}**", expanded=True):
#        for item in items:
#            st.markdown(f"- {item}")

#st.sidebar.markdown("---")
st.info("✨ Auf einen wundervollen Trip! Ich freue mich sehr ♥️")
