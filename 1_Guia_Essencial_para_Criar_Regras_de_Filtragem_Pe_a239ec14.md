**Guia Essencial para Criar Regras de Filtragem Personalizadas com Módulos**

**Introdução**

As regras de filtragem personalizadas permitem que você controle com precisão quais dados são mostrados em seus resultados do Google Analytics. Ao usar módulos, você pode criar regras complexas que são fáceis de manter e reutilizar.

**Benefícios de usar módulos**

* **Regras mais robustas:** Crie regras complexas que não são possíveis com os filtros padrão.
* **Facilidade de manutenção:** Modifique ou estenda as regras facilmente, sem precisar reescrever tudo.
* **Reutilização:** Reutilize módulos em várias regras para economizar tempo e esforço.

**Criando regras de filtragem personalizadas com módulos**

1. **Criar um novo filtro**

* Acesse a guia "Admin" no Google Analytics.
* Clique em "Filtros" em "Propriedade".
* Clique em "Adicionar filtro".

2. **Selecione o tipo de filtro**

* Selecione "Filtro personalizado" na lista suspensa "Tipo de filtro".

3. **Definir o escopo do filtro**

* Selecione os dados que deseja filtrar ("Visualizações" ou "Todos os dados").

4. **Criar módulos**

* **Módulo de campo:** Selecione o campo que deseja filtrar, como "Cidade" ou "Fonte".
* **Módulo de operador:** Selecione o operador lógico que deseja usar, como "Igual a" ou "Contém".
* **Módulo de valor:** Especifique o valor que deseja filtrar, como "Nova York" ou "Pesquisa orgânica".

**Exemplo**

Para criar uma regra que filtre as sessões de usuários de Nova York, você usaria os seguintes módulos:

* **Módulo de campo:** Cidade
* **Módulo de operador:** Igual a
* **Módulo de valor:** Nova York

**Conectando módulos**

* Use parênteses para agrupar módulos.
* Use operadores lógicos (E, OU) para combinar módulos.

**Diagrama de árvore de exemplo**

```
(
  (Módulo de campo: Cidade)
  (Módulo de operador: Igual a)
  (Módulo de valor: Nova York)
)
```

**Regras de filtragem personalizadas avançadas**

* **Usar expressões regulares:** Use o operador "Corresponde à expressão regular" para filtrar dados com base em padrões avançados.
* **Criar vários módulos:** Crie regras complexas conectando vários módulos com operadores lógicos.
* **Negar regras:** Use o operador "Não" para negar uma condição de filtragem.

**Dicas para criar regras eficazes**

* **Teste suas regras:** Teste suas regras em um ambiente de teste antes de aplicá-las a dados ativos.
* **Documentar suas regras:** Adicione notas para explicar o propósito e a lógica de cada regra.
* **Revise suas regras regularmente:** Revise suas regras periodicamente para garantir que ainda estejam atendendo às suas necessidades.