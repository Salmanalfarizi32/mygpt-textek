import streamlit as st
import pandas as pd
import random

# --- Page config & custom style (letakkan di sini paling atas) ---
st.set_page_config(
    page_title="Textek.id",
    page_icon="🟢",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    .big-title {
        font-size: 60px;
        color: #0b6623;  /* hijau gelap */
        font-weight: bold;
        text-align: center;
        margin-top: 50px;
    }
    .stApp {
        background-color: #ffffff;  /* putih */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="big-title">Textek.id</div>', unsafe_allow_html=True)

# --- Load QnA database ---
qna_df = pd.read_csv("qna.csv")
examples = qna_df['Jawaban'].tolist()  # gunakan jawaban sebagai reference content

<<<<<<< HEAD
# --- Streamlit UI ---
st.set_page_config(page_title="MyGPT - Content Agent", layout="centered")

=======
>>>>>>> 7b8970e (Update UI: tambah Textek.id header + tema hijau-putih)
# --- Sidebar Settings ---
with st.sidebar:
    st.header("Settings")
    n_examples = st.number_input("Jumlah contoh referensi", min_value=1, max_value=10, value=3)
    n_variations = st.number_input("Jumlah variasi di-generate", min_value=1, max_value=10, value=3)
    show_examples = st.button("Lihat semua jawaban tersimpan")

if show_examples:
    st.subheader("Jawaban dari QnA database")
    st.table(pd.DataFrame({'examples': examples}))

# --- Simple Search QnA ---
st.subheader("Tanya MyGPT (database QnA)")
user_question = st.text_input("Tanya apa aja seputar fashion / hijab:")

if user_question:
    matches = qna_df[qna_df["Pertanyaan"].str.contains(user_question, case=False, na=False)]
    if not matches.empty:
        st.write("**Jawaban MyGPT:**")
        st.write(matches.iloc[0]["Jawaban"])
    else:
        st.write("Maaf, aku belum punya jawaban di database. Coba tanyakan dengan kata lain.")

# --- Agent Prototype (variations generator) ---
def retrieve_examples(n=3):
    return random.sample(examples, min(n, len(examples)))

def generate_variations(base_prompt, num=3):
    ctas = ["Ayo coba sekarang!", "Stok terbatas.", "Dapatkan diskon spesial.", "Pesan sekarang!"]
    variations = []
    for _ in range(num):
        ex = random.choice(examples)
        variations.append(f"{base_prompt} {ex} {random.choice(ctas)}")
    return variations

def rank_variations(variations):
    target_len = 60
    scored = []
    for v in variations:
        score = -abs(len(v) - target_len)
        if any(k in v.lower() for k in ["diskon","pesan","stok","coba","dapatkan"]):
            score += 5
        scored.append((v, score))
    scored.sort(key=lambda x: x[1], reverse=True)
    return [v for v,_ in scored]

st.subheader("Agent Content Generator")
prompt = st.text_area("Masukkan contoh konten sukses / brief:", height=120)

if st.button("Run Agent"):
    if not prompt.strip():
        st.error("Isi prompt dulu.")
    else:
        refs = retrieve_examples(n_examples)
        st.write("**Referensi yang diambil:**")
        for r in refs:
            st.write("- " + r)

        variations = generate_variations(prompt, num=n_variations)
        st.write("**Variasi yang di-generate:**")
        for i,v in enumerate(variations, start=1):
            st.write(f"{i}. {v}")

        ranked = rank_variations(variations)
        st.write("**Rekomendasi terbaik:**")
        st.info(ranked[0])
