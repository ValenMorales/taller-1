class Soluciones:
    #crear metodo inicializador de la clase
    def __init__(self):
        #declaracion de variables
        self.categorias= [ "lacteos", "aseo", "granos"]
        self.listaProductos=[]
    #punto 2
        self.existencia_lacteos = [ ]
        self.existencia_aseos = [ ]
        self.existencia_granos = [ ]
    #punto 3
    #El sistema debe permitir ingresar el nombre
    #  del producto y el número de los mismos,  
    #ademas de la categoría a la que pertenecen.

    def agregar_producto(self, existencia, num_categoria):
        nombre_producto= input('ingresa el nombre del producto ')
        if nombre_producto in globals():
            print('ya existe')
            cantidad_producto= int(input('cuanta cantidad hay de este producto?'))
            for item in existencia:
                if item[0]==nombre_producto:
                    item[1]=int(item[1])+cantidad_producto
        else:  
            self.listaProductos.append((self.categorias[num_categoria], nombre_producto))
            cantidad_producto= int(input('cuanta cantidad hay de este producto?'))
            existencia.append((nombre_producto, cantidad_producto))


    def añadir_producto(self):
        while True:
            try:
                n= int(input('cuantos productos quieres ingresar?'))
                for i in range(n):
                    tipo_producto= int(input('que tipo de producto vas a ingresar?\n 1.lacteos\n 2.aseo \n 3.granos\n'))
                    if tipo_producto==1:
                        self.agregar_producto(self.existencia_lacteos, 0)
                    if tipo_producto==2:
                        self.agregar_producto(self.existencia_aseos, 1)
                    if tipo_producto==3:
                        self.agregar_producto(self.existencia_granos, 2)
                break
            except:
                print('debes seleccionar una de las 3 opciones')

    def mostrar_productos(self):
        for item in self.existencia_aseos:
            print(item)
        for item in self.existencia_granos:
            print(item)
        for item in self.existencia_lacteos:
            print(item)


    

        





