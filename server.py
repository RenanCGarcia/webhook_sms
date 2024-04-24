from flask import Flask, request, jsonify
import requests
import datetime

app = Flask(__name__)

@app.route('/pegar', methods=['GET', 'POST'])
def pegar():
    if request.method == 'GET':
        # Lógica para lidar com requisições GET
        return 'Recebido um pedido GET! Detalhes do Request:\n{}'.format(str(request))
        print("TOKEN?")
    # Verifica se 'validToken' está presente nos dados
    if 'validToken' in data:
        print("TEM TOKEN")
        return jsonify({'token': data['validToken']})
    elif request.method == 'POST':
        # Lógica para lidar com requisições POST
        data = request.json  # Supondo que os dados são enviados em formato JSON
        print("TOKEN?")
    # Verifica se 'validToken' está presente nos dados
    if 'validToken' in data:
        print("TEM TOKEN")
        return jsonify({'token': data['validToken']})
    else:
        print('SEM TOKEN')
        # Aqui você pode processar os dados recebidos
        return 'Recebido um pedido POST com os seguintes dados: {}\nDetalhes do Request:\n{}'.format(data, str(request))


if __name__ == '__main__':
    app.run(debug=True)


'''@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("TOKEN?")
    # Verifica se 'validToken' está presente nos dados
    if 'validToken' in data:
        print("TEM TOKEN")
        return jsonify({'token': data['validToken']})
    else:
        print('SEM TOKEN')
        return jsonify({'error': 'validToken not found'})

@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.json
    
    # Formata os dados para enviar para a API
    sms_data = {
        "id": data["id"],
        "to": data["to"],
        "message": data["text"],
        "schedule": datetime.datetime.now().isoformat(),
        "from": data.get("from", ""),
        "status": 0,  # Coloque o status desejado aqui
        "statusDescription": "",  # Descrição do status, se aplicável
        "carrier_name": data.get("carrier_name", "")  # Nome da operadora, se aplicável
    }

    print(sms_data)
    
    # Faz um POST para a API com os dados formatados
    api_url = 'URL_DA_SUA_API_AQUI'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, json=sms_data, headers=headers)
    
    # Verifica se a solicitação foi bem-sucedida e retorna a resposta da API
    if response.ok:
        return jsonify({"success": True, "response": response.json()}), 200
    else:
        return jsonify({"success": False, "error": response.text}), response.status_code
'''
'''if __name__ == '__main__':
    app.run(debug=True)'''
