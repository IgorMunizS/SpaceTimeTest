class Mapa:
    '''
    Classe para criação de um objeto de mapa
    :param mapa: imagem NxM, onde mapa[i, j] > 0 é solo e mapa[i, j] =0 é mar
    :param vizinhanca: Tipo de vizinhança a ser considerada quando realizar operações.
                       4 para 4-conexa e 8 para 8-conexa. Padrão é 8.
    '''
    def __init__(self, mapa, vizinhanca=8):
        self.mapa = mapa
        self.n_linhas = len(mapa)
        self.n_colunas = len(mapa[0])
        self.n_terra = 0


        assert (vizinhanca == 8 or vizinhanca == 4), "Escolha 8 para vizinhanca 8-conexa ou 4 para 4-conexa"

        if vizinhanca == 4:
            self.direcao_vizinhanca = [[-1, 0], [0, -1], [0, 1], [1, 0]]  # [linha, coluna]
            self.tipo_vizinhanca = "vizinhança 4-conexa"
        else:
            self.direcao_vizinhanca = [[-1, 0], [-1,-1], [0, -1], [1,-1], [1, 0], [1, 1], [0, 1], [-1, 1]]  # [linha, coluna]
            self.tipo_vizinhanca = "vizinhança 8-conexa"


    def posicao_valida(self, x, y):

        if x >= 0 and x < self.n_linhas and \
                y >= 0 and y < self.n_colunas and \
                not self.pixel_checado[x][y] and \
                self.mapa[x][y] == 1:

            return True
        else:
            return False


    def checa_vizinho(self, i, j):
        '''Checa quais vizinhos de um pixel solo também é solo'''

        self.pixel_checado[i][j] = True

        for direcao in self.direcao_vizinhanca:
            if self.posicao_valida(i + direcao[0], j + direcao[1]):
                self.n_terra += 1 # soma a quantidade de terras de uma mesma ilha
                self.checa_vizinho(i + direcao[0], j + direcao[1])


    def numero_ilhas(self):
        '''Retorna o número de ilhas em uma matriz MxN'''

        #Matriz de auxílio para controle de pixels já checados
        self.pixel_checado = [[False for _ in range(self.n_colunas)] for _ in range(self.n_linhas)]
        self.n_ilhas = 0

        #Verifica pixel por pixel até encontrar algum que seja solo
        for i in range(self.n_linhas):
            for j in range(self.n_colunas):
                if self.mapa[i][j] == 1 and self.pixel_checado[i][j] == False:
                    self.n_ilhas += 1 #Incrementa número de ilhas quando acha um novo solo que ainda não foi checado
                    self.checa_vizinho(i, j)

        return self.n_ilhas

    def quantidade_terra_afetada(self, x, y):
        '''Calcula o numero de pontos de solo do mapa que podem ser
            afetados por uma semente lançada em mapa[i, j]
            Entrada: (x,y) posição onde semente é lançada
        '''
        self.n_terra = 0
        self.pixel_checado = [[False for _ in range(self.n_colunas)] for _ in range(self.n_linhas)]
        if self.mapa[x][y] == 0:
            return 0 #caiu no mar

        else:
            self.n_terra += 1
            self.checa_vizinho(x,y)

            return self.n_terra




mapa = [[0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0.],
        [0., 1., 1., 1., 0., 0.],
        [0., 0., 1., 0., 1., 0.],
        [0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 0., 0.]]

mapa2 = [[1., 1., 0., 0., 0., 0.],
        [0., 1., 0., 0., 0., 0.],
        [0., 1., 0., 1., 0., 0.],
        [1., 0., 1., 0., 1., 0.],
        [0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 0., 1.]]

mapa3 = [[1., 1., 1., 0., 0., 0.],
        [0., 1., 0., 0., 0., 0.],
        [0., 1., 0., 1., 0., 0.],
        [0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 1., 1.]]

m = Mapa(mapa, 4)
tipo_vizinhanca = m.tipo_vizinhanca
n_ilhas = m.numero_ilhas()
n_terras = m.quantidade_terra_afetada(2,2)
print("Número de ilhas: ", n_ilhas, "com " + tipo_vizinhanca)
print("Número de pontos de solo afetados: ", n_terras, "com " + tipo_vizinhanca)


m = Mapa(mapa, 8)
tipo_vizinhanca = m.tipo_vizinhanca
n_ilhas = m.numero_ilhas()
n_terras = m.quantidade_terra_afetada(2,2)
print("Número de ilhas: ", n_ilhas, "com " + tipo_vizinhanca)
print("Número de pontos de solo afetados: ", n_terras, "com " + tipo_vizinhanca)