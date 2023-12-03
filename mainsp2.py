# Inicialização do status das opções
opcoes = {
    1: {"nome": "Libras (Língua Brasileira de Sinais)", "descricao_curta": "Libras", "status": "Off"},
    2: {"nome": "Alto Contraste", "descricao_curta": "Alto Contraste", "status": "Off"},
    3: {"nome": "Daltonismo", "descricao_curta": "Modo Daltonismo", "status": "Off","modo_daltonismo": None},
    4: {"nome": "Aumentar tamanho da fonte", "descricao_curta": "Aumentar Tamanho da Fonte", "status": "Off"},
    5: {"nome": "Diminuir tamanho da fonte", "descricao_curta": "Diminuir Tamanho da Fonte", "status": "Off"},
}

# Modos de daltonismo disponíveis
modos_daltonismo = {
    1: {"nome": "Deuteranopia"},
    2: {"nome": "Protanopia"},
    3: {"nome": "Tritanopia"},
}

# Função para alternar o status de uma opção como um interruptor (on/off)
def alternar_opcao(opcao):
    if opcoes[opcao]["status"] == "Off" and opcao:
        opcoes[opcao]["status"] = "On"
        print(f"{opcoes[opcao]['descricao_curta']} agora está ativado.")
    else:
        opcoes[opcao]["status"] = "Off"
        print(f"{opcoes[opcao]['descricao_curta']} agora está desativado.")

# Função para exibir informações sobre Libras e alternar o status da opção 1
def exibir_informacoes_libras():
    alternar_opcao(1)
    print("\nInformações sobre Libras:")
    print("A Língua Brasileira de Sinais (Libras) é a língua utilizada pela comunidade surda no Brasil.")
    print("É uma língua visual e gestual, com estrutura gramatical própria.")
    print("Utilize-a para se comunicar eficientemente com pessoas surdas.")
    print(f"\nStatus da opção: {opcoes[1]['status']}")

# Função para exibir informações sobre Alto Contraste e alternar o status da opção 2
def exibir_informacoes_alto_contraste():
    alternar_opcao(2)
    print("\nInformações sobre Alto Contraste:")
    print("O modo de Alto Contraste melhora a visibilidade para pessoas com baixa visão.")
    print("Ative-o para facilitar a identificação de elementos na tela.")
    print(f"Status da opção: {opcoes[2]['status']}\n")

# Função para selecionar o modo para daltonismo e alternar o status da opção 3
def selecionar_modo_daltonismo():
    print("\nSelecione o tipo de daltonismo:")
    for modo, dados_modo in modos_daltonismo.items():
        print(f"{modo}. {dados_modo['nome']}")
    print("4. Desativar modo para daltonismo")

    try:
        modo = int(input("\nInforme o valor numérico do modo: "))
        if modo == 4:
            opcoes[3]["modo_daltonismo"] = None
            opcoes[3]["status"] = "Off"
            print("O Modo para daltonismo agora está desativado")
        elif modo in modos_daltonismo:
            opcoes[3]["modo_daltonismo"] = modos_daltonismo[modo]["nome"]
            opcoes[3]["status"] = "On"
            print(f"\nO Modo para daltonismo agora está ativado: {modos_daltonismo[modo]['nome']}")
        else:
            print("Modo inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Informe novamente um valor numérico.")

# Função para exibir informações sobre Modo Daltonismo e alternar o status da opção 3
def exibir_informacoes_modo_daltonismo():
    alternar_opcao(3)
    print("\nInformações sobre o Modo Daltonismo:")
    print("Este modo ajusta as cores na tela para melhorar a visualização de pessoas com daltonismo.")
    print("Selecione o modo desejado ou desative-o para retornar às cores normais.")
    print(f"Status da opção: {opcoes[3]['status']}, Modo: {opcoes[3]['modo_daltonismo']}\n")

# Função para aumentar o tamanho da fonte e alternar o status da opção 4
def aumentar_tamanho_fonte():
    alternar_opcao(4)
    print("\nAumentando o tamanho da fonte:")
    print("O tamanho da fonte será aumentado para facilitar a leitura.\n")
    print(f"Status da opção: {opcoes[4]['status']}\n")
    print("Texto em tamanho grande: MENU ACESSÍVEL SALESFORCE")

# Função para diminuir o tamanho da fonte e alternar o status da opção 5
def diminuir_tamanho_fonte():
    alternar_opcao(5)
    print("\nDiminuindo o tamanho da fonte:")
    print("O tamanho da fonte será reduzido para facilitar a leitura.\n")
    print(f"Status da opção: {opcoes[5]['status']}\n")
    print("Texto em tamanho pequeno: menu acessível salesforce")

# Função para mostrar opções ativadas
def mostrar_opcoes_ativadas():
    opcoes_ativadas = [dados['nome'] for opcao, dados in opcoes.items() if dados["status"] == "On"]
    if opcoes_ativadas:
        print("\nOpções ativadas:\n")
        for opcao_ativada in opcoes_ativadas:
            print(opcao_ativada)
    else:
        print("\nNenhuma opção está ativa no momento.")

# Função para obter uma escolha válida do usuário
def obter_escolha_valida():
    escolha = input("Informe o número da sua escolha: ")
    
    if escolha.isdigit() and 1 <= int(escolha) <= 7:
        return int(escolha)
    else:
        print("Entrada inválida. Por favor, escolha um valor numérico entre 1 e 7.")
        return obter_escolha_valida()

# Loop principal do programa
while True:
    print("\n===> MENU ACESSÍVEL <===")
    print("\nSelecione a opção desejada conforme sua preferência:\n")
    for opcao, dados in opcoes.items():
        print(f"{opcao}. {dados['nome']} ({dados['status']}) {dados['modo_daltonismo'] if 'modo_daltonismo' in dados and dados['modo_daltonismo'] is not None else ''}")
    print("6. Mostrar opções que estão ativas")
    print("7. Fechar menu\n")

    escolha = obter_escolha_valida()
    
    if escolha == 7:
        break
    elif escolha == 1:
        exibir_informacoes_libras()
    elif escolha == 2:
        exibir_informacoes_alto_contraste()
    elif escolha == 3:
        exibir_informacoes_modo_daltonismo()
        selecionar_modo_daltonismo()
    elif escolha == 4:
        aumentar_tamanho_fonte()
    elif escolha == 5:
        diminuir_tamanho_fonte()
    elif escolha == 6:
        mostrar_opcoes_ativadas()
