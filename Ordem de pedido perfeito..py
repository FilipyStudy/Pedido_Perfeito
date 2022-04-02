print('''
__________               _____              __                                
\______   \ ____________/ ____\____   _____/  |_                              
 |     ___// __ \_  __ \   __\/ __ \_/ ___\   __\                             
 |    |   \  ___/|  | \/|  | \  ___/\  \___|  |                               
 |____|    \___  >__|   |__|  \___  >\___  >__|                               
               \/                 \/     \/                                   
________            .___                                                      
\_____  \_______  __| _/___________                                           
 /   |   \_  __ \/ __ |/ __ \_  __ \                                          
/    |    \  | \/ /_/ \  ___/|  | \/                                          
\_______  /__|  \____ |\___  >__|                                             
        \/           \/    \/                                                 
__________               _____                                                
\______   \ ____________/ ____\___________  _____ _____    ____   ____  ____  
 |     ___// __ \_  __ \   __\/  _ \_  __ \/     \\__  \  /    \_/ ___\/ __ \ 
 |    |   \  ___/|  | \/|  | (  <_> )  | \/  Y Y  \/ __ \|   |  \  \__\  ___/ 
 |____|    \___  >__|   |__|  \____/|__|  |__|_|  (____  /___|  /\___  >___  >
               \/                               \/     \/     \/     \/    \/ 
''')
print("Iniciando Script para análise da ordem perfeita.")
print("Insira os dados a seguir usando apenas valores numéricos:")


while True:
    entregas = int(input("Quantidade de pedidos entregues: ")) #ALTERE AQUI O TOTAL DO NÚMERO DE ENTREGAS DURANTE O PERÍODO ANÁLISADO
    reg_errado = int(input("Quantidade de pedidos regristrados erroneamente: ")) #NÚMERO DE PEDIDOS ERRADOS
    sep_errado = int(input("Quantidade de pedidos separados erroneamente: ")) #NÚMERO DE PEDIDOS SEPARADOS ERRRONEAMENTE
    ent_errado = int(input("Quantidade de pedidos entregues erroneamente: ")) #NÚMERO DE PEDIDOS ENTREGUES DE FORMA INCORRETA
    ava_errado = int(input("Quantidade de pedidos avariados: ")) #NÚMERO DE PEDIDOS QUE REGISTRARAM ALGUM TIPO DE AVARIA
    fat_errado = int(input("Quantidade de pedidos faturados erroneamente: ")) #NÚMERO DE PEDIDOS QUE FORAM FATURADOS DE FORMA ERRADA

    reg_errado2 = entregas - reg_errado
    sep_errado2 = entregas - sep_errado
    ent_errado2 = entregas - ent_errado
    ava_errado2 = entregas - ava_errado
    fat_errado2 = entregas - fat_errado

    aa = (reg_errado2 * 100) / entregas
    bb = (sep_errado2 * 100) / entregas
    cc = (ent_errado2 * 100) / entregas
    dd = (ava_errado2 * 100) / entregas
    ee = (fat_errado2 * 100) / entregas

    perfect_delivery = aa/100 * bb/100 * cc/100 * dd/100 * ee/100 * 100
    print("Ánalise de Ordem perfeita.")
    print("%2.2f%%" % aa)
    print("Porcentagem sem registros errados.")
    print("%2.2f%%" % bb)
    print("Porcentagem de pedidos separados corretamente.")
    print("%2.2f%%" % cc)
    print("Porcentagem de entregas corretas.")
    print("%2.2f%%" % dd)
    print("Porcentagem de entregas sem avarias.")
    print("%2.2f%%" % ee)
    print("Porcentagem de faturamento correta.")
    print("%2.2f%%" % perfect_delivery)
    print("Perfect Order Performance")

    if perfect_delivery < 90:
        print("Performance abaixo do esperado (menor que 90%)")
    else:
        print("Perfomance nos níveis esperados! (igual ou maior que 90%)")
    print("")
    print("Aguardando correção dos professores.")

    resetScript = str(input('Deseja reiniciar o script com outros valores? (S/N) -> '))
    if resetScript.lower() == 's':
        continue
    elif resetScript.lower() == 'n':
        print('Ok! Até a próxima.')
        break
    else:
        print('Você precisa digitar "S" ou "N" para escolher uma opção, por padrão o programa será encerrado!')
        break
