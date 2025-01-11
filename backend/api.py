# Servidor Flask para gerenciar o backend.
from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/atualizar-dados', methods=['POST'])
def atualizar_dados():
    try:
        subprocess.run(['python', 'backend/atualizar_dados.py'], check=True)
        return jsonify({"message": "Atualizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)