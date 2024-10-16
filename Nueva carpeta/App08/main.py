import flet as ft


def main(page: ft.Page):
    page.window_width=800
    page.window_height=800
    
    page.bgcolor="black"
    page.title="Mictlan"
    page.fgcolor="gray"
    

#audios
    Intro=ft.Audio(src="Intro.mp3",volume=1,balance=0)
    page.overlay.append(Intro)
    
    Nivel1=ft.Audio(src="Primer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel1)

    Nivel2=ft.Audio(src="Segundo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel2)
    
    Nivel3=ft.Audio(src="Tercer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel3)
    
    Nivel4=ft.Audio(src="Cuarto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel4)
    
    Nivel5=ft.Audio(src="Quinto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel5)
    
    Nivel6=ft.Audio(src="Sexto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel6)
    
    Nivel7=ft.Audio(src="Septimo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel7)
    
    Nivel8=ft.Audio(src="Octavo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel8)
    
    Nivel9=ft.Audio(src="Noveno_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel9)
    
#Creamos la interfaz
    btnIntro=ft.FilledButton(text="Escucha el intro",disabled=False)

    img1=ft.Image(src="Primer-Nivel.jpeg",width=150,height=150)
    
    btnnivel1=ft.ElevatedButton(text="Primer Nivel")
    
    img2=ft.Image(src="Segundo-Nivel.jpeg",width=150,height=150)
    
    btnnivel2=ft.ElevatedButton(text="Segundo Nivel")
    
    img3=ft.Image(src="Tercer-Nivel.png",width=150,height=150)
    
    btnnivel3=ft.ElevatedButton(text="Tercer Nivel")
    
    img4=ft.Image(src="Cuarto-Nivel.jpeg",width=150,height=150)
    
    btnnivel4=ft.ElevatedButton(text="Cuarto Nivel")
    
    img5=ft.Image(src="Quinto-Nivel.jpeg",width=150,height=150)
    
    btnnivel5=ft.ElevatedButton(text="Quinto Nivel")
    
    img6=ft.Image(src="Sexto-Nivel.jpeg",width=150,height=150)
    
    btnnivel6=ft.ElevatedButton(text="Sexto Nivel")
    
    img7=ft.Image(src="Septimo-Nivel.jpeg",width=150,height=150)
    
    btnnivel7=ft.ElevatedButton(text="Septimo Nivel")
    
    img8=ft.Image(src="Octavo-Nivel.png",width=150,height=150)
    
    btnnivel8=ft.ElevatedButton(text="Octavo Nivel")
    
    img9=ft.Image(src="Noveno-Nivel.jpeg",width=150,height=150)
    
    btnnivel9=ft.ElevatedButton(text="Noveno Nivel")







ft.app(main)
