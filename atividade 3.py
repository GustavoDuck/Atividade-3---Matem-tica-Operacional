def avaliar_festa(ana_presente, bruno_presente, bruno_traz_musica):
    """Avalia se a festa será animada com base na presença de Ana, Bruno e se Bruno traz música."""
    festa_animada = (ana_presente and bruno_presente) or (not ana_presente and bruno_traz_musica)
    return festa_animada

def exibir_tabela():
    """Exibe a tabela verdade das proposições."""
    print("Tabela Verdade:")
    print("Ana | Bruno | Música | Festa Animada")
    print("----|-------|--------|---------------")
    for ana in [True, False]:
        for bruno in [True, False]:
            for musica in [True, False]:
                resultado_festa = avaliar_festa(ana, bruno, musica)
                print(f"{'Sim' if ana else 'Não'} | {'Sim' if bruno else 'Não'} | {'Sim' if musica else 'Não'} | {'Sim' if resultado_festa else 'Não'}")
    print()

def capturar_input(mensagem):
    """Captura e valida a entrada do usuário."""
    while True:
        resposta = input(mensagem)
        if resposta == "!s":
            print("Saindo do programa. Obrigado pela participação.")
            exit()
        if resposta not in ["S", "N"]:
            print("Digite apenas 'S' ou 'N'. Para sair, digite '!s'.")
            continue
        return resposta == "S"

def rodar_programa():
    """Executa o programa principal."""
    exibir_tabela()
    
    while True:
        print("Para sair, digite '!s' quando solicitado.")
        
        ana = capturar_input("Ana está presente? (S ou N): ")
        bruno = capturar_input("Bruno está presente? (S ou N): ")
        musica = capturar_input("Bruno traz música? (S ou N): ")

        festa = avaliar_festa(ana, bruno, musica)
        
        print("Resultado:")
        print(f"Ana: {'Sim' if ana else 'Não'} | Bruno: {'Sim' if bruno else 'Não'} | Música: {'Sim' if musica else 'Não'} | Festa: {'Sim' if festa else 'Não'}")
        break 

if __name__ == "__main__":
    rodar_programa()
