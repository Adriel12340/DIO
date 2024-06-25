package pack;

public class ContaPoupanca extends Conta{

    @Override
    public void imprimirExtrato() {
        System.out.println("Extrato conta poupança: ");
        System.out.println(String.format("Agencia: %d", super.agencia));
        System.out.println(String.format("Número: %d", super.numero));
        System.out.println(String.format("saldo: %.2f", super.saldo));

    }

}
