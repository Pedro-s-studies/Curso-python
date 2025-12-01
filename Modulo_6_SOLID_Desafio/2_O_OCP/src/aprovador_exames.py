from exames.exame_aprovavel import ExameAprovavel


class AprovadorExames:

    def aprovar_solicitacao_exame(self, exame: ExameAprovavel):
        exame.aprovar()
