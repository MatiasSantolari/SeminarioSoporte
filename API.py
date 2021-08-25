import yfinance as yf
import matplotlib.pyplot as plt

# EXTRAER DATOS
dataML = yf.download('MELI', '2015-08-01', '2021-08-23', interval="1d")
print(dataML)

# CREAR GRAFICA
plt.figure(figsize=(16, 10))
dataML['Close'].plot()
plt.suptitle("MercadoLibre, Inc. - Currency in USD")
plt.savefig('MELI.png')
plt.show()

# PASAR DATOS A UN EXCEL
dataML.to_csv('MELI.csv') # LUEGO EL ARCHIVO CSV SE PUEDE EXPORTAR A UNA BASE DE DATOS0
