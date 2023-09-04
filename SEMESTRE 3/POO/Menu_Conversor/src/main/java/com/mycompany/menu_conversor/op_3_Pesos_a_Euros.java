/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.menu_conversor;

/**
 *
 * @author User
 */
public class op_3_Pesos_a_Euros {
    
    double R;
    
    public op_3_Pesos_a_Euros (double valor1){
    
    this.R=valor1/4461;
     
    }
    public void mostrar(){
        System.out.println("coneversion es :"+R);
    }
}
