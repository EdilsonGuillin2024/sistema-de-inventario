class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.producto_id

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.producto_id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.obtener_id()] = producto

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            del self.productos[producto_id]
            print(f"Producto ID {producto_id} eliminado.")
        else:
            print(f"Producto ID {producto_id} no encontrado.")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        if producto_id in self.productos:
            if cantidad is not None:
                self.productos[producto_id].establecer_cantidad(cantidad)
            if precio is not None:
                self.productos[producto_id].establecer_precio(precio)
            print(f"Producto ID {producto_id} actualizado.")
        else:
            print(f"Producto ID {producto_id} no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.obtener_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_inventario(self, filename):
        with open(filename, 'w') as f:
            for producto in self.productos.values():
                f.write(f"{producto.obtener_id()},{producto.obtener_nombre()},{producto.obtener_cantidad()},{producto.obtener_precio()}\n")

    def cargar_inventario(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    producto_id, nombre, cantidad, precio = line.strip().split(',')
                    self.agregar_producto(Producto(producto_id, nombre, int(cantidad), float(precio)))
        except FileNotFoundError:
            print("Archivo no encontrado.")

def mostrar_menu():
    print("\n--- UEA ---")
    print("Facultad de Ciencias de la Educación")
    print("Ingeniería en Tecnologías de la Información")
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario en archivo")
    print("7. Cargar inventario desde archivo")
    print("8. Salir")

def main():
    inventario = Inventario()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            producto_id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            inventario.agregar_producto(Producto(producto_id, nombre, cantidad, precio))
            print("Producto añadido.")

        elif opcion == '2':
            producto_id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(producto_id)

        elif opcion == '3':
            producto_id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje vacío si no desea cambiar): ")
            precio = input("Ingrese el nuevo precio (deje vacío si no desea cambiar): ")
            inventario.actualizar_producto(producto_id, int(cantidad) if cantidad else None, float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            filename = input("Ingrese el nombre del archivo para guardar el inventario: ")
            inventario.guardar_inventario(filename)
            print("Inventario guardado.")

        elif opcion == '7':
            filename = input("Ingrese el nombre del archivo para cargar el inventario: ")
            inventario.cargar_inventario(filename)
            print("Inventario cargado.")

        elif opcion == '8':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
