package proyecto009poo;

public class CuentaBancaria {
    public int saldo;
    public CuentaBancaria(){
        saldo = 0;
    }
    public void imponerSaldo(int cantidad){
        if(cantidad < 10000){
            saldo += cantidad;
        }else{
            System.out.println("Cantidad demasiado grande, tienes que pasar por la oficina");
        }
    }
    public void retirarSaldo(int cantidad){
        if(saldo - cantidad > 0){
            saldo -= cantidad;
        }else{
            System.out.println("No tiene fondos para esa operación");
        }    
    }
    public int dimeSaldo(){
        return saldo;
    }
}
