package pack;

public class ContaCorrente extends Conta{

    @Override
    public void imprimirExtrato() {
        System.out.println("Extrato conta corrente: ");
        System.out.println(String.format("Agencia: %d", super.agencia));
        System.out.println(String.format("Número: %d", super.numero));
        System.out.println(String.format("saldo: %.2f", super.saldo));

    }
}
