import streamlit as st

st.title("Caesar's Cipher")
mode = st.radio("Choose mode:", ("Encrypt", "Decrypt"))
user_input = st.text_input("Enter message to encrypt:")
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if not char.isalpha():
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text
if mode == "Encrypt":
    result = caesar(user_input, shift)
    st.write("🔐 Encrypted text:", result)
else:
    result = caesar(user_input, -shift)
    st.write("🔓 Decrypted text:", result)