from nicegui import ui
import pandas as pd


"""
First case (just gives name of the uploaded file)
ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('max-w-full')
"""
#.set_content()
#.clear()
# Declaracion de Variables
relacion = dict()
u1=ui.html('People registered')

# Llamada a la interfaz web nicegui y llamada a funcion, una vez que carga excel
ui.upload(on_upload=lambda e: u1.set_content(read_pandas_excel(e.content.read())))
ui.label('People registered in the seminar')


def read_pandas_excel(f):
    """
    Lectura de Excel y  estructuras de datos
    """
    ui.html('')
    tabla=''
    print()
    print('People registered:')
    
    df = pd.read_excel(f, engine='openpyxl')
    df = df.iloc[:,[7,13,22]]
    df.columns = ['nombre','correo', 'pais']
    df = df.drop_duplicates(subset='nombre')
    df = df.drop_duplicates(subset='correo')

    #Relacion de Paises
    paises = set(df.iloc[:,2])

    #Efectivo Por Pais
    for pais in paises:
        #efectivo = df[df.iloc[:,1].str.contains(pais)].shape[0]
        efectivo = df[df.iloc[:,2]==pais].shape[0]
        relacion[pais]=efectivo
        #ui.label(pais, efectivo)
        tabla+=f'{pais} {efectivo} <br>'
        print(pais, efectivo)

    #Conversion a Pandas    
    df_total = pd.DataFrame(relacion.items(), columns=['Pais', 'Efectivo'])
    total = sum(df_total['Efectivo'])
    tabla+=f'Total {total}'
    print('Total', total)
    #ui.label(total)
    return str(tabla)
          
ui.run()
 
 
