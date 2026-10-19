"""Seus testes do Marco 1 (veja a seção 6 do ENUNCIADO_MARCO1.md).

Regras: pelo menos 8 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual ou np.allclose.
"""
import unittest

from elevatoria.dados import por_tag
from elevatoria.serie import SerieTemporal


class TestPorTagExemplo(unittest.TestCase):
    """Exemplo do formato. `por_tag` é código existente da base."""

    def test_lista_vazia(self):
        """Sem registros, por_tag devolve uma lista vazia."""
        self.assertEqual(por_tag([], "PT101"), [])


# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #4 (escreva-os ANTES de corrigir o defeito e confirme que falham).

# Monitoria de 19 de outubro
class TesteMovelTam(unittest.TestCase):
    def test_tamanho_janela(self):
        serie = SerieTemporal.de_lista([i for i in range(1000)])
        valores_janela = [1, 50, 200, 500]
        for jan in valores_janela:
            self.assertEqual(serie.media_movel(janela = jan), len(serie) - jan + 1)

if __name__ == "__main__":
    unittest.main()
