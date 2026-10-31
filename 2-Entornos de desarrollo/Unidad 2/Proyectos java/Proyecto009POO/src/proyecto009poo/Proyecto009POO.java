package proyecto009poo;
// POO "Programacion orientada a objetos"
public class Proyecto009POO {

    public static void main(String[] args) {
        CuentaBancaria Cuenta1 = new CuentaBancaria();
        System.out.println("Cual es mi saldo?");
        System.out.println(Cuenta1.dimeSaldo());
        Cuenta1.imponerSaldo(1000);
        System.out.println("Cual es mi saldo?");
        System.out.println(Cuenta1.dimeSaldo());
        Cuenta1.retirarSaldo(100000000);
        System.out.println("Cual es mi saldo?");
        System.out.println(Cuenta1.dimeSaldo());
    }
    
}
