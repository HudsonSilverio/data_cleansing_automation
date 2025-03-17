from flask import Flask, request, render_template, send_file
import pandas as pd
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

# Criar diretórios se não existirem
for folder in [UPLOAD_FOLDER, PROCESSED_FOLDER]:
    os.makedirs(folder, exist_ok=True)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado!", 400
    
    file = request.files['file']
    if file.filename == '':
        return "Nome de arquivo inválido!", 400
    
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    # Processar o CSV para remover e-mails
    processed_filepath = process_csv(filepath, file.filename)
    
    return f"Arquivo processado com sucesso! <a href='/download/{file.filename}'>Baixar arquivo limpo</a>"

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(PROCESSED_FOLDER, filename), as_attachment=True)

def process_csv(filepath, filename):
    df = pd.read_csv(filepath)
    df = df.applymap(lambda x: '' if isinstance(x, str) and '@' in x else x)  # Remove e-mails
    processed_filepath = os.path.join(PROCESSED_FOLDER, filename)
    df.to_csv(processed_filepath, index=False)
    return processed_filepath

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# poetry run app.py