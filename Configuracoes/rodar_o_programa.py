import funcoes
import sistema_financeiro
import classe


cliente_num1 = classe.ContaBancaria(email=funcoes.email(), 
                                    senha=funcoes.senha_forte(), 
                                    nome=funcoes.nome(), 
                                    saldo=funcoes.saldo())

print(cliente_num1.tabela_moldura())