/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package modelo;

/**
 *
 * @author 304-1
 */
public class Modelo {
    int nuno;
    int ndos;
    int nresult;

    public Modelo() {
    }
    
    public int getNuno() {
        return nuno;
    }

    public void setNuno(int nuno) {
        this.nuno = nuno;
    }

    public int getNdos() {
        return ndos;
    }

    public void setNdos(int ndos) {
        this.ndos = ndos;
    }

    public int getNresult() {
        return nresult;
    }

    public void setNresult(int nresult) {
        this.nresult = nresult;
    }
    
    public int operacion()
    {
       this.nresult=this.nuno+this.ndos;
       return this.nresult;
    }
    
    public int operacion1()
    {
       this.nresult=this.nuno-this.ndos;
       return this.nresult;
    }
}
