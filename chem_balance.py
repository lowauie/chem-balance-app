import streamlit as st
from chempy import balance_stoichiometry

st.set_page_config(page_title="Chemical Equation Balancer")

st.title("⚗️ Chemical Equation Balancer")
st.markdown("**Developed by Reem Mousa Al-Qahtani**")

st.markdown("Enter an unbalanced chemical equation. Example: `H2 + O2 -> H2O`")

user_input = st.text_input("Unbalanced Equation", "")

if user_input:
    try:
        reactants_str, products_str = user_input.split("->")
        reactants = [r.strip() for r in reactants_str.split("+")]
        products = [p.strip() for p in products_str.split("+")]
        reac, prod = balance_stoichiometry(set(reactants), set(products))
        balanced_eq = " + ".join(f"{reac[r]} {r}" for r in reac) + " -> " + " + ".join(f"{prod[p]} {p}" for p in prod)
        st.success(f"✅ Balanced Equation:\n\n**{balanced_eq}**")
    except Exception as e:
        st.error(f"❌ Error balancing equation: {e}")
