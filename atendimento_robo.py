from chatterbot import ChatBot


def executar_robo():
    Bot = ChatBot("Robô de Atendimento da Academia")
    
    while True:
        entrada = input("Bot: "+"digite alguma coisa: \n")
        resposta = Bot.get_response(entrada.lower())
        if resposta.confidence > 0.6:
            print("Bot: "+resposta.text)
        else:
            print("Bot: "+"ainda não sei como responder essa pergunta. ")
            print("Bot: "+"pergunte outra coisa?...\n")
            

if __name__ == "__main__":
    executar_robo()