/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.mvc_moshe;
import Vista.Interfaz_Vista;
import Controlador.Controlador;
import Modelo.Modelo;


/**
 *
 * @author User
 */
public class MVC_moshe {

    public static void main(String[] args) {
        
        
       Modelo mod=new Modelo();
       Interfaz_Vista view=new Interfaz_Vista();
       Controlador Control=new Controlador(view,mod);
       Control.iniciar();
       view.setVisible(true);
       
        
        
        
    }
}
