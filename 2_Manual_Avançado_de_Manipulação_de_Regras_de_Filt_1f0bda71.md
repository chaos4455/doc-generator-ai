**Manual Avançado de Manipulação de Regras de Filtragem Baseadas em Módulos**

**Tópico: Criação de Regras de Filtragem Personalizadas Usando Módulos**

**Introdução:**

As regras de filtragem baseadas em módulos permitem que você filtre recursos com base em condições específicas definidas em módulos personalizados do Azure Functions. Este manual fornece instruções detalhadas sobre como criar regras de filtragem personalizadas usando módulos.

**Seção 1: Criando um Módulo de Filtro Personalizado**

1. **Criar um novo projeto do Azure Functions:** Crie um novo projeto do Azure Functions em seu ambiente do Azure.
2. **Adicionar um módulo personalizado:** Adicione um módulo personalizado ao projeto clicando em "Adicionar" -> "Função do Azure" -> "Módulo personalizado".
3. **Definir condições de filtro:** Dentro do módulo personalizado, defina as condições de filtro que determinarão quais recursos serão incluídos ou excluídos na regra de filtragem.

**Exemplo:**

```
public static bool Evaluate(Resource resource)
{
    if (resource.Type == "VirtualMachine" && resource.Location == "East US")
    {
        return true;
    }
    else
    {
        return false;
    }
}
```

**Seção 2: Criando uma Regra de Filtragem Baseada em Módulos**

1. **Navegar até Regras de Filtragem:** No portal do Azure, navegue até "Governança e Conformidade" -> "Conformidade do Azure" -> "Regras de Filtragem".
2. **Criar nova regra de filtragem:** Clique em "Criar regra de filtragem".
3. **Configurar os detalhes da regra:** Forneça um nome e uma descrição para a regra de filtragem.
4. **Adicionar módulo personalizado:** Selecione "Módulo personalizado" como o tipo de filtro e escolha o módulo personalizado criado na Seção 1.

**Exemplo de Diagrama de Árvore:**

```
Regras de Filtragem
    -> Criar Nova Regra de Filtragem
        -> Configurar Detalhes da Regra
            -> Adicionar Módulo Personalizado
```

**Conclusão:**

Este manual forneceu instruções detalhadas sobre como criar regras de filtragem personalizadas usando módulos no Azure. Ao seguir essas etapas, você pode filtrar recursos com base em condições específicas definidas em módulos personalizados, permitindo maior controle e personalização da conformidade de recursos.