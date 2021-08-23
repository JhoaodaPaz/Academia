from chatterbot import ChatBot
from difflib import SequenceMatcher
ACEITACAO = 0.70

def comparar_mensagens(mensagem, mensagem_candidata):
    confianca = 0.0

    if mensagem.text and mensagem_candidata.text:
        texto_mensagem = mensagem.text
        texto_mensagem_candidata = mensagem_candidata.text

        confianca = SequenceMatcher(
            None,
            texto_mensagem,
            texto_mensagem_candidata
        )
        confianca = round(confianca.ratio(), 2)
        if confianca < ACEITACAO:
            confianca = 0.0
    return confianca

def selecionar_resposta(mensagem, lista_respostas, storage=None):
    resposta = lista_respostas[0]

    return resposta



def executar_robo():
    bot = ChatBot("Robô de Atendimento do IFBA",
        read_only=True, 
        statement_comparison_function= comparar_mensagens,
        response_selection_method= selecionar_resposta,
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
            }
        ])

    while True:
        entrada = input("Bot: "+"digite alguma coisa: \n")
        
        resposta = bot.get_response(entrada.lower())
        if resposta.confidence > 0.0:
            print("Bot: "+resposta.text)
        else:
            print("Bot: "+"ainda nao sei como responder essa pergunta!")
            print("Bot: "+"pergunte outra coisa: ")
            

if __name__ == "__main__":
    executar_robo()