import nltk
import random
import string

# Download data untuk tokenisasi
nltk.download('punkt')

# Daftar pertanyaan dan jawaban
pairs = {
    "hai": ["Hai juga!", "Halo!", "Selamat datang!"],
    "apa kabar": ["Saya baik, terima kasih!", "Luar biasa, bagaimana denganmu?"],
    "siapa kamu": ["Saya chatbot buatan Python.", "Saya asisten virtual."],
    "terima kasih": ["Sama-sama!", "Kapan pun!"],
    "bye": ["Sampai jumpa!", "Dadah!", "Selamat tinggal!"],
    "nama kamu": ["Saya Risal", "Saya Robot Buatan", "Saya Robot Python"],
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))
    for key in pairs:
        if key in user_input:
            return random.choice(pairs[key])
    return "Maaf, saya tidak mengerti. Bisa ulangi?"

def start_chat():
    print("Chatbot: Halo! Ketik 'bye' untuk keluar.")
    while True:
        user_input = input("Kamu: ")
        if user_input.lower() in ["bye", "keluar", "exit"]:
            print("Chatbot:", random.choice(pairs["bye"]))
            break
        print("Chatbot:", chatbot_response(user_input))

if __name__ == "__main__":
    start_chat()
