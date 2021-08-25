from operator import itemgetter
import speech_recognition as sr
import time
import os
import wave
import contextlib
import soundfile as sf

#Definimos la función que analizará el audio y texto como entrada será el texto
def interface():
    print("-----------------------------------------------------------------------------")
    print("    ████████╗███████╗██╗  ██╗████████╗██╗   ██╗██╗██╗     ██╗      █████╗    ")
    print("    ╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝██║   ██║██║██║     ██║     ██╔══██╗   ")
    print("       ██║   █████╗   ╚███╔╝    ██║   ██║   ██║██║██║     ██║     ███████║   ")
    print("       ██║   ██╔══╝   ██╔██╗    ██║   ╚██╗ ██╔╝██║██║     ██║     ██╔══██║   ")
    print("       ██║   ███████╗██╔╝ ██╗   ██║    ╚████╔╝ ██║███████╗███████╗██║  ██║   ")
    print("       ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝     ╚═══╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ")
    print("   Analizador de discursos por voz y texto -- by: troyaninfec and cazalmas   ")
    print("-----------------------------------------------------------------------------")
def analizador(texto):
    quitar = "?;¿:_-¡.,\n!\"'"
    for caracter in quitar:
        texto = texto.replace(caracter," ")
    texto = texto.lower()
    palabras = texto.split()
    palabras_new = []
    conectores= ("y","no","por","nos","el","lo","es","las","la","un","a","u","de","los","para","que","en","del","con","una","se","al","ha")
    for e in palabras:
        if e not in conectores:
            palabras_new.append(e)
    palabras = palabras_new

    diccionario_frecuencias = {}
    for palabra in palabras:
        if palabra in diccionario_frecuencias:
            diccionario_frecuencias[palabra] += 1
        else:
            diccionario_frecuencias[palabra] = 1
    diccionario_frecuencias = dict(sorted(diccionario_frecuencias.items(),key=itemgetter(1),reverse=True))
    total_procentaje=len(palabras)
    for palabra in diccionario_frecuencias:
        frecuencia = diccionario_frecuencias[palabra]
        porcentaje = (frecuencia*100)/total_procentaje
        print(" ",palabra,"{0:.2f}".format(porcentaje),"%",frecuencia,"veces")
interface()
time.sleep(2)
os.system('cls')
interface()
print(" 1)Analizar por audio (wav)")
print(" 2)Analizar por texto (txt)")
print(" 3)Analizar por microfono  ")
print(" 4)Salir")
option = int(input(" Selecione una opción: "))
if option == 1:
    os.system('cls')
    interface()
    ruta_audio = input(" Ingrese la ruta del archivo .wav: ")
    duration = sf.SoundFile(ruta_audio)
    duration = len(duration) / duration.samplerate
    r = sr.Recognizer()
    with sr.AudioFile(ruta_audio) as source:
        audio = r.listen(source)
        try:
            os.system('cls')
            interface()
            print(" Analizando audio ...")
            texto_audio = r.recognize_google(audio, language="es-ES")
            time.sleep(duration)
            os.system('cls')
            interface()
            print(" Resultados:")
            f = open('Audio_convertido.txt', 'w')
            f.write(texto_audio)
            print("")
            print(" Audio convertido a txt y guardado con el nombre: Audio_convertido.txt")
            print("")
            analizador(texto_audio)
        except:
            print("No se cargo el audio")
elif option == 2:
    os.system('cls')
    interface()
    ruta_texto = input(" Ingrese la ruta del archivo .txt:")
    texto = open (ruta_texto,'r',encoding="utf8")
    texto_txt = texto.read()
    os.system('cls')
    interface()
    print(" Resultados:")
    print("")
    analizador(texto_txt)
elif option == 3:
    os.system('cls')
    interface()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Te estoy escuchando:) ')
        audio = r.listen(source)
        try:
            os.system('cls')
            interface()
            print(" Analizando audio ...")
            texto = r.recognize_google(audio, language="es-ES")
            os.system('cls')
            interface()
            print(" Resultados:")
            f = open('Audio_convertido.txt', 'w')
            f.write(texto)
            print("")
            print(" Audio convertido a txt y guardado con el nombre: Audio_convertido.txt")
            print("")
            analizador(texto)
        except:
            print('No te pude escuchar:(')
elif option == 4:
    print("     _                        ")
    print("    / )                       ")
    print("   / /                        ")
    print("  / /               /\        ")
    print(" / /. - ```-. / ^ `-.         ")
    print(" \ \    /       \_/  (|) `o   ")
    print("  \ \  /   .-.   \\ _  ,--'   ")
    print("   \ \/   /   )   \( `^^^     ")
    print("    \   \/    (    )          ")
    print("     \   )     )  /           ")
    print("      ) /__    | (__          ")
    print("     (___)))   (__)))         adios ...")
    time.sleep(3)
    os.system('cls')
    os.system('exit')
else:
    print("No es una opción valida")

