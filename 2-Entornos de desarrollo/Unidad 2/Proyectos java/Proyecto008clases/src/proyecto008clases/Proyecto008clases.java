package proyecto008clases;

public class Proyecto008clases {

   public static void main(String[] args) {
        // En la instanciacion hay que indicar el tipo de datos
        // Cliente es el tipo de datos del objeto
        // Cliente1 es el nombre de la instancia que creo (aqui puedo poner todo lo que quiera)
        // new es la palabra reservada que usamos para instanciar
        //Cliente es la llamada a la clase (que lleva parametros de constructor)
        Cliente Cliente1 = new Cliente("Lucas Ezequiel","Andres Griego",31);
        System.out.println(Cliente1.edad);
        System.out.println(Cliente1.dameEdad());
   }
    
}
