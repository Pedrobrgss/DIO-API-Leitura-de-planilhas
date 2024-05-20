from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Função para ler a planilha Excel
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')

@app.route('/read_excel', methods=['GET'])
def read_excel_api():
    file_path = request.args.get('file_path')
    if not file_path:
        return jsonify({"error": "File path is required"}), 400
    try:
        data = read_excel(file_path)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
