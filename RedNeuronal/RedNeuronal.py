from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD

#inputs , situacion
x =0# lista de movimientos legales
y =0# tablero
z =0# valores de piezas
w =0# movimiento optimo = solucion


input_dim = 4

output_dim = 1

modelo = Sequential()
modelo.add(Dense(output_dim, input_dim=input_dim, activation ='linear'))

sgd =SGD(lr=0.0004)
modelo.compile(loss='mse',optimizer=sgd)

modelo.summary()

num_epochs= 40000
batch_size = x #revisar esto

history = modelo.fit(x, y, epochs = num_epochs,batch_size= batch_size, verbose= 0)


capas = modelo.layers[0]
w,b = capas.get_weights()

