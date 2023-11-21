select * from proveedores;
UPDATE usuarios SET contraseña = 'Teczonic21' WHERE usuario='mzabaleta';

INSERT INTO proveedores (razon_social, nit, direccion, ciudad, telefono, banco, cuenta, tipo_cuenta) VALUES 
						('Bogotá', 'Vehículos familiares', 12000,0,0,0,0),
						('Bogotá', 'Camión', 60000,0,0,0,0);