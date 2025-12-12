import ctypes
import os
import shutil

def install_font(font_path):
    # Folder font sistem Windows
    fonts_dir = os.path.join(os.environ['WINDIR'], 'Fonts')
    font_name = os.path.basename(font_path)
    dest_path = os.path.join(fonts_dir, font_name)

    # Salin file ke folder Fonts (jika belum ada)
    if not os.path.exists(dest_path):
        shutil.copy(font_path, dest_path)
        print(f"Font copied to: {dest_path}")
    else:
        print("Font already exists in system.")

    # Registrasi font ke sistem Windows
    ctypes.windll.gdi32.AddFontResourceW(dest_path)
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x001D, 0, 0)  # Memicu pembaruan font system
    print("Font registered successfully!")

# Contoh pemakaian:
install_font(r"D:/semester 2/Struktur Data dan Algoritma/Project/Pharmora/assets/fonts/RobotoFlex-VariableFont_GRAD,XOPQ,XTRA,YOPQ,YTAS,YTDE,YTFI,YTLC,YTUC,opsz,slnt,wdth,wght.ttf")
