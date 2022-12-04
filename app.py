from flask import Flask, render_template, request
from decimal import Decimal
from fractions import Fraction
import numpy as np

app = Flask(__name__)

############# Funciones ###########################
def crear_matriz_string(filas,columnas): #hacer una matriz nxn llena de "" en todas sus posiciones
    if filas > 1:
        return [["" for j in range(columnas)] for i in range(filas)]
    elif filas == 1:
        return ["" for i in range(columnas)]

def crear_matriz_numeros(filas,columnas):
    return np.array([[0 for j in range(columnas)] for i in range(filas)],float) #hacer una matriz numpy nxn llena de 0. en todas sus posiciones

def convertir_decimal_fraccion(matriz): #convierte una matriz numpy a la versión de ella misma pero con fracciones en lugar de números decimales
    filas = matriz.__len__()
    columnas = 0
    for i in matriz:
        columnas = i.__len__()

    resultado = crear_matriz_string(filas,columnas)
    for i in range(len(resultado)):
        for j in range(len(resultado[i])):
            numero = round(matriz[i][j],3)
            racional = Fraction(numero).limit_denominator()
            resultado[i][j] = str(racional)  
    return resultado

def convertir_inputs_decimal(matriz): #convierte una matriz de strings a su respectiva version de matriz numpy
    filas = matriz.__len__()
    columnas = 0
    for i in matriz:
        columnas = i.__len__()

    matriz_final = crear_matriz_numeros(filas,columnas)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numero = matriz[i][j]
            try:
                numero = float(numero)
                matriz_final[i][j] = numero
            except:
                numero_split = numero.split("/")
                primer_numero = numero_split[0]
                segundo_numero = numero_split[1]
                resultado = round(float(int(primer_numero)/int(segundo_numero)),5)
                matriz_final[i][j] = resultado
    return matriz_final

def convertir_decimal_fraccion_vector(vector):
    vector_resultado = crear_matriz_string(1,len(vector))  
    for i in range(len(vector)):
        numero = round(vector[i],3)
        racional = Fraction(numero).limit_denominator()
        vector_resultado[i] = str(racional)
    return vector_resultado


def rad_a_ang(angulo):
    ang_final = angulo*180/np.pi
    return round(ang_final,2)

def det(matrizA):
    return np.linalg.det(matrizA)

def sumar_matrices(matriz_a,Matriz_b): #suma de 2 matrices
    try:
        suma = matriz_a+Matriz_b
        return suma
    except:
        error ="No es posible la suma de estas matrices"
        return error
def restar_matrices(matriz_a,matriz_b): #resta de 2 matrices
    try:
        suma = matriz_a-matriz_b
        return suma
    except:
        error ="No es posible la suma de estas matrices"
        return error

def multiplicar_matrices(matriz_a,matriz_b): # multiplicar 2 matrices
    try:
        multiplicacion = matriz_a @ matriz_b
        return multiplicacion
    except:
        return "Las matrices no tienen el tamaño adecuado para ser multiplicadas"

def traza(matriz): ## Traza de una matriz
    try:
        traza = matriz.trace()
        return traza
    except:
        return "Invalido"

def traspuesta(matriz): # Transpuesta de una matriz 
    try:
        traspuesta = matriz.T
        return traspuesta
    except:
        return "Invalido"

def multiplicar_por_escalar(escalar,matriz_a): #multiplicar una matriz por un escalar
    try:
        multiplicacion= escalar*matriz_a
        return multiplicacion
    except:
        error = "No es posible hacer esta operación"
    return error

def calcular_matriz_inversa(matriz_a): #calcular la matriz inversa de una matriz
    try:
        matriz_inversa = np.linalg.inv(matriz_a)
        inversa_real = convertir_decimal_fraccion(matriz_inversa)
        return inversa_real
    except:
        return "Esta matriz no tiene inversa"

def calcular_norma(vector): #calcula la norma o magnitud de un vector
    try:
        norma = np.linalg.norm(vector)
        return norma
    except:
        return "No se puede calcular la norma de este vector"


def direccion_vector(vector): # Dirección de un vector
    n_elementos = 0
    for i in vector:
        n_elementos += 1
    if n_elementos == 2:
        a = vector[0]
        b = vector[1]
        angulo = 0
        arco = np.arctan(b/a)
        if a > 0 and b > 0:
            angulo = arco
            return rad_a_ang(angulo)
        elif a < 0 and b > 0:
            angulo = arco
            return rad_a_ang(angulo)
        elif a < 0 and b < 0:
            angulo = np.arctan(b/a)
            return -180+rad_a_ang(angulo)
        elif a > 0 and b < 0:
            angulo = np.arctan(b/a)
            return 180+rad_a_ang(angulo)
    if n_elementos == 3:
        pass
    else:
        return "No se puede calcular la dirección para este vector"

def calcular_vector_unitario(vector): #calcula el vector unitario de un vector
    try:
        vec_unitario = vector/calcular_norma(vector)
        return vec_unitario
    except:
        return "No se puede"

def producto_punto(vector_a,vector_b): #producto punto de dos vectores
    try:
        producto_punto = np.dot(vector_a,vector_b)
        return producto_punto
    except:
        error = "No se puede hacer el producto punto entre estos vectores"
        return error
def scal(u,v):
    return np.vdot(u,v)

def unit(u):
    return 1/np.sqrt(scal(u,u))*u
def Gram_Schmidt(L1):
    L2 = [unit(L1[0])]
    for i in range(1,len(L1)):
        s=L1[i]
        for j in range(i):
            s = s-scal(L1[i],L2[j])*L2[j]
        L2.append(unit(s))
    return convertir_decimal_fraccion(L2) 

def calcular_valores_propios(matriz): #Calcula los valores propios de una matriz
    try:
        valores = np.linalg.eigvals(matriz)
        return convertir_decimal_fraccion_vector(valores)  
    except:
        return "Ha ocurrido un error"

def calcular_vectores_propios(matriz): #calcula los vectores propios de una matriz
    try:
        valores,vectores = np.linalg.eig(matriz)
        return convertir_decimal_fraccion(vectores) 
    except:
        return "Ha ocurrido un error"


## GJ 
#---------------- métodos para la reducción por Gauss Jordan----------------------------------
def gauss_Jorda_p1(matriz_t, matriz_r):
    def div_pivote(fila,resultado,nf):
        num=fila[nf]
        if num!=0:
            resultado[nf]=resultado[nf]/num
            for i in range(len(fila)):
                fila[i]=fila[i]/num

        return fila, resultado
    
    def suma_filas(m1,m2,resultado,nf,nr):
        num=m2[nf]
        m_temp=[]
        m_temp_r=[]
        for i in range(len(m1)):
            m_temp.append(m1[i])
        for i in range(len(resultado)):
            m_temp_r.append(resultado[i])
    
        if num<0:
            num=num*-1
        for i in range(len(m_temp)):    
            m_temp[i] = m_temp[i]*num
            
        if m2[nf]>0:
            resultado[nr]=resultado[nr]-(num*m_temp_r[nf])
            for i in range(len(m2)):
                m2[i]=m2[i]-m_temp[i]
                
        else:
            resultado[nr]=resultado[nr]+(num*m_temp_r[nf])
            for i in range(len(m2)):
                m2[i]=m2[i]+m_temp[i]
        return m2, resultado
    recorrido=0
    recorrido2=0

    if len(matriz_t)>=len(matriz_t[0]):
        recorrido=len(matriz_t)
        recorrido2=len(matriz_t[1])
    
    if len(matriz_t)<len(matriz_t[0]):
        recorrido=len(matriz_t)
        recorrido2=len(matriz_t[1])
    
    cont=0
    
    for i in range(recorrido):

        
        matriz_t[i]=div_pivote(matriz_t[i],matriz_r,cont)[0]
        matriz_r=div_pivote(matriz_t[i],matriz_r,cont)[1]

            
        for j in range(i+1,recorrido):

            if i>=len(matriz_t[0]) and len(matriz_t)!=len(matriz_t[0]):

                break
            matriz_t[j]= suma_filas(matriz_t[i], matriz_t[j],matriz_r,i,j)[0]
            matriz_r= suma_filas(matriz_t[i], matriz_t[j],matriz_r,i,j)[1]

        if cont!=recorrido2-1:    
            cont=cont+1

    

    matrizfinal=matriz_t
    matrizresultado=matriz_r

    def suma_columna2(m1, m2, resultado, cont_col,nr):
        
        
        num=m2[cont_col]
        m_temp=[]
        m_temp_r=[]
        for i in range(len(m1)):
            m_temp.append(m1[i])
        for i in range(len(resultado)):
            m_temp_r.append(resultado[i])
        if num<0:
            num=num*-1
    
        for i in range(len(m_temp)):
            m_temp[i] = m_temp[i]*num
            
        if m2[cont_col]>0:
            resultado[nr]=resultado[nr]-(num*m_temp_r[cont_col])
            for i in range(len(m2)):
                m2[i]=m2[i]-m_temp[i]
        else:
            resultado[nr]=resultado[nr]+(num*m_temp_r[cont_col])
            for i in range(len(m2)):
                m2[i]=m2[i]+m_temp[i]  
                
        return m2, resultado         
    
    recorrido=0
    recorrido2=0
    if len(matrizfinal)!=len(matrizfinal[0]):
        recorrido=len(matrizfinal)-1
        recorrido2=len(matrizfinal[1])
    if len(matrizfinal)==len(matrizfinal[0]):
        recorrido=len(matrizfinal)-1
        recorrido2=len(matrizfinal[1])
        
    cont=recorrido-1
    cont_col=recorrido2-1
    cf=0
    for i in range(recorrido):
        if len(matrizfinal)>len(matrizfinal[0]): 
            cont_col=len(matrizfinal[0])-1+cf 
            cont=cont_col-1
        if len(matrizfinal)==len(matrizfinal[0]): 
            cont=recorrido-1+cf
            cont_col=recorrido2-1+cf 
        if len(matrizfinal)<len(matrizfinal[0]):
            cont_col=len(matrizfinal)-1+cf 
            cont=cont_col-1
            
        for j in range(i+1,recorrido2):

            matrizfinal[cont]=suma_columna2(matrizfinal[cont_col],matrizfinal[cont],matrizresultado ,cont_col,cont)[0]
            matrizresultado=suma_columna2(matrizfinal[cont_col], matrizfinal[cont], matrizresultado, cont_col, cont)[1]
            if cont!=0:
                cont=cont-1
        if cont_col!=0:    
            cont_col=cont_col-1 
        cf=cf-1
    return matrizfinal, matrizresultado
############## Rutas ##############################
### Index
@app.route('/')
def home():
    return render_template('index.html', rango=10)

### Determinante
@app.route('/leerFormDet', methods=["POST"])
def leerFormDet():
    if request.method == "POST":
        numeroFilas = int(request.form['numeroFilas'])
        numeroColumnas = int(request.form['numeroColumnas'])
        return render_template('determinante.html', data={'nFilas':numeroFilas, 'nColumnas':numeroColumnas})
    else:
        return 'Bad request'

@app.route('/resultadoDet', methods=["POST"])
def resultadoDet():
    if request.method == "POST":
        filas = 0       
        matriz = request.form
        for i in matriz.items():
            filas +=1
        filas = np.sqrt(filas)

        matrizA = np.zeros((int(filas),int(filas)))
        for (i,j), e in matriz.items():
            matrizA[int(i)-1,int(j)-1] = float(e)
        resDet = det(matrizA)
        return render_template('resultadoDet.html', data=[resDet])
    else:
        return 'bad request'

### Suma y resta de matrices
@app.route('/leerFormSum', methods=["POST"])
def leerFormSum():
    if request.method == "POST":
        numeroFilasSuma = int(request.form['numeroFilas'])
        numeroColumnasSuma = int(request.form['numeroColumnas'])
        return render_template('suma.html', data={'nFilas':numeroFilasSuma, 'nColumnas':numeroColumnasSuma})
    else:
        return 'Bad request'
@app.route('/resultadoSuma', methods=["POST"])
def resultadoSuma():
    if request.method == "POST":
        valores = request.form.copy()
        valores.popitem()
        print(valores)
        for v in valores:
            final = v

        filas = int(final[0])   
        columnas = int(final[1])

        listaValoresA = []
        listaValoresB = []
        for v in valores:
            listaValoresA.append((valores.getlist(v)[0]))
            listaValoresB.append((valores.getlist(v)[1]))
        matrizA = np.array(listaValoresA).reshape(filas, columnas)
        matrizB = np.array(listaValoresB).reshape(filas, columnas)
        matrizA = convertir_inputs_decimal(matrizA)
        matrizB = convertir_inputs_decimal(matrizB)


        if request.form['action'] == 'Calcular suma':
            resultado = sumar_matrices(matrizA, matrizB)
            resultado = convertir_decimal_fraccion(resultado)
            return render_template('resultadoSuma.html', matrizRes = resultado, nFilas=filas, nColumnas=columnas)
        elif request.form['action'] == 'Calcular resta':
            resultado = restar_matrices(matrizA, matrizB)
            resultado = convertir_decimal_fraccion(resultado)
            return render_template('resultadoResta.html', matrizRes = resultado, nFilas=filas, nColumnas=columnas)
    else:
        return 'bad request'

### Producto de matrices
@app.route('/leerMulMatrices', methods=["POST"])
def leerMulMatrices():
    if request.method == "POST":
        nFilasMatrizA = int(request.form.getlist('numeroFilas')[0])
        nFilasMatrizB = int(request.form.getlist('numeroFilas')[1])
        nColumnasMatrizA = int(request.form.getlist('numeroColumnas')[0])
        nColumnasMatrizB = int(request.form.getlist('numeroColumnas')[1])
        print(nFilasMatrizA, nColumnasMatrizA)
        return render_template('mulMatrices.html', data={'nFilasA':nFilasMatrizA, 'nColumnasA':nColumnasMatrizA, 'nFilasB': nFilasMatrizB, 'nColumnasB': nColumnasMatrizB})
    else:
        return 'Bad request'
@app.route('/resultadoMultiMatrices', methods=["POST"])
def resultadoMultiMatrices():
    if request.method == "POST":
        nFilasMatrizA = int(request.form['nFilasA'])
        nColumnasMatrizA = int(request.form['nColumnasA'])
        nFilasMatrizB = int(request.form['nFilasB'])
        nColumnasMatrizB = int(request.form['nColumnasB'])

        valores = request.form.copy()
        valores.pop('nFilasA')
        valores.pop('nFilasB')
        valores.pop('nColumnasA')
        valores.pop('nColumnasB')

        listaValoresA = []
        listaValoresB = []
        print(valores)
        for v in valores:
            if v[0] == 'A':
                listaValoresA.append(valores.getlist(v)[0])
            else:
                listaValoresB.append(valores.getlist(v)[0])

        matrizA = np.array(listaValoresA).reshape(nFilasMatrizA, nColumnasMatrizA)
        matrizB = np.array(listaValoresB).reshape(nFilasMatrizB, nColumnasMatrizB)
        matrizA = convertir_inputs_decimal(matrizA)
        matrizB = convertir_inputs_decimal(matrizB)
        
        matrizRes = multiplicar_matrices(matrizA, matrizB)
        matrizRes = convertir_decimal_fraccion(matrizRes)

        return render_template('resultadoMultiMatrices.html', matrizRes = matrizRes, nFilas = nFilasMatrizA, nColumnas = nColumnasMatrizB )
    else:
        return "Bad Request"

@app.route('/leerTraza', methods=["POST"])
def leerTraza():
    if request.method == "POST":
        numeroFilas = int(request.form['numeroFilas'])
        numeroColumnas = int(request.form['numeroColumnas'])
        return render_template('traza.html', data={'nFilas':numeroFilas, 'nColumnas':numeroColumnas})
    else:
        return 'Bad request'

@app.route('/resultadoTraza', methods=["POST"])
def resultadoTraza():
    if request.method == "POST":
        nFilas = int(request.form['nFilas'])
        nColumnas = int(request.form['nColumnas'])

        valores = request.form.copy()
        valores.pop('nFilas')
        valores.pop('nColumnas')
        listaValoresA = []

        for v in valores:
            listaValoresA.append(valores.getlist(v)[0])

        matrizA = np.array(listaValoresA).reshape(nFilas, nColumnas)
        matrizA = convertir_inputs_decimal(matrizA)
        resTraza = traza(matrizA)
        return render_template('resultadoTraza.html', data=[resTraza])
    else:
        return 'bad request'

@app.route('/leerTranspuesta', methods=["POST"])
def leerTranspuesta():
    if request.method == "POST":
        numeroFilas = int(request.form['numeroFilas'])
        numeroColumnas = int(request.form['numeroColumnas'])
        return render_template('transpuesta.html', data={'nFilas':numeroFilas, 'nColumnas':numeroColumnas})
    else:
        return 'Bad request'

@app.route('/resultadoTranspuesta', methods=["POST"])
def resultadoTranspuesta():
    if request.method == "POST":
        nFilas = int(request.form['nFilas'])
        nColumnas = int(request.form['nColumnas'])

        valores = request.form.copy()
        valores.pop('nFilas')
        valores.pop('nColumnas')
        listaValoresA = []

        for v in valores:
            listaValoresA.append(valores.getlist(v)[0])

        matrizA = np.array(listaValoresA).reshape(nFilas, nColumnas)
        matrizA = convertir_inputs_decimal(matrizA)
        resTranspuesta = traspuesta(matrizA)
        resTranspuesta = convertir_decimal_fraccion(resTranspuesta)
        return render_template('resultadoTranspuesta.html', nFilas = nFilas, nColumnas = nColumnas, matrizRes= resTranspuesta)
    else:
        return 'bad request'

@app.route('/leermultPorEscalar', methods=["POST"])
def leermultPorEscalar():
    if request.method == "POST":
        numeroFilas = int(request.form['numeroFilas'])
        numeroColumnas = int(request.form['numeroColumnas'])
        return render_template('multPorEscalar.html', data={'nFilas':numeroFilas, 'nColumnas':numeroColumnas})
    else:
        return 'Bad request'

@app.route('/resultadomultPorEscalar', methods=["POST"])
def resultadomultPorEscalar():
    if request.method == "POST":
        nFilas = int(request.form['nFilas'])
        nColumnas = int(request.form['nColumnas'])
        escalar = int(request.form['escalar'])

        valores = request.form.copy()
        valores.pop('nFilas')
        valores.pop('nColumnas')
        valores.pop('escalar')
        listaValoresA = []

        for v in valores:
            listaValoresA.append(valores.getlist(v)[0])

        matrizA = np.array(listaValoresA).reshape(nFilas, nColumnas)
        matrizA = convertir_inputs_decimal(matrizA)
        resMultiPorEscalar = multiplicar_por_escalar(escalar, matrizA)
        resMultiPorEscalar = convertir_decimal_fraccion(resMultiPorEscalar)
        return render_template('resultadomultPorEscalar.html', nFilas = nFilas, nColumnas = nColumnas, matrizRes= resMultiPorEscalar)
    else:
        return 'bad request'

@app.route('/leerInversa', methods=["POST"])
def leerInversa():
    if request.method == "POST":
        numeroFilas = int(request.form['numeroFilas'])
        numeroColumnas = int(request.form['numeroColumnas'])
        return render_template('inversa.html', data={'nFilas':numeroFilas, 'nColumnas':numeroColumnas})
    else:
        return 'Bad request'

@app.route('/resultadoInversa', methods=["POST"])
def resultadoInversa():
    if request.method == "POST":
        nFilas = int(request.form['nFilas'])
        nColumnas = int(request.form['nColumnas'])

        valores = request.form.copy()
        print(valores)
        valores.pop('nFilas')
        valores.pop('nColumnas')
        listaValoresA = []
        print(valores)

        for v in valores:
            listaValoresA.append(valores.getlist(v)[0])

        matrizA = np.array(listaValoresA).reshape(nFilas, nColumnas)
        print(matrizA)
        matrizA = convertir_inputs_decimal(matrizA)
        print(matrizA)
        resInversa = calcular_matriz_inversa(matrizA)
        #resInversa = convertir_decimal_fraccion(matrizA)
        return render_template('resultadoInversa.html', nFilas = nFilas, nColumnas = nColumnas, matrizRes= resInversa)
    else:
        return 'bad request'

@app.route('/leerNorma', methods=["POST"])
def leerNorma():
    if request.method == "POST":
        numeroFilas = int(request.form['numeroFilas'])
        return render_template('norma.html', data={'nFilas':numeroFilas})
    else:   
        return 'Bad request'

@app.route('/resultadoNorma', methods=["POST"])
def resultadoNorma():
    if request.method == "POST":
        valores = request.form.copy()
        valores.pop('nFilas')
        listaValoresA = []
        for v in valores:
            listaValoresA.append(int(valores.getlist(v)[0]))

        vectorA = np.array(listaValoresA)
        resNorma = calcular_norma(vectorA)
        print(resNorma)
        return render_template('resultadoNorma.html', data=[resNorma])
    else:
        return 'bad request'

@app.route('/leerDireccion', methods=["POST"])
def leerDireccion():
    if request.method == "POST":
        numeroFilas = int(request.form['numeroFilas'])
        return render_template('direccion.html', data={'nFilas':numeroFilas})
    else:   
        return 'Bad request'

@app.route('/resultadoDireccion', methods=["POST"])
def resultadoDireccion():
    if request.method == "POST":
        valores = request.form.copy()
        valores.pop('nFilas')
        listaValoresA = []
        print(valores)
        for v in valores:
            listaValoresA.append(int(valores.getlist(v)[0]))

        vectorA = np.array(listaValoresA)
        print(vectorA)
        resDireccion = direccion_vector(vectorA)
        return render_template('resultadoDireccion.html', data=[resDireccion])
    else:
        return 'bad request'

@app.route('/leerUnitario', methods=["POST"])
def leerUnitario():
    if request.method == "POST":
        numeroFilas = int(request.form['numeroFilas'])
        return render_template('unitario.html', data={'nFilas':numeroFilas})
    else:   
        return 'Bad request'

@app.route('/resultadoUnitario', methods=["POST"])
def resultadoUnitario():
    if request.method == "POST":
        valores = request.form.copy()
        valores.pop('nFilas')
        listaValoresA = []
        print(valores)
        for v in valores:
            listaValoresA.append(int(valores.getlist(v)[0]))

        vectorA = np.array(listaValoresA)
        print(vectorA)
        resUnitario = calcular_vector_unitario(vectorA)
        return render_template('resultadoUnitario.html', data=[resUnitario])
    else:
        return 'bad request'

@app.route('/leerProductoPunto', methods=["POST"])
def leerProductoPunto():
    if request.method == "POST":
        numeroFilas = int(request.form['numeroFilas'])
        return render_template('productoPunto.html', data={'nFilas':numeroFilas})
    else:   
        return 'Bad request'

@app.route('/resultadoProductoPunto', methods=["POST"])
def resultadoProductoPunto():
    if request.method == "POST":
        valores = request.form.copy()
        listaValoresA = []
        listaValoresB = []
        print(valores)
        for v in valores:
            listaValoresA.append(int(valores.getlist(v)[0]))
            listaValoresB.append(int(valores.getlist(v)[1]))

        vectorA = np.array(listaValoresA)
        vectorB  =np.array(listaValoresB)
        print(vectorA)
        print(vectorB)
        resProductoPunto = producto_punto(vectorA, vectorB)
        return render_template('resultadoProductoPunto.html', data=[resProductoPunto])
    else:
        return 'bad request'

@app.route('/leerGram', methods=["POST"])
def leerGram():
    if request.method == "POST":
        numeroFilas = int(request.form['numeroFilas'])
        numeroColumnas = int(request.form['numeroFilas'])
        return render_template('gram.html', data={'nFilas':numeroFilas, 'nColumnas':numeroColumnas})
    else:
        return 'Bad request'

@app.route('/resultadoGram', methods=["POST"])
def resultadoGram():
    if request.method == "POST":
        nFilas = int(request.form['nFilas'])
        nColumnas = int(request.form['nColumnas'])

        valores = request.form.copy()
        print(valores)
        valores.pop('nFilas')
        valores.pop('nColumnas')
        listaValoresA = []
        print(valores)

        for v in valores:
            listaValoresA.append(int(valores.getlist(v)[0]))

        matrizA = np.array(listaValoresA).reshape(nFilas, nColumnas)
        print('matriz :', matrizA)
        resGram = Gram_Schmidt(matrizA)
        print(resGram)
        return render_template('resultadoGram.html', nFilas = nFilas, nColumnas = nColumnas, matrizRes= resGram)
    else:
        return 'bad request'

@app.route('/leerValoresPropios', methods=["POST"])
def leerValoresPropios():
    if request.method == "POST":
        numeroFilas = int(request.form['numeroFilas'])
        numeroColumnas = int(request.form['numeroFilas'])
        return render_template('valoresPropios.html', data={'nFilas':numeroFilas, 'nColumnas':numeroColumnas})
    else:
        return 'Bad request'

@app.route('/resultadoValoresPropios', methods=["POST"])
def resultadoValoresPropios():
    if request.method == "POST":
        nFilas = int(request.form['nFilas'])
        nColumnas = int(request.form['nColumnas'])

        valores = request.form.copy()
        print(valores)
        valores.pop('nFilas')
        valores.pop('nColumnas')
        listaValoresA = []
        print(valores)

        for v in valores:
            listaValoresA.append(int(valores.getlist(v)[0]))

        matrizA = np.array(listaValoresA).reshape(nFilas, nColumnas)
        print('matriz :', matrizA)
        resValoresPropios = calcular_valores_propios(matrizA)
        print(resValoresPropios)
        return render_template('resultadoValoresPropios.html', nFilas = nFilas, nColumnas = nColumnas, matrizRes= resValoresPropios)
    else:
        return 'bad request'

@app.route('/leerVectoresPropios', methods=["POST"])
def leerVectoresPropios():
    if request.method == "POST":
        numeroFilas = int(request.form['numeroFilas'])
        numeroColumnas = int(request.form['numeroFilas'])
        return render_template('vectoresPropios.html', data={'nFilas':numeroFilas, 'nColumnas':numeroColumnas})
    else:
        return 'Bad request'

@app.route('/resultadoVectoresPropios', methods=["POST"])
def resultadoVectoresPropios():
    if request.method == "POST":
        nFilas = int(request.form['nFilas'])
        nColumnas = int(request.form['nColumnas'])

        valores = request.form.copy()
        print(valores)
        valores.pop('nFilas')
        valores.pop('nColumnas')
        listaValoresA = []
        print(valores)

        for v in valores:
            listaValoresA.append(int(valores.getlist(v)[0]))

        matrizA = np.array(listaValoresA).reshape(nFilas, nColumnas)
        print('matriz :', matrizA)
        resVectoresPropios = calcular_vectores_propios(matrizA)
        print(resVectoresPropios)
        return render_template('resultadoVectoresPropios.html', nFilas = nFilas, nColumnas = nColumnas, matrizRes= resVectoresPropios)
    else:
        return 'bad request'

@app.route('/leerGauss', methods=["POST"])
def leerGauss():
    if request.method == "POST":
        numeroFilas = int(request.form['numeroFilas'])
        numeroColumnas = int(request.form['numeroColumnas'])
        return render_template('gauss.html', data={'nFilas':numeroFilas, 'nColumnas':numeroColumnas})
    else:
        return 'Bad request'

@app.route('/resultadoGauss', methods=["POST"])
def resultadoGauss():
    if request.method == "POST":
        nFilas = int(request.form['nFilas'])
        nColumnas = int(request.form['nColumnas'])

        valores = request.form.copy()
        valores.pop('nFilas')
        valores.pop('nColumnas')
        listaValoresA = []
        listaValoresR = []

        for v in valores:
            listaValoresA.append(valores.getlist(v)[0])

        matrizA = np.array(listaValoresA).reshape(nFilas, nColumnas)
        matrizA = convertir_inputs_decimal(matrizA)

        i = nColumnas
        listaValoresR = [fila[i-1] for fila in matrizA]
        matrizR = np.array(listaValoresR).reshape(i-1,1)

        matrizA = np.delete(matrizA, i-1, 1)

        resGaus = gauss_Jorda_p1(matrizA, matrizR)
        matrizReducida = resGaus[0]
        matrizReducida = convertir_decimal_fraccion(matrizReducida)
        matrizResultados = resGaus[1]
        matrizResultados = convertir_decimal_fraccion(matrizResultados)
        print(matrizReducida)
        print(matrizResultados)
        return render_template('resultadoGauss.html',  nFilas = nFilas, nColumnas = nColumnas, matrizReducida = matrizReducida, matrizRes= matrizResultados)
    else:
        return 'bad request'

if __name__ == '__main__':
    # Iniciamos la aplicación en modo debug
    app.run(debug=True)
