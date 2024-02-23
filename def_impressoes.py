def calcular_impressoes_semanais(num_atual, num_anterior):
    return num_atual - num_anterior

def calcular_media_diaria(impressoes_semanais):
    return impressoes_semanais / 5

def calcular_custos(impressoes_projecao):
    return (impressoes_projecao - 3000) * 0.06 if impressoes_projecao > 3000 else 0

def gerar_impressoes_projecao(semanas):
    soma_impressoes = 0
    semana_atual = len(semanas)
    for semana in semanas:
        soma_impressoes += semanas[semana]
    media_semanal = soma_impressoes / semana_atual
    return media_semanal * 4

def main():
    numero_atual = int(input("Digite o número atual de impressões: "))
    numero_anterior = int(input("Digite o número anterior de impressões: "))
    impressoes_semanais = calcular_impressoes_semanais(numero_atual, numero_anterior)
    impressoes_dia = calcular_media_diaria(impressoes_semanais)
    
    semana_atual = int(input("Digite em qual semana estamos: "))
    semanas = {}
    for i in range(1, semana_atual):
        semana = input(f"Digite o número de impressões para a semana {i}: ")
        semanas[f'semana_{i}'] = int(semana)
    
    semanas[f'semana_{semana_atual}'] = impressoes_semanais
    
    impressoes_projecao = gerar_impressoes_projecao(semanas)
    
    meta = impressoes_projecao <= 3000
    custo = calcular_custos(impressoes_projecao)
    
    print("\nBoa tarde a todos.")
    print("\nSegue relatório de impressões semanais.")
    print(f"\nDurante a semana foram feitas {impressoes_semanais} impressões, isso representa {impressoes_dia:.2f} por dia.")
    
    if meta:
        print(f"\nCom isso, no momento estamos DENTRO da meta, se continuarmos assim, fecharemos o mês com {impressoes_projecao:.2f} impressões.")
    else:
        print(f"\nCom isso, no momento estamos FORA da meta, se continuarmos assim, fecharemos o mês com {impressoes_projecao:.2f} impressões.")
        print(f"\nAlém disso, o custo adicional estimado para este mês é de R${custo:.2f} devido ao excesso de impressões.")
    
    print("\nContamos com a colaboração de cada um para que possamos nos policiar quanto ao uso de impressões e trabalhar juntos para atingir nossa meta estabelecida. Pequenas mudanças em nossos hábitos podem fazer uma grande diferença na redução de custos e no impacto ambiental.")
    print("\nDesde já, obrigado.")

if __name__ == "__main__":
    main()
