import tkinter as tk
import instaloader as insta
from urllib.request import urlopen
from PIL import Image, ImageTk
import io


def get_profile():
    username = user_input.get().strip()
    if not username:
        status_label.config(text="❌ لطفاً نام کاربری وارد کنید!", fg="red")
        return

    try:
        L = insta.Instaloader()
        profile = insta.Profile.from_username(L.context, username)

        open_url = urlopen(profile.profile_pic_url)
        data = open_url.read()
        open_url.close()
        image = Image.open(io.BytesIO(data))
        image = image.resize((200, 200))  # تغییر سایز برای زیباتر شدن
        final = ImageTk.PhotoImage(image)

        profile_picture.config(image=final)
        profile_picture.image = final

        profile_followers.config(text=f"👥 فالوورها: {profile.followers}")
        profile_following.config(text=f"➡️ فالووینگ‌ها: {profile.followees}")
        profile_posts.config(text=f"📸 تعداد پست‌ها: {profile.mediacount}")

        status_label.config(text=f"✅ پروفایل  با موفقیت دریافت شد", fg="green")

    except Exception as e:
        status_label.config(text=f"❌ خطا: {e}", fg="red")


root = tk.Tk()
root.title("Instagram Profile Viewer")
root.geometry('500x700')
root.resizable(False, False)

label = tk.Label(root, text=' : آیدی اینستاگرام را وارد کنید', font=('Arial', 16, "bold"))
label.pack(pady=20)

user_input = tk.Entry(root, width=25, font=('Arial', 16))
user_input.pack(pady=5)

button = tk.Button(root, text='🔍 جستجو', width=20, font=("Arial", 14), command=get_profile, bg="#4CAF50", fg="white")
button.pack(pady=15)

profile_picture = tk.Label(root)
profile_picture.pack(pady=15)

profile_followers = tk.Label(root, text="", font=("Arial", 14))
profile_followers.pack(pady=5)

profile_following = tk.Label(root, text="", font=("Arial", 14))
profile_following.pack(pady=5)

profile_posts = tk.Label(root, text="", font=("Arial", 14))
profile_posts.pack(pady=5)

status_label = tk.Label(root, text="", font=("Arial", 12))
status_label.pack(pady=10)

root.mainloop()
