#  definindo variaveis para evitar muito texto no meio codigo
#  --------------------------------------------INPUT-------------------------------------------------------------------------------------------------------------------------------------
TEM_SINTOMAS = "Você apresenta pelo menos 4 dos sintomas principais do COVID-19? (Tosse, febre, dor de garganta, congestão nasal, coriza, dor de cabeça, cansaço, dores pelo corpo)"
TEVE_CONTATO = "Você entrou em contato recentemente com alguém que foi diagnosticado com o vírus?"
FEZ_O_TESTE = "Você realizou o teste do COVID-19 desde que esses sintomas surgiram?"
ESTADO_GRAVE = "Você se encontra em estado grave de saúde?"
GRUPO_DE_RISCO = "Você se enquadra em um grupo de risco? (gestante; portador de doenças crônicas; problemas respiratórios; fumante; pessoa de extremos de idade, seja criança ou idoso)"
#  --------------------------------------------OUTPUT------------------------------------------------------------------------------------------------------------------------------------
INVALIDO = "Opção inválida, recomece a avaliação"
DIST_SOCIAL = "Baseado em suas respostas, a orientação é que você permaneça em distanciamento social"
ISOLAMENTO = "Baseado em suas respostas, a orientação é que você entre em isolamento"
INTERNACAO = "Baseado em suas respostas, a orientação é que você vá a um hospital para que possa ser internado"
FAZER_TESTE = "Baseado em suas respostas, a orientação é que você vá ao hospital para ser testado para o COVID-19"
oQuePrintar = INVALIDO
#  --------------------------------------------OPCOES------------------------------------------------------------------------------------------------------------------------------------
SIM_NAO = "(1) sim\n" + "(2) não" + "\n"
POSITIVO_NEGATIVO = "(1) não\n" + "(2) sim, deu positivo\n" + "(3) sim, deu negativo" + "\n"
#  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

resposta = input(TEM_SINTOMAS + "\n" + SIM_NAO)
if resposta == '2':
    resposta = input(TEVE_CONTATO + "\n" + SIM_NAO)
    if resposta == '1':
        oQuePrintar = ISOLAMENTO
    elif resposta == '2':
        oQuePrintar = DIST_SOCIAL
elif resposta == '1':
    resposta = input(FEZ_O_TESTE + "\n" + POSITIVO_NEGATIVO)
    if resposta == '1':
        oQuePrintar = FAZER_TESTE
    elif resposta == '3':
        oQuePrintar = DIST_SOCIAL
    elif resposta == '2':
        resposta = input(ESTADO_GRAVE + "\n" + SIM_NAO)
        if resposta == '1':
            oQuePrintar = INTERNACAO
        elif resposta == '2':
            resposta = input(GRUPO_DE_RISCO + "\n" + SIM_NAO)
            if resposta == '1':
                oQuePrintar = INTERNACAO
            elif resposta == '2':
                oQuePrintar = ISOLAMENTO

print(oQuePrintar)