import speech_recognition as sr


def listen_mic():
    mic = sr.Recognizer()  # habilita o microfone para ouvir o usuário
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)  # reduz o ruído com uma função do SpeechRecognition
        print(
            "Fale uma frase (o reconhecimento pode demorar alguns segundos...) ")  # espera a entrada de voz do usuário
        audio = mic.listen(source)  # armazena o áudio numa variável

    try:
        phrase = mic.recognize_google(audio, language='pt-BR')  # passa o áudio para o reconhecedor do SpeechRecognition
        print("Sua frase foi: \"" + phrase + "\"")  # retorna a frase dita

    except sr.UnkownValueError:  # mensagem de erro para caso não conseguir reconhecer o padrão de fala
        print("Não entendi o que você disse")

    return phrase


listen_mic()
