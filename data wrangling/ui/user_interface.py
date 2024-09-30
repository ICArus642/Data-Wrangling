import matplotlib.pyplot as plt
from tabulate import tabulate

#solo admite bibliotecas
def impresion_datos_extraidos (results_df):

    print(tabulate(results_df, tablefmt="github", headers=["Número de registro", "Ciudad de ubicación","Departamento", "Edad", "Tipo", "Estado", "País de procedencia"]))
    
def impresion_estadistica (results_df):
    print(results_df.describe())
    
def impresion_grafica (results_df):
    results_df['edad'].value_counts().plot(kind='bar')
    plt.xlabel('edad')
    plt.ylabel('Número de casos')
    plt.title('Número de casos por edad')
    plt.show()
