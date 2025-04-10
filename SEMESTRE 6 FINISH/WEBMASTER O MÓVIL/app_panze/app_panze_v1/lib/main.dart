import 'package:flutter/material.dart';

void main() {
  runApp(RestauranteApp());
}

class RestauranteApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Menú de Restaurante',
      theme: ThemeData.dark().copyWith(
        primaryColor: Color(0xFF1A1A2E),
        scaffoldBackgroundColor: Color(0xFF121212),
        appBarTheme: AppBarTheme(
          backgroundColor: Color(0xFF8B4513), // Color marrón como en la imagen
        ),
        colorScheme: ColorScheme.dark(
          primary: Color(0xFF8B4513),
          secondary: Color(0xFFFF9800),
        ),
      ),
      home: MenuRestaurante(),
    );
  }
}

class Categoria {
  final String nombre;
  final String imagen;
  final List<Producto> productos;

  Categoria({required this.nombre, required this.imagen, required this.productos});
}

class Producto {
  final String nombre;
  final double precio;
  final String descripcion;
  final String imagen;
  int cantidad;

  Producto({
    required this.nombre, 
    required this.precio, 
    this.descripcion = '',
    required this.imagen,
    this.cantidad = 0,
  });
}

class MenuRestaurante extends StatefulWidget {
  @override
  _MenuRestauranteState createState() => _MenuRestauranteState();
}

class _MenuRestauranteState extends State<MenuRestaurante> {
  List<Categoria> categorias = [];
  List<Producto> carrito = [];
  
  int _categoriaSeleccionada = -1; // -1 significa que se muestra el menú principal
  
  // Fondo para simular la textura de madera como en la imagen
  final String fondoMadera = 'assets/fondo_madera.jpg';

  @override
  void initState() {
    super.initState();
    
    // Inicializar las categorías y productos
    categorias = [
      Categoria(
        nombre: 'Hamburguesas',
        imagen: 'assets/hamburguesa_icon.png',
        productos: [
          Producto(
            nombre: 'Hamburguesa Clásica',
            precio: 8.99,
            descripcion: 'Carne, queso, lechuga, tomate y mayonesa',
            imagen: 'assets/hamburguesa_clasica.png',
          ),
          Producto(
            nombre: 'Hamburguesa Doble',
            precio: 12.99,
            descripcion: 'Doble carne, doble queso, lechuga, tomate y salsa especial',
            imagen: 'assets/hamburguesa_doble.png',
          ),
          Producto(
            nombre: 'Hamburguesa Vegetariana',
            precio: 9.99,
            descripcion: 'Medallón de vegetales, queso, lechuga y tomate',
            imagen: 'assets/hamburguesa_vegetariana.png',
          ),
        ],
      ),
      Categoria(
        nombre: 'Sandwiches',
        imagen: 'assets/sandwich_icon.png',
        productos: [
          Producto(
            nombre: 'Sandwich de Pollo',
            precio: 7.50,
            descripcion: 'Pollo grillado, lechuga, tomate y mayonesa',
            imagen: 'assets/sandwich_pollo.png',
          ),
          Producto(
            nombre: 'Sandwich de Jamón y Queso',
            precio: 6.99,
            descripcion: 'Jamón, queso, lechuga y tomate',
            imagen: 'assets/sandwich_jamon.png',
          ),
        ],
      ),
      Categoria(
        nombre: 'Twister',
        imagen: 'assets/twister_icon.png',
        productos: [
          Producto(
            nombre: 'Twister de Pollo',
            precio: 8.99,
            descripcion: 'Pollo, verduras y salsa especial',
            imagen: 'assets/twister_pollo.png',
          ),
          Producto(
            nombre: 'Twister Vegetariano',
            precio: 7.99,
            descripcion: 'Mezcla de vegetales grillados y salsa especial',
            imagen: 'assets/twister_vegetariano.png',
          ),
        ],
      ),
      Categoria(
        nombre: 'Choriperros',
        imagen: 'assets/choriperro_icon.png',
        productos: [
          Producto(
            nombre: 'Choriperro',
            precio: 6.50,
            descripcion: 'Chorizo, salchicha y salsas',
            imagen: 'assets/choriperro.png',
          ),
          Producto(
            nombre: 'Choriperro Especial',
            precio: 7.99,
            descripcion: 'Chorizo, salchicha, queso, tocino y salsas',
            imagen: 'assets/choriperro_especial.png',
          ),
        ],
      ),
    ];
  }

  void agregarAlCarrito(Producto producto) {
    setState(() {
      bool encontrado = false;
      for (var item in carrito) {
        if (item.nombre == producto.nombre) {
          item.cantidad++;
          encontrado = true;
          break;
        }
      }
      
      if (!encontrado) {
        Producto nuevoProducto = Producto(
          nombre: producto.nombre,
          precio: producto.precio,
          descripcion: producto.descripcion,
          imagen: producto.imagen,
          cantidad: 1,
        );
        carrito.add(nuevoProducto);
      }
      
      // Mostrar mensaje
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('${producto.nombre} agregado al carrito'),
          duration: Duration(seconds: 2),
          backgroundColor: Colors.green,
        ),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Bienvenido',
          style: TextStyle(
            fontFamily: 'Cursive',
            fontSize: 28,
            color: Colors.white,
          ),
        ),
        centerTitle: true,
      ),
      body: Container(
        decoration: BoxDecoration(
          image: DecorationImage(
            image: AssetImage(fondoMadera),
            fit: BoxFit.cover,
            colorFilter: ColorFilter.mode(
              Colors.black.withOpacity(0.3),
              BlendMode.darken,
            ),
          ),
        ),
        child: _categoriaSeleccionada == -1
            ? _construirMenuPrincipal()
            : _construirDetalleCategoria(),
      ),
      floatingActionButton: carrito.isNotEmpty
          ? FloatingActionButton(
              onPressed: () {
                _mostrarCarrito();
              },
              backgroundColor: Colors.amber,
              child: Stack(
                alignment: Alignment.center,
                children: [
                  Icon(Icons.shopping_cart, color: Colors.black),
                  if (carrito.isNotEmpty)
                    Positioned(
                      right: 0,
                      top: 0,
                      child: Container(
                        padding: EdgeInsets.all(2),
                        decoration: BoxDecoration(
                          color: Colors.red,
                          borderRadius: BorderRadius.circular(10),
                        ),
                        constraints: BoxConstraints(
                          minWidth: 16,
                          minHeight: 16,
                        ),
                        child: Text(
                          _obtenerTotalProductos().toString(),
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 10,
                          ),
                          textAlign: TextAlign.center,
                        ),
                      ),
                    ),
                ],
              ),
            )
          : null,
    );
  }

  int _obtenerTotalProductos() {
    int total = 0;
    for (var producto in carrito) {
      total += producto.cantidad;
    }
    return total;
  }

  Widget _construirMenuPrincipal() {
    return Column(
      children: [
        SizedBox(height: 20),
        Text(
          'Menú',
          style: TextStyle(
            fontSize: 36,
            fontWeight: FontWeight.bold,
            fontFamily: 'Cursive',
          ),
          textAlign: TextAlign.center,
        ),
        SizedBox(height: 30),
        Expanded(
          child: ListView.builder(
            itemCount: categorias.length,
            itemBuilder: (context, index) {
              return _construirItemCategoria(index);
            },
          ),
        ),
      ],
    );
  }

  Widget _construirItemCategoria(int index) {
    return Padding(
      padding: EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      child: InkWell(
        onTap: () {
          setState(() {
            _categoriaSeleccionada = index;
          });
        },
        child: Container(
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(30),
            color: index % 2 == 0 ? Colors.amber : Colors.deepOrange,
          ),
          child: Padding(
            padding: EdgeInsets.symmetric(vertical: 12, horizontal: 16),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Row(
                  children: [
                    ClipRRect(
                      borderRadius: BorderRadius.circular(25),
                      child: Container(
                        color: Colors.white,
                        padding: EdgeInsets.all(8),
                        child: Image.asset(
                          categorias[index].imagen,
                          width: 40,
                          height: 40,
                        ),
                      ),
                    ),
                    SizedBox(width: 16),
                    Text(
                      categorias[index].nombre,
                      style: TextStyle(
                        fontSize: 24,
                        fontFamily: 'Cursive',
                        fontWeight: FontWeight.bold,
                        color: Colors.black,
                      ),
                    ),
                  ],
                ),
                Container(
                  decoration: BoxDecoration(
                    color: Colors.white,
                    shape: BoxShape.circle,
                  ),
                  child: Icon(
                    Icons.keyboard_arrow_down,
                    color: Colors.black,
                    size: 30,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _construirDetalleCategoria() {
    return Column(
      children: [
        // Botón para volver atrás
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: ElevatedButton.icon(
            onPressed: () {
              setState(() {
                _categoriaSeleccionada = -1;
              });
            },
            icon: Icon(Icons.arrow_back),
            label: Text('Volver al menú principal'),
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.brown,
            ),
          ),
        ),
        // Título de la categoría
        Text(
          categorias[_categoriaSeleccionada].nombre,
          style: TextStyle(
            fontSize: 32,
            fontWeight: FontWeight.bold,
            fontFamily: 'Cursive',
          ),
        ),
        // Lista de productos de la categoría
        Expanded(
          child: ListView.builder(
            itemCount: categorias[_categoriaSeleccionada].productos.length,
            itemBuilder: (context, index) {
              final producto = categorias[_categoriaSeleccionada].productos[index];
              return Card(
                margin: EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                color: Colors.brown.withOpacity(0.7),
                child: ListTile(
                  contentPadding: EdgeInsets.all(16),
                  leading: Image.asset(
                    producto.imagen,
                    width: 60,
                    height: 60,
                    errorBuilder: (context, error, stackTrace) {
                      return Icon(Icons.fastfood, size: 60);
                    },
                  ),
                  title: Text(
                    producto.nombre,
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  subtitle: Text(
                    producto.descripcion + '\n\nPrecio: \$${producto.precio.toStringAsFixed(2)}',
                  ),
                  trailing: IconButton(
                    icon: Icon(Icons.add_circle, size: 40, color: Colors.amber),
                    onPressed: () {
                      agregarAlCarrito(producto);
                    },
                  ),
                ),
              );
            },
          ),
        ),
      ],
    );
  }

  void _mostrarCarrito() {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) {
        return Container(
          height: MediaQuery.of(context).size.height * 0.7,
          decoration: BoxDecoration(
            color: Colors.grey[900],
            borderRadius: BorderRadius.only(
              topLeft: Radius.circular(20),
              topRight: Radius.circular(20),
            ),
          ),
          child: Column(
            children: [
              Container(
                padding: EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.brown,
                  borderRadius: BorderRadius.only(
                    topLeft: Radius.circular(20),
                    topRight: Radius.circular(20),
                  ),
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      'Tu Pedido',
                      style: TextStyle(
                        fontSize: 22,
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ),
                    IconButton(
                      icon: Icon(Icons.close, color: Colors.white),
                      onPressed: () {
                        Navigator.pop(context);
                      },
                    ),
                  ],
                ),
              ),
              Expanded(
                child: carrito.isEmpty
                    ? Center(
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(Icons.shopping_cart_outlined, size: 100, color: Colors.grey),
                            SizedBox(height: 16),
                            Text(
                              'Tu carrito está vacío',
                              style: TextStyle(
                                fontSize: 18,
                                color: Colors.grey,
                              ),
                            ),
                          ],
                        ),
                      )
                    : ListView.builder(
                        itemCount: carrito.length,
                        itemBuilder: (context, index) {
                          final producto = carrito[index];
                          return ListTile(
                            leading: Image.asset(
                              producto.imagen,
                              width: 50,
                              height: 50,
                              errorBuilder: (context, error, stackTrace) {
                                return Icon(Icons.fastfood, size: 50);
                              },
                            ),
                            title: Text(producto.nombre),
                            subtitle: Text('\$${producto.precio.toStringAsFixed(2)}'),
                            trailing: Row(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                IconButton(
                                  icon: Icon(Icons.remove_circle, color: Colors.red),
                                  onPressed: () {
                                    setState(() {
                                      if (producto.cantidad > 1) {
                                        producto.cantidad--;
                                      } else {
                                        carrito.removeAt(index);
                                      }
                                      Navigator.pop(context);
                                      _mostrarCarrito();
                                    });
                                  },
                                ),
                                Text(
                                  '${producto.cantidad}',
                                  style: TextStyle(fontSize: 18),
                                ),
                                IconButton(
                                  icon: Icon(Icons.add_circle, color: Colors.green),
                                  onPressed: () {
                                    setState(() {
                                      producto.cantidad++;
                                      Navigator.pop(context);
                                      _mostrarCarrito();
                                    });
                                  },
                                ),
                              ],
                            ),
                          );
                        },
                      ),
              ),
              if (carrito.isNotEmpty)
                Container(
                  padding: EdgeInsets.all(16),
                  color: Colors.grey[800],
                  child: Column(
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            'Total:',
                            style: TextStyle(
                              fontSize: 20,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          Text(
                            '\$${_calcularTotal().toStringAsFixed(2)}',
                            style: TextStyle(
                              fontSize: 20,
                              fontWeight: FontWeight.bold,
                              color: Colors.amber,
                            ),
                          ),
                        ],
                      ),
                      SizedBox(height: 16),
                      ElevatedButton(
                        onPressed: () {
                          // Aquí iría la lógica para procesar el pedido
                          ScaffoldMessenger.of(context).showSnackBar(
                            SnackBar(
                              content: Text('¡Pedido realizado con éxito!'),
                              backgroundColor: Colors.green,
                            ),
                          );
                          setState(() {
                            carrito.clear();
                          });
                          Navigator.pop(context);
                        },
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.amber,
                          padding: EdgeInsets.symmetric(vertical: 15),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(10),
                          ),
                        ),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(
                              Icons.check_circle,
                              color: Colors.black,
                            ),
                            SizedBox(width: 8),
                            Text(
                              'REALIZAR PEDIDO',
                              style: TextStyle(
                                color: Colors.black,
                                fontWeight: FontWeight.bold,
                                fontSize: 16,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
            ],
          ),
        );
      },
    );
  }

  double _calcularTotal() {
    double total = 0;
    for (var producto in carrito) {
      total += producto.precio * producto.cantidad;
    }
    return total;
  }
}