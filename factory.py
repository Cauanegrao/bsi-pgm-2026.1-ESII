class EquipamentoFactory:
    @staticmethod
    def criar(tipo, codigo, modelo, *args, **kwargs):
        tipo_normalizado = tipo.lower()
        
        if tipo_normalizado == "notebook":
            from modelos import Notebook
            return Notebook(codigo=codigo, modelo=modelo)
        elif tipo_normalizado == "projetor":
            from modelos import Projetor
            return Projetor(codigo=codigo, modelo=modelo)
        else:
            raise ValueError(f"Tipo de equipamento desconhecido: {tipo}")
