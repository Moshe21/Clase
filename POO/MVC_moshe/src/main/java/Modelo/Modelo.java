/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Modelo;

/**
 *
 * @author User
 */
public class Modelo {
   /*las variables*/ 
    int n_uno;
    int n_dos;
    int n_resultado;
/*las constructor*/ 
    public Modelo() {
    }
    
    
    
/*las colocar y obtener*/ 
    public int getN_uno() {
        return n_uno;
    }

    public void setN_uno(int n_uno) {
        this.n_uno = n_uno;
    }

    public int getN_dos() {
        return n_dos;
    }

    public void setN_dos(int n_dos) {
        this.n_dos = n_dos;
    }

    public int getN_resultado() {
        return n_resultado;
    }

    public void setN_resultado(int n_resultado) {
        this.n_resultado = n_resultado;
    }
    
    
    
    /*opreacciones y partes logicas*/
    
    
    public int operacion1()
    {
    
    this.n_resultado=this.n_uno+this.n_dos;
    return this.n_resultado;
    
    }
    
      public int operacion2()
    {
    
    this.n_resultado=this.n_uno-this.n_dos;
    return this.n_resultado;
    
    }

    public void getN_uno(int parseInt) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }

    public void getN_dos(int parseInt) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
    
}
