import streamlit as st

st.set_page_config(page_title="Madrid Reiseplan", layout="wide")

# Titel
st.title("🌆 Madrid Reiseplan für 4 Tage")
st.markdown("**Für unsere Reise  ♥️ – mit viel Zeit für gutes Essen, Entspannung und Genuss.**")

# Reisedaten (einmal definieren)
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
            "🍷 Abendessen: *La Taberna de Elia* (klassisch & lokal)"
        ]
    },
    # [... Tag 2–4 wie gehabt ...]
}

tab1, tab2 = st.tabs(["Übersicht", "Editierbarer Plan"])

# === Übersicht ===
with tab1:
    for day, sections in itinerary.items():
        st.subheader(day)
        for section, items in sections.items():
            with st.expander(section, expanded=True):
                for item in items:
                    st.markdown(f"- {item}")

# === Editierbarer Plan ===
with tab2:
    st.warning("⚠️ Änderungen werden aktuell nicht gespeichert – bitte manuell kopieren bei Bedarf.")
    for day, sections in itinerary.items():
        st.subheader(day)
        for section, items in sections.items():
            with st.expander(section, expanded=True):
                for i, item in enumerate(items):
                    st.text_input(
                        f"{day} – {section} – {i+1}",
                        value=item,
                        key=f"{day}_{section}_{i}"
                    )

st.info("✨ Auf einen wundervollen Trip! Ich freue mich sehr ♥️")
