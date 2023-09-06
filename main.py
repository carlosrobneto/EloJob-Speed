from flask import Flask, render_template, url_for, request, redirect
import json

app = Flask(__name__)

def jsonToVar(nomeArquivo):
    with open('db/' + nomeArquivo + '.json', encoding="utf8") as json_file:
        varRetorno = json.load(json_file)
        return varRetorno

@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/suporte')
def discord():
    return render_template('suporte.html')

@app.route('/contas')
def contas():
    return render_template('contas.html')

@app.route('/lol/coach')
def coachLol():
    elosLol = jsonToVar("coach_lol")
    ligas = []
    for elos in elosLol["elos"]:
        ligas.append(elos["liga"])
    return render_template('/lol/coach.html', elos=ligas, adicionais=elosLol["adicionais"])

@app.route('/lol/ws-elo-coach/<elo_selecionado>', defaults={'div_sel': ""})
@app.route('/lol/ws-elo-coach/<elo_selecionado>/<div_sel>')
def wscoach(elo_selecionado, div_sel):
    elosLol = jsonToVar("coach_lol")
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
def wsPrecocoach(seu_elo, elo_desejado):
    valor = 0
    return '{"Valor":' + str(valor) + '}'






@app.route('/lol/md5')
def md5Lol():
    elosLol = jsonToVar("md5_lol")
    ligas = []
    for elos in elosLol["elos"]:
        ligas.append(elos["liga"])
    return render_template('/lol/md5.html', elos=ligas, adicionais=elosLol["adicionais"])

@app.route('/lol/ws-elo-md5/<elo_selecionado>', defaults={'div_sel': ""})
@app.route('/lol/ws-elo-md5/<elo_selecionado>/<div_sel>')
def wsMd5(elo_selecionado, div_sel):
    elosLol = jsonToVar("md5_lol")
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
def wsPrecoMD5(seu_elo, elo_desejado):
    valor = 0
    return '{"Valor":' + str(valor) + '}'



@app.route('/lol/vitorias')
def vitoriasLol():
    elosLol = jsonToVar("vitorias_lol")
    ligas = []
    for elos in elosLol["elos"]:
        ligas.append(elos["liga"])
    return render_template('/lol/vitorias.html', elos=ligas, adicionais=elosLol["adicionais"])

@app.route('/lol/ws-elo-vitorias/<elo_selecionado>', defaults={'div_sel': ""})
@app.route('/lol/ws-elo-vitorias/<elo_selecionado>/<div_sel>')
def wsVitorias(elo_selecionado, div_sel):
    elosLol = jsonToVar("vitorias_lol")
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
def wsPrecoVitorias(seu_elo, elo_desejado):
    valor = 0
    return '{"Valor":' + str(valor) + '}'




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


if __name__ == '__main__':
    app.run(debug=True)
