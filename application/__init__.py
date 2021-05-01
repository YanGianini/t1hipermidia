from flask import Flask
import os
from application.model.entity.estado import Estado
from application.model.entity.noticia import Noticia


app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))


estado1 = Estado("Rio de Janeiro", "RJ", "rj.png")
estado2 = Estado("São Paulo", "SP", "sp.png")
estado3 = Estado("Minas Gerais", "MG", "mg.png")
estado4 = Estado("Espirito Santo", "ES", "es.png")

estado_list = [estado1, estado2, estado3, estado4]

titulo1 = "Paes diz que fez 'reserva técnica' para 2ª dose contra a Covid no Rio"
texto1 = "Após se recuperar da Covid, prefeito do Rio participa na manhã desta quinta-feira da inauguração de novo posto drive-thru de vacinação na Base Aérea do Galeão. Essa é a primeira agenda oficial após ele ter sido reinfectado pelo coronavírus. O prefeito do Rio, <b>Eduardo Paes (DEM), disse nesta quinta-feira (29) que fez uma “reserva técnica” e por enquanto não deve faltar vacina para aplicação da 2ª dose contra a Covid-19 na capital. 'Apesar de ter tido uma liberação do Ministério da Saúde no sentido de que não se reservasse a segunda dose, tomamos o cuidado de fazer uma reserva técnica', falou o prefeito."

noticia1 = Noticia(1, "url 1", "paes1.jpeg", titulo1, texto1, "29/04/2021")

titulo2 = "Nova Iguaçu, na Baixada Fluminense, volta a aplicar 2ª dose da CoronaVac nesta sexta-feira"
texto2 = "Município suspendeu a vacinação na terça (27) por falta de doses. Nesta quinta (29) a prefeitura recebeu um lote de três mil doses exclusivas para segunda dose de CoronaVac. Imunização com AstraZeneca segue normal.A Prefeitura de Nova Iguaçu, na Baixadas Fluminense, informou que irá aplicar a segunda dose da vacina CoronaVac nesta sexta-feira (30).O município recebeu uma reserva técnica da vacina por parte do governo do estado nesta quinta-feira (29). A vacinação da segunda dose com CoronaVac tinha sido suspensa por falta de doses na terça-feira (27).Segundo a prefeitura, eles receberam um lote de três mil doses de CoronaVac para aplicação exclusiva da segunda dose."

noticia2 = Noticia(2, "url 2", "vacina2.jpg", titulo2, texto2, "12/03/2021")

titulo3 = "Número de casos de coronavírus registrados em SP nos últimos 30 dias é 50% maior que o total dos 100 primeiros dias da pandemia"
texto3 = "Estado de SP chega a 45.863 óbitos e 1.426.176 casos de Covid-19 no estado neste domingo (27). Procura por testes de Covid-19 aumentou por causa das festas de fim de ano. O número de novos casos de Covid-19 registrados no estado de São Paulo nos últimos 30 dias é 52% maior que o total de casos confirmados nos 100 primeiros dias da pandemia, segundo dados divulgados pelo governo estadual neste domingo (27).No período de 27 de novembro a 27 de dezembro, foram 196.909 novos casos confirmados no estado. De 26 de fevereiro, quando ocorreu a primeira confirmação da doença no país, a 4 de junho, o estado registrou 129.200 casos. O total de mortes por coronavírus no estado já chega a 45.863 óbitos e os casos confirmados totalizam 1.426.176 confirmações, conforme dados deste domingo (27). Foram 55 mortes e 2.836 casos nas últimas 24h em todo o estado."

noticia3 = Noticia(3, "url 3", "sp3.jpg", titulo3, texto3, "12/03/2021")

titulo4 = "Butantan localiza variante suíça do novo coronavírus em SP e confirma outro caso da sul-africana"
texto4 = "Variante suíça, conhecida pela sigla B.1.1.318, já tinha sido reportada em análise de Santa Catarina. Já a sul-africana, antes verificada em Sorocaba, agora foi achada em amostra coletada na Baixada Santista. Pesquisadores do Instituto Butantan identificaram, pela primeira vez no estado de São Paulo, a presença da variante suíça do novo coronavírus, a B.1.1.318. Além disso, a rede de monitoramento identificou um novo caso da variante sul-africana, a B.1.351."

noticia4 = Noticia(4, "url 4", "virus4.jpg", titulo4, texto4, "26/04/2021")

titulo5 = "COVID-19: Minas Gerais recebe o 15° lote de vacinas com 589.800 doses"
texto5 = "Minas Gerais recebeu, na noite desta quinta-feira (29/4), o 15º lote de vacinas contra a COVID-19, enviado pelo Ministério da Saúde. As 589.800 doses serão encaminhadas para a Rede de Frios, no Bairro Gameleira, na Região Oeste de Belo Horizonte."

noticia5 = Noticia(5, "url 5", "minas5.jpeg", titulo5, texto5, "26/04/2021")

titulo6 = "Minas Gerais ultrapassa 34 mil mortes por Covid-19"
texto6 = "Minas Gerais chegou, neste sábado (1º), a 34.036 mortes por Covid-19 desde o início da pandemia. De acordo com a Secretaria de Estado de Saúde (SES), 337 óbitos foram registrados nas últimas 24 horas. Os dados da SES ainda apontam que 76.236 pacientes estão em acompanhamento. Outros 1.256.330 já se recuperaram da doença. Ou seja, são pessoas que atendem a três pré-requisitos: estão há 72 horas assintomáticas; receberam alta hospitalar e/ou cumpriram isolamento domiciliar de dez dias; e estão sem intercorrências.. Já o número de casos atingiu 1.366.602. Foram 7.465 confirmações a mais em relação à véspera."

noticia6 = Noticia(6, "url 6", "minas6.jpg", titulo6, texto6, "12/03/2021")

titulo7 = "ES não tem mais cidades em risco extremo para a Covid-19"
texto7 = "O governador do Espírito Santo, Renato Casagrande (PSB), divulgou nesta sexta-feira (30) o novo mapa de risco da Covid-19. A nova classificação começa a valer na próxima segunda (3) e não tem cidades em risco extremo. No mapa atual, há cinco cidades na classificação máxima. O novo mapa também tem 56 municípios em risco alto e 22 em risco moderado. Não há cidades em risco baixo."

noticia7 = Noticia(7, "url 7", "mapa7.jpg", titulo7, texto7, "12/03/2021")

titulo8 = "Espírito Santo registra mais 12 mortes e 1.181 novos casos de covid-19 em 24 horas"
texto8 = "Em 24 horas, o Espírito Santo registrou mais 12 mortes em decorrência do novo coronavírus, segundo informações do Painel Covid-19, da Secretaria de Estado da Saúde (Sesa), atualizadas na tarde deste sábado (01). Com isso, o total de óbitos causados pela doença no Estado chegou a 9.536. Além disso, entre sexta-feira (30) e sábado (1), 1.181 novos casos de covid-19 foram contabilizados, elevando o total de infectados, desde o início da pandemia, para 437.862 no Espírito Santo. O Painel Covid-19 aponta, ainda, que 410.153 pessoas já conseguiram vencer a doença no Estado."

noticia8 = Noticia(8, "url 8", "es8.jpg", titulo8, texto8, "12/03/2021")

noticia_list = [noticia1, noticia2, noticia3, noticia4, noticia5, noticia6, noticia7, noticia8]

estado1.set_noticias(noticia1)
estado1.set_noticias(noticia2)
estado2.set_noticias(noticia3)
estado2.set_noticias(noticia4)
estado3.set_noticias(noticia5)
estado3.set_noticias(noticia6)
estado4.set_noticias(noticia7)
estado4.set_noticias(noticia8)


from application.controller import main_controller