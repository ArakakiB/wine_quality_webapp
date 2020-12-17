from flask import Flask, request
import pickle
import pandas as pd
import os

# importando classes
from wine_quality.WineQuality import WineQuality  # para o heroku add o .WineQuality

# Carregando o modelo
# rb - read
# colocamos o model aqui para quando ele iniciar o modelo já estar na memoria e o carregamento ser rapido
model = pickle.load(open('model/modelo.pkl', 'rb'))  # Aqui para o heroku sera so "model"

app = Flask(__name__)

# /predict é a pagina que vamos acessar, poderia ter dado qualquer nome
# POST porque vamos escrever (postar)
@app.route( '/predict', methods=['POST'] )  # vai para a funcao predict

def predict():
    test_json = request.get_json()  # recebe o json
    
    # coletando os dados
    if test_json:  # testa para saber se o json esta vazio ou nao
        if isinstance( test_json, dict ):
            df_raw = pd.DataFrame( test_json, index[0] )
        else:
            df_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
    
    # usando a classe e passando para uma variavel/objeto
    pipeline = WineQuality()  # Classe
    
    df1 = pipeline.data_preparation(df_raw)  # data_preparation - Funcao da classe
    
    # predicao
    pred = model.predict( df1 )  # predicao normal
    
    df1['prediction'] = pred  # prepara para o cliente a predicao em uma nova col
    return df1.to_json( orient='records' )  # passa de dataframe para json e retorna
    #response = df_raw['prediction'] = pred
    #return response
    
if __name__ == '__main__':
    # Iniciando o flask
    # host é o endereco, nesse caso estamos passado o da maquina.
    # port - é a porta. Poderia ser qualquer numero
    
    # para o heroku:
    port = os.environ.get('PORT',5000)
    app.run( host='127.0.0.1', port=port )
    
    
# agora teoricamente é so rodarmos local. é so colocar "python app.py" no cmd do anaconda. Lembre-se de ver se o flask esta instalado
# lembre-se de executar o arquivo na pasta em que esta o app.py
    
    
    
    
    