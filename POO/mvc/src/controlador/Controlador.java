/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controlador;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import vista.Vista;
import modelo.Modelo;
/**
 *
 * @author 304-1
 */
public class Controlador implements ActionListener{
    Vista view;
    Modelo model;
    
    public Controlador(Vista view, Modelo model)
    {
       this.view = view;
       this.model= model;
       this.view.btnoperacion.addActionListener(this);
       this.view.btnoperacion1.addActionListener(this);
    }
    
    public void iniciar(){
        view.setTitle("Ventana de Calculos");
        view.setLocationRelativeTo(null);
    }
    
    public void actionPerformed(ActionEvent e)
    {
        model.setNuno(Integer.parseInt(view.txtnum1.getText()));
        model.setNdos(Integer.parseInt(view.txtnum2.getText()));
        if (e.getSource()==view.btnoperacion)
        {
            model.operacion();
        }
        if (e.getSource()==view.btnoperacion1)
        {
            model.operacion1();
        }
        view.txtnum3.setText(String.valueOf(model.getNresult()));
    }
}
