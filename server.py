from flask import Flask, request, jsonify
import requests
import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    # Verifica se 'validToken' está presente nos dados
    if 'validToken' in data:
        return jsonify({'token': data['validToken']})
    else:
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

if __name__ == '__main__':
    app.run(debug=True)
