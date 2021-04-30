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

noticia4 = Noticia(4, "url 4", "url img 4", titulo4, texto4, "26/04/2021")
noticia5 = Noticia(5, "url 5", "url img 5", "titulo 5", "texto 5", "26/04/2021")
noticia6 = Noticia(6, "url 6", "url img 6", "titulo 6", "texto 6", "12/03/2021")
noticia7 = Noticia(7, "url 7", "url img 7", "titulo 7", "texto 7", "12/03/2021")
noticia8 = Noticia(8, "url 8", "url img 8", "titulo 8", "texto 8", "12/03/2021")

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