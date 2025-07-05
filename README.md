# 🗝️ Secret Notes – Simple Encrypted Notes App

This Python project allows users to securely save their private notes by encrypting them with a custom key, and later decrypting them using the same key.  
It's designed as a beginner-friendly project combining **Tkinter GUI** with a basic **encryption algorithm**.

---

## 🎯 Features

- Input fields for title, message, and encryption key
- Encrypts messages and saves them to `notlar.txt`
- Allows decryption of saved messages using the correct key
- Clean and minimal user interface (built with Tkinter)
- Optional background image for visual appeal

---

## 🔐 Encryption Method

The app uses a simple character-shifting (Vigenère-like) encryption method combined with **Base64 encoding**.  
This method is for **educational purposes only** and should not be used in real-world secure systems.

---

## 🛠️ Requirements

- Python 3.x
- Pillow (for background image support)

```bash
pip install pillow
