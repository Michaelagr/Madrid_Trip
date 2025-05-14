import streamlit as st

st.set_page_config(page_title="Madrid Reiseplan", layout="wide")


# Titel
st.title("🌆 Madrid Reiseplan für 4 Tage")
st.markdown("**Für unsere Reise  ♥️ – mit viel Zeit für gutes Essen, Entspannung und Genuss.**")

# Seitenleiste für Navigation
days = ["Tag 1 – Klassiker & Altstadt", "Tag 2 – Kunst & Retiro",
        "Tag 3 – Lokale Viertel & Hidden Gems", "Tag 4 – Abschied & Ausblick", "Tag 5 - Montag - Abreise"]
#selected_day = st.sidebar.radio("📅 Wähle einen Tag", days)

# Tagespläne
itinerary = {
    "Tag 1 – Klassiker & Altstadt": {
        "Frühstück": [
            "☕ *Café de la Luz* oder *HanSo Café* (Malasaña, 10 Minuten zu Fuß vom Hotel)"
        ],
        "Vormittag": [
            "📍 Puerta del Sol – das Herz Madrids",
            "🧭 Plaza Mayor – kurzer Stopp bei *Chocolatería San Ginés* für Churros",
        ],
        "Mittagessen": [
            "🍤 Mercado de San Miguel – Tapas von verschiedenen Ständen",
            "🍽️ Alternativ: *Casa Revuelta* – legendärer Bacalao",
        ],
        "Nachmittag": [
            "🏛️ Almudena-Kathedrale & Palacio Real",
            "🌳 Pause in den Gärten *Sabatini* oder *Campo del Moro*"
        ],
        "Abendessen": [
            "🍹 Rooftop-Aperitif: *Picalagartos* oder *Doña Luz*",
            "🍷 Abendessen Option 1: *La Taberna de Elisa* (klassisch & lokal)",
            "🍷 Abendessen Option 2: *Kuoco* (Empfehlung Maria)"
        ]
    },
    "Tag 2 – Kunst & Retiro": {
        "Sport": [
          "💪 *Jogging-Runde* durch Retiro Park"      
        ],
        "Frühstück": [
            "☕ *Café de Oriente* oder *Federal Café*"
        ],
        "Vormittag": [
            "🖼️ Besuch im *Museo del Prado* oder *Reina Sofía* (für Picasso & Co.)"
        ],
        "Mittagessen": [
            "🍷 *Los Gatos* oder *Bodega de los Secretos* (stylische Location!)",
            " 🌭 Option für *Snack*: Latino Arepa (Arepas, Empfehlung)"
        ],
        "Nachmittag": [
            "🌿 Spaziergang durch den *Retiro-Park* mit Kristallpalast",
            "📖 Bummel durchs *Barrio de las Letras* (literarisches Viertel)"
        ],
        "Abendessen": [
            "🍷 *La Venencia* – authentisch, Sherry-Bar, keine Fotos erlaubt",
            "🥘 Alternativ: *Inclán Brutal* – kreative Tapas"
        ]
    },
    "Tag 3 – Lokale Viertel & Hidden Gems": {
        "Frühstück": [
            "☕ *Plántate Café* oder *The Fix* (Lavapiés)"
        ],
        "Vormittag": [
            "🎨 Erkundung von *Lavapiés*: Street Art, kleine Galerien, alternative Läden"
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
            "🛍️ Bummel über die *Gran Vía*, Shopping oder Cafébesuch",
            "🌇 Rooftop: *Círculo de Bellas Artes* (fantastischer Ausblick!)"
        ],
        "Mittagessen": [
            "🥘 *Lamucca de Pez* oder *Toma Jamón*"
        ],
        "Nachmittag": [
            "🕌 *Templo de Debod* – ägyptischer Tempel mit Sonnenuntergang",
            "🖼️ Optional: *Museo Sorolla* (klein & ruhig)"
        ],
        "Abendessen": [
            "🌿 *Botania* (gleich beim Hotel, stilvoll)",
            "🍄 *El Cisne Azul* – für Pilzliebhaber"
        ]
    },
        "Tag 5 - Montag - Abreise": {
            "Abreise": [
                "✈️ 6.20 Uhr Abflug Madrid Flughafen "
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

