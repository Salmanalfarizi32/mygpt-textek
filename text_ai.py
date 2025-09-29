import random

# Dataset kecil contoh caption sukses
captions = [
    "Kain elegan dengan kenyamanan maksimal, cocok untuk acara spesial!",
    "Rasakan sentuhan mewah setiap kali mengenakan kain premium kami.",
    "Pilihan tepat untuk tampil stylish dan tetap nyaman seharian.",
    "Kain berkualitas tinggi dengan harga terjangkau, jangan lewatkan!",
    "Bahan adem, lembut, dan elegan — cocok untuk segala suasana."
]

# Fungsi generator sederhana
def generate_caption(base_prompt):
    base = random.choice(captions)
    return f"{base_prompt} {base}"

# Prompt dari user
prompt = "Tuliskan caption promosi untuk produk kain:"
print("Generated Text:")
print(generate_caption(prompt))
