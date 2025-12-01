from src.aprovador_exames import AprovadorExames
from src.exames.exame_sangue import ExameSangue
from src.exames.exame_raio_x import ExameRaioX

aprovador = AprovadorExames()

exame1 = ExameSangue()
exame2 = ExameRaioX()

aprovador.aprovar_solicitacao_exame(exame1)
aprovador.aprovar_solicitacao_exame(exame2)
