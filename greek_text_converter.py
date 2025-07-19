import streamlit as st
import random
import pandas as pd

# Load the mapping from CSV (assuming it's in the same directory)
mapping_df = pd.read_csv("English-Greek-Latin_Mapping_Table.csv")

# Build replacement dictionary with possible variants
replacement_map = {}

for _, row in mapping_df.iterrows():
    en_upper = row['English Upper']
    en_lower = row['English Lower']
    gr_upper = row['Greek Upper'] if pd.notna(row['Greek Upper']) and row['Greek Upper'] != "" else None
    gr_lower = row['Greek Lower'] if pd.notna(row['Greek Lower']) and row['Greek Lower'] != "" else None

    if gr_upper:
        replacement_map.setdefault(en_upper, []).append(gr_upper)
    if gr_lower:
        replacement_map.setdefault(en_lower, []).append(gr_lower)

# Streamlit UI
st.title("🔤 English to Greek Letter Converter")
st.markdown("Enter English text below to convert letters using Greek equivalents. Each letter will be replaced randomly if multiple variants exist.")

input_text = st.text_area("Enter text:", height=150)

if st.button("Convert"):
    output = ""
    for char in input_text:
        if char in replacement_map:
            output += random.choice(replacement_map[char])
        else:
            output += char

    st.subheader("Converted Output:")
    st.code(output, language='text')
