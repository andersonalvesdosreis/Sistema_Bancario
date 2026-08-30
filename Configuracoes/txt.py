
largura = 45
linha = "=" * largura
print(
    f"{linha}\n"
    f"| {'PAINEL DA BOLSA':^41} |\n"
    f"{linha}\n"
    f"   TICKER    |   LUCRO(R$)  | VALOR UNI(R$)\n"
    f"{linha}\n"
    f"[1] ⛽ PETR4 |   77.82B     |   R$ 38,50   |\n"
    f"[2] 🏦 ITUB4 |   43.82B     |   R$ 36,20   |\n"
    f"[3] ⛏️ VALE3  |   27.82B     |   R$ 61,10   |\n"
    f"[4] 🍻 ABEV3 |   15.19B     |   R$ 12,40   |\n"
    f"[5] 🏦 BBDC3 |   20.97B     |   R$ 13,80   |\n"
    f"{linha}"
)


def comprar_acao(saldo: float | int, num_da_acao: int) -> float:
    precos = {
        1: 38.50, # PETR4
        2: 36.20, # ITUB4
        3: 61.10, # VALE3
        4: 12.40, # ABEV3
        5: 13.80  # BBDC3
    }
    
    if num_da_acao not in precos:
        print("Opção de ação inválida!")
        return saldo

    quantidade = int(input('Deseja comprar quantas? '))
    
    if quantidade <= 0:
        print("A quantidade deve ser maior que zero!")
        return saldo

    preco_unitario = precos[num_da_acao]
    custo_total = preco_unitario * quantidade

    if saldo >= custo_total:
        saldo -= custo_total
        print(f"Compra realizada com sucesso! Custo total: R$ {custo_total:.2f}")
        print(f"Saldo restante: R$ {saldo:.2f}")
    else:
        print(f"Saldo insuficiente! Você precisa de R$ {custo_total:.2f}, mas tem R$ {saldo:.2f}")

    return saldo