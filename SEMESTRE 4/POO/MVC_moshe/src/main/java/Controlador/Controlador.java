/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controlador;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import Vista.Interfaz_Vista;
import Modelo.Modelo;



/**
 *
 * @author User
 */
public class Controlador implements ActionListener{
    
    Interfaz_Vista view;
    Modelo model;
    
    public Controlador(Interfaz_Vista view,Modelo model){
    
        this.view=view;
        this.model=model;
        
        this.view.btnoperacion1.addActionListener(this);
        this.view.btnoperacion2.addActionListener(this);
    }
    
    public void iniciar(){
    
        view.setTitle("Ventana de calculos");
        view.setLocationRelativeTo(null);
        
    }
    
    public void ActionPerformed(ActionEvent e){
    
        model.setN_uno(Integer.parseInt(view.txt1.getText()));
        model.setN_dos(Integer.parseInt(view.txt2.getText()));
        
        if(e.getSource()== view.btnoperacion1){
        
            model.operacion1();
        }
        if(e.getSource()== view.btnoperacion2){
        
            model.operacion2();
        }
        
        view.txt3.setText(String.valueOf(model.getN_resultado()));
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
    
}
