# app.py
import streamlit as st
from ai import suggest_restaurant_names, suggest_menu_for_name, suggest_names_and_menus

st.set_page_config(page_title="Restaurant Name Generator", page_icon="🍽️")

st.title("🍽️ Restaurant Name Generator")

st.markdown(
    "Generate brandable restaurant names and instant menu ideas.\n"
    "Powered by OpenAI + LangChain."
)

# --- Sidebar controls ---
with st.sidebar:
    st.header("Preferences")
    cuisine = st.text_input("Cuisine", value="Pakistani")
    tone = st.selectbox(
        "Vibe / Tone",
        ["Modern", "Classic", "Rustic", "Luxury", "Street", "Family", "Minimal", "Fusion", "Coastal", "Urban"],
        index=0
    )
    n_names = st.slider("How many names?", 1, 20, 8, step=1)
    n_menu_items = st.slider("Menu items per name", 4, 20, 10, step=1)
    mode = st.radio("Mode", ["Names only", "Names + Menus"], index=1)

col1, col2 = st.columns([1,1])

with col1:
    if st.button("Generate"):
        with st.spinner("Cooking ideas…"):
            try:
                if mode == "Names only":
                    names = suggest_restaurant_names(cuisine=cuisine, tone=tone, count=n_names)
                    st.subheader("Suggested Names")
                    for i, n in enumerate(names, start=1):
                        st.write(f"{i}. **{n}**")
                else:
                    results = suggest_names_and_menus(
                        cuisine=cuisine,
                        tone=tone,
                        n_names=n_names,
                        n_menu_items=n_menu_items
                    )
                    st.subheader("Names + Menus")
                    for i, item in enumerate(results, start=1):
                        st.markdown(f"**{i}. {item['name']}**")
                        st.write(", ".join(item["menu"]))
                        st.divider()
            except Exception as e:
                st.error(f"Error: {e}")

with col2:
    st.markdown("### Tips")
    st.markdown(
        "- Check domain & social handle availability.\n"
        "- Say it out loud — easy to pronounce?\n"
        "- Avoid tongue-twisters and clichés.\n"
        "- Keep it legally clear (trademarks!)."
    )

