import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Vigenère Cipher", page_icon="🔐", layout="centered")

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔐 Vigenère Cipher Tool</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Encrypt and decrypt messages using a keyword-based cipher</p>", unsafe_allow_html=True)

# --- Sidebar for Mode Selection ---
with st.sidebar:
    st.header("🔧 Settings")
    mode = st.radio("Choose a mode", ['Encrypt', 'Decrypt'])
    st.markdown("ℹ️ The **key** must match for both encryption and decryption.")

# --- Main Input Area ---
st.markdown("### ✉️ Message Input")
text = st.text_area("Enter your message below:", placeholder="Type your message here...")

st.markdown("### 🔑 Key Input")
key = st.text_input("Enter your secret key:", placeholder="Only alphabetic characters (e.g. lemon)")

# --- Cipher Logic ---
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

# --- Output ---
if text and key:
    if not key.isalpha():
        st.error("The key must only contain alphabetic characters.")
    else:
        result = encrypt(text, key.lower()) if mode == 'Encrypt' else decrypt(text, key.lower())
        st.success(f"🔓 Result ({mode}ed Message):")
        st.code(result, language="text")
