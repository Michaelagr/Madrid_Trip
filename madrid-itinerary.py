import streamlit as st

st.set_page_config(page_title="Madrid Reiseplan", layout="wide")


# Titel
st.title("🌆 Madrid Reiseplan für 4 Tage")
st.markdown("**Für unsere Reise  ♥️ – mit viel Zeit für gutes Essen, Entspannung und Genuss.**")

# Seitenleiste für Navigation
days = ["Tag 1 – Klassiker & Altstadt", "Tag 2 – Kunst & Retiro",
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
        ]
    },
    
    
    "Tag 2 – Kunst & Retiro": {
        "Frühstück": [
            "☕ *Café de la Luz* oder *HanSo Café* (Malasaña, 10 Minuten zu Fuß vom Hotel)",
            "☕ *Café de Oriente* oder *Federal Café*"
        ],
        "Vormittag": [
            "🔦 *Museo de la Luz*",
            "🖼️ Besuch im *Museo del Prado* oder *Reina Sofía* (für Picasso & Co.) - vielleicht auch nicht"
        ],
        "Mittagessen": [
            "🍽️ * La Maruca* - Empfehlung (nördlich von Retiro)"
            "🍷 *Los Gatos* oder *Bodega de los Secretos* (stylische Location!)",
            " 🌭 Option für *Snack*: Latino Arepa (Arepas, Empfehlung)"
        ],
        "Nachmittag": [
            "🌿 Spaziergang durch den *Retiro-Park* mit Kristallpalast",
            "🏛️ Almudena-Kathedrale & Palacio Real",
            "📖 Bummel durchs *Barrio de las Letras* (literarisches Viertel)",
            "🌳 Pause in den Gärten *Sabatini* oder *Campo del Moro*"
        ],
        "Sundownder": [
            "🍷 Danach: Sundowner auf der Dachterrasse des Círculo de Bellas Artes (kleiner Eintritt, grandiose Aussicht)"
        ],
        "Abendessen": [
            "🍷 *La Venencia* – authentisch, Sherry-Bar, keine Fotos erlaubt",
            "🍽️ Alternativ: *Casa Revuelta* – legendärer Bacalao",
            "🍹 Rooftop-Aperitif: *Picalagartos* oder *Doña Luz*",
            "🍷 Abendessen Option 1: *La Taberna de Elisa* (klassisch & lokal)",
            "🍷 Abendessen Option 2: *Kuoco* (Empfehlung Maria)"
        ]
    },
    "Tag 3 – Lokale Viertel & Hidden Gems": {
        "Sport": [
          "💪 *Jogging-Runde* durch Retiro Park"      
        ],
        "Frühstück": [
            "☕ *Plántate Café* oder *The Fix* (Lavapiés)",
            "☕ *Café de la Luz* oder *HanSo Café* (Malasaña, 10 Minuten zu Fuß vom Hotel)",
            "☕ *Café de Oriente* oder *Federal Café*"
        ],
        "Vormittag": [
            "🔦 *Museo de la Luz*",
            "🖼️ Besuch im *Museo del Prado* oder *Reina Sofía* (für Picasso & Co.) - vielleicht auch nicht"
            "🎨 Erkundung von *Lavapiés*: Street Art, kleine Galerien, alternative Läden",
            "🌿 Spaziergang durch den Jardines del Conde Duque – ruhig & grün",
            "🖼️ Optional: Ausstellung im Centro Cultural Conde Duque – wechselnde moderne Kunst/Performance"
        ],
        "Mittagessen": [
            "🍽️ *Mercado de Antón Martín* – vielfältige Auswahl",
            "⭐ Alternative: La Maruca - Velazquez (Empfehlung)"
        ],
        "Nachmittag": [
            "🚶 Spaziergang durch *La Latina* mit Plaza de la Paja",
            "🏛️ Optional: *Museo Cerralbo* – ein echter Geheimtipp!"
        ],
        "Abendessen": [
            "🔥 *Sobrino de Botín* – ältestes Restaurant der Welt (vorher reservieren!)",
            "🍷 Alternative 1: *Taberna Tempranillo* auf der *Cava Baja*",
            "⭐ Alternative 2: *Manero* (Empfehlung Maria)"
        ]
    },
    "Tag 4 – Abschied & Ausblick": {
        "Frühstück": [
            "☕ *El Jardín Secreto* oder Hotelfrühstück auf der Terrasse"
        ],
        "Vormittag": [
            "🛍️ Bummel über den *Rastro* - auf die Taschen aufpassen!",
            "🌇 Rooftop: *Círculo de Bellas Artes* (fantastischer Ausblick!)"
        ],
        "Mittagessen": [
            "🥘 *Lamucca de Pez* oder *Toma Jamón*"
        ],
        "Nachmittag": [
            "🕌 *Templo de Debod* – ägyptischer Tempel mit Sonnenuntergang",
            "Alternativ: 🌿 Jardín Botánico – herrlicher botanischer Garten neben dem Prado, ruhig und wunderschön angelegt",
            "🐢 Im Anschluss: Atocha Bahnhof – Tropenhalle mit Schildkröten & Palmen mitten im Bahnhof",
            "❌ Leider geschlossen: *Museo Sorolla* (klein & ruhig)"
        ],
        "Abendessen": [
            "🦐 *Mercado Miguel* - Tapas Snacks?",
            "🍄 *El Cisne Azul* – für Pilzliebhaber"
        ]
    },
        "Tag 5 - Montag - Abreise": {
            "Abreise": [
                "✈️ 6.20 Uhr Abflug Madrid Flughafen "
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
                " 🌭 Option für *Snack*: Latino Arepa (Arepas, Empfehlung)"
            ], 
            "Nachmittag": [
                "🌿 Spaziergang durch den *Retiro-Park* mit Kristallpalast",
                "🏛️ Almudena-Kathedrale & Palacio Real",
                "📖 Bummel durchs *Barrio de las Letras* (literarisches Viertel)",
                "🌳 Pause in den Gärten *Sabatini* oder *Campo del Moro*"
            ],
             "Abendessen": [
                "🍷 *La Venencia* – authentisch, Sherry-Bar, keine Fotos erlaubt",
                "🍽️ Alternativ: *Casa Revuelta* – legendärer Bacalao",
                "🍹 Rooftop-Aperitif: *Picalagartos* oder *Doña Luz*",
                "🍷 Abendessen Option 1: *La Taberna de Elisa* (klassisch & lokal)",
                "🍷 Abendessen Option 2: *Kuoco* (Empfehlung Maria)"
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
