import tkinter as tk
from PIL import ImageTk, Image
import base64


path = "topSecret_no_bg.png"

def encode(key, clear):
    result = ""
    for i in range(len(clear)):
        key_char = key[i % len(key)]
        encrypted_char = chr((ord(clear[i]) + ord(key_char)) % 256)
        result += encrypted_char
    return base64.b64encode(result.encode()).decode()


def decode(key, enc):
    try:
        enc = base64.b64decode(enc).decode()
        result = ""
        for i in range(len(enc)):
            key_char = key[i % len(key)]
            decrypted_char = chr((256 + ord(enc[i]) - ord(key_char)) % 256)
            result += decrypted_char
        return result
    except:
        return "Çözüm başarısız!"


def kaydet():
    title = titleEntry.get()
    message = textMessage.get("1.0", tk.END).strip()
    key = keyEntry.get()

    if title == "" or message == "" or key == "":
        print("Lütfen tüm alanları doldurun.")
        return

    encrypted_message = encode(key, message)

    with open("notlar.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"{title}\n{encrypted_message}\n")

    print("Not şifrelenip kaydedildi.")
    titleEntry.delete(0, tk.END)
    keyEntry.delete(0, tk.END)
    textMessage.delete("1.0", tk.END)


def desifre_et():
    encrypted_message = textMessage.get("1.0", tk.END).strip()
    key = keyEntry.get()

    if encrypted_message == "" or key == "":
        print("Lütfen şifreli mesajı ve anahtarınızı girin.")
        return

    decrypted = decode(key, encrypted_message)
    textMessage.delete("1.0", tk.END)
    textMessage.insert("1.0", decrypted)
    print("Şifre çözme tamamlandı.")


pencere = tk.Tk()
pencere.title("Secret Notes")
pencere.config(bg="grey")
pencere.minsize(200, 800)


img = Image.open(path)
img = img.resize((300, 200))
img = ImageTk.PhotoImage(img)

panel = tk.Label(pencere, image=img)
panel.image = img
panel.pack()

titleLabel = tk.Label(pencere, text="Enter Your Title")
titleLabel.pack(pady=20)

titleEntry = tk.Entry()
titleEntry.pack(side="top")
titleEntry.focus()

subtitleLabel = tk.Label(pencere, text="Enter Your Secret Notes")
subtitleLabel.pack(pady=25)

textMessage = tk.Text()
textMessage.pack(padx=60)

keyLabel = tk.Label(pencere, text="Enter Your Key (any text)")
keyLabel.pack(pady=20)

keyEntry = tk.Entry()
keyEntry.pack(side="top")

saveButton = tk.Button(pencere, text="Save and Encrypt", command=kaydet)
saveButton.pack(pady=10)

decryptButton = tk.Button(pencere, text="Decrypt", command=desifre_et)
decryptButton.pack(pady=10)

pencere.mainloop()
