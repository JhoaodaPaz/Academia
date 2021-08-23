from atendimento_robo import *
from flask import Flask

VERSAO = "1.0"

Bot = ChatBot("Robô de Atendimento da Academia",
    read_only=True, 
    )
servico_robo = Flask(__name__)

@servico_robo.route("/versao", methods=["GET"])
def get_verso():
    return VERSAO

@servico_robo.route("/resposta/<mensagem>", methods=["GET"])
def get_resposta(mensagem):
    resposta = Bot.get_response(mensagem)

    return resposta.text

if __name__ == "__main__":
    servico_robo.run()