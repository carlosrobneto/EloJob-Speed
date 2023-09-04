from flask import Flask, render_template, url_for, request, redirect
import json

app = Flask(__name__)

def jsonToVar(nomeArquivo):
    with open('db/' + nomeArquivo + '.json', encoding="utf8") as json_file:
        varRetorno = json.load(json_file)
        return varRetorno

@app.route('/')
def home():
    servicos = jsonToVar("servicos")
    """ return servicos["Services"] """
    return render_template('home.html', cards=servicos["Services"]) 

@app.route('/discord')
def discord():
    return render_template('discord.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/contas')
def contas():
    return render_template('contas.html')


@app.route('/lol/elojob')
def elojobLol():
    elosLol = jsonToVar("elojob_lol")
    ligas = []
    for elos in elosLol["elos"]:
        ligas.append(elos["liga"])
    return render_template('/lol/elojob.html', elos=ligas, adicionais=elosLol["adicionais"])

@app.route('/lol/ws-elo/<elo_selecionado>', defaults={'div_sel': ""})
@app.route('/lol/ws-elo/<elo_selecionado>/<div_sel>')
def wsElo(elo_selecionado, div_sel):
    elosLol = jsonToVar("elojob_lol")
    divs = []
    img = ""
    tempoGasto = 0
    valPorMinuto = elosLol["valor_minuto"]
    for elo in elosLol["elos"]:
        if elo["liga"] == elo_selecionado:
            for div in elo["divisoes"]:
                divs.append(div["nome"])
                if img == "": 
                    if div_sel == "": 
                        img = div["img"]
                        tempoGasto = div["min"]
                    elif div_sel == div["nome"]:
                        img = div["img"]
                        tempoGasto = div["min"]

    return '{"divisoes":' + json.dumps(divs) + ',"img":"' + img + '", "tempoGasto":' + str(tempoGasto) + ', "valPorMinuto": ' + str(valPorMinuto) + '}'



@app.route('/lol/ws-preco/<seu_elo>/<elo_desejado>')
def wsPreco(seu_elo, elo_desejado):
    valor = 0
    return '{"Valor":' + str(valor) + '}'

@app.route('/lol/duoboost')
def duoboostLol():
    DuoboostLoL = jsonToVar("duoboost_lol")
    ligas = []
    for elos in DuoboostLoL["elos"]:
        ligas.append(elos["liga"])
    return render_template('/lol/duoboost.html', elos=ligas, adicionais=DuoboostLoL["adicionais"])

@app.route('/lol/ws-elo-duoboost/<elo_selecionado>', defaults={'div_sel': ""})
@app.route('/lol/ws-elo-duoboost/<elo_selecionado>/<div_sel>')
def wsEloDuoboostLoL(elo_selecionado, div_sel):
    DuoboostLoL = jsonToVar("duoboost_lol")
    divs = []
    img = ""
    tempoGasto = 0
    valPorMinuto = DuoboostLoL["valor_minuto"]
    for elo in DuoboostLoL["elos"]:
        if elo["liga"] == elo_selecionado:
            for div in elo["divisoes"]:
                divs.append(div["nome"])
                if img == "":
                    if div_sel == "":
                        img = div["img"]
                        tempoGasto = div["min"]
                    elif div_sel == div["nome"]:
                        img = div["img"]
                        tempoGasto = div["min"]

    return '{"divisoes":' + json.dumps(divs) + ',"img":"' + img + '", "tempoGasto":' + str(tempoGasto) + ', "valPorMinuto": ' + str(valPorMinuto) + '}'


@app.route('/lol/ws-preco-duoboost/<seu_elo>/<elo_desejado>')
def wsPrecoDuoboostLoL(seu_elo, elo_desejado):
    valor = 0
    return '{"Valor":' + str(valor) + '}'



@app.route('/valorant/elojob')
def elojobValorant():
    elosVaVa = jsonToVar("elojob_valorant")
    ligas = []
    for elos in elosVaVa["elos"]:
        ligas.append(elos["liga"])
    return render_template('/valorant/elojob.html', elos=ligas, adicionais=elosVaVa["adicionais"])

@app.route('/valorant/ws-eloV/<elo_selecionado>', defaults={'div_sel': ""})
@app.route('/valorant/ws-eloV/<elo_selecionado>/<div_sel>')
def wsEloValorant(elo_selecionado, div_sel):
    elosVaVa = jsonToVar("elojob_valorant")
    divs = []
    img = ""
    tempoGasto = 0
    valPorMinuto = elosVaVa["valor_minuto"]
    for elo in elosVaVa["elos"]:
        if elo["liga"] == elo_selecionado:
            for div in elo["divisoes"]:
                divs.append(div["nome"])
                if img == "":
                    if div_sel == "":
                        img = div["img"]
                        tempoGasto = div["min"]
                    elif div_sel == div["nome"]:
                        img = div["img"]
                        tempoGasto = div["min"]

    return '{"divisoes":' + json.dumps(divs) + ',"img":"' + img + '", "tempoGasto":' + str(tempoGasto) + ', "valPorMinuto": ' + str(valPorMinuto) + '}'

@app.route('/valorant/ws-precoV/<seu_elo>/<elo_desejado>')
def wsPrecoValorant(seu_elo, elo_desejado):
    valor = 0
    return '{"Valor":' + str(valor) + '}'




@app.route('/valorant/duoboost', methods = ['POST', 'GET'])
def duoboostValorant():
    if request.method == 'GET':
        elosVaVa = jsonToVar("duoboost_valorant")
        ligas = []
        for elos in elosVaVa["elos"]:
            ligas.append(elos["liga"])
        return render_template('/valorant/duoboost.html', elos=ligas, adicionais=elosVaVa["adicionais"])
    else:
        print("The Array is: ", request.form['eloCliente'])
        pedido = {}
        pedido['eloCliente'] = request.form['eloCliente']
        pedido["divCliente"] = request.form['divCliente']
        pedido["eloDesejado"] = request.form['eloDesejado']
        pedido["divDesejada"] = request.form['divDesejada']
        pedido["vitExtra"] = "Solicitado!" if "vitExtra" in request.form else "Nao Solicitado"
        pedido["amigo"] = "Solicitado!" if "amigo" in request.form else "Nao Solicitado"
        pedido["prioridade"] = "Solicitado!" if "prioridade" in request.form else "Nao Solicitado"

        """ converte em json """
        pedidoJson = json.dumps(pedido)
        """ salva o json no arquivo """
        with open('./pedidos/pedido.json', 'w') as outfile:
            json.dump(pedidoJson, outfile)
        return redirect("/compras")

@app.route('/valorant/ws-eloV/<elo_selecionado>', defaults={'div_sel': ""})
@app.route('/valorant/ws-eloV/<elo_selecionado>/<div_sel>')
def wsEloValorantDuo(elo_selecionado, div_sel):
    elosVaVa = jsonToVar("duoboost_valorant")
    divs = []
    img = ""
    tempoGasto = 0
    valPorMinuto = elosVaVa["valor_minuto"]
    for elo in elosVaVa["elos"]:
        if elo["liga"] == elo_selecionado:
            for div in elo["divisoes"]:
                divs.append(div["nome"])
                if img == "":
                    if div_sel == "":
                        img = div["img"]
                        tempoGasto = div["min"]
                    elif div_sel == div["nome"]:
                        img = div["img"]
                        tempoGasto = div["min"]

    return '{"divisoes":' + json.dumps(divs) + ',"img":"' + img + '", "tempoGasto":' + str(tempoGasto) + ', "valPorMinuto": ' + str(valPorMinuto) + '}'

@app.route('/valorant/ws-precoV/<seu_elo>/<elo_desejado>')
def wsPrecoValorantDuo(seu_elo, elo_desejado):
    valor = 0
    return '{"Valor":' + str(valor) + '}'

@app.route('/compras')
def compras():
    return render_template('/compras.html')

if __name__ == '__main__':
    app.run(debug=True)
