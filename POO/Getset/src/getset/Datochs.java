/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package getset;

/**
 *
 * @author 304
 */
public class Datochs {
    String nombre;
    String apellido;
    int edad;

    public Datochs(String nombre, String apellido, int edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }
    
    public void mostra(){
        
        System.out.println("datos ingresados");
        System.out.println("nombre  "+nombre);
        System.out.println("apellido  "+apellido);
        System.out.println("edad  "+edad);
    }
}
