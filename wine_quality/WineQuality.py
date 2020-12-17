import pickle

class WineQuality(object):
    def __init__(self):  # essa funcao 'init' é inicializada automaticamente quando a classe é instanciada
        self.free_sulfur_dioxide_scaler = pickle.load( open( 'parameter/free_sulfur_dioxide_scaler.pkl', 'rb' ) )
        self.total_sulfur_dioxide_scaler = pickle.load( open( 'parameter/total_sulfur_dioxide_scaler.pkl', 'rb' ) )

    # aqui podemos criar qualquer preparacao de dados: limpeza, scaler, encoding e etec...
    def data_preparation(self,df):  # Transforma os novos dados recebidos
        df['free sulfur dioxide'] = self.free_sulfur_dioxide_scaler.transform(df[['free sulfur dioxide']].values)
        df['total sulfur dioxide'] = self.total_sulfur_dioxide_scaler.transform(df[['total sulfur dioxide']].values)
    
        return df