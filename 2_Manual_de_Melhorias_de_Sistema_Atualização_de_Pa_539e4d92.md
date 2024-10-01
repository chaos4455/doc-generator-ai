## 📘 Manual de Melhorias de Sistema: Atualização de Pacotes com `pkg update`

### 📝 Tema: Atualizar o Patch do Sistema

#### 💻 Comando:

```
pkg update
```

### 🌐 Objetivo:

Obter as informações de patch mais recentes de repositórios online para atualizar o sistema.

### 🛠️ Etapas:

1. Abra um Terminal.
2. Digite `pkg update` e pressione Enter.
3. Insira a senha do administrador, se solicitado.
4. O Terminal exibirá uma lista dos patches disponíveis.
5. Revise a lista e observe quais patches deseja instalar.
6. Digite `y` para instalar todos os patches ou `n` para cancelar.

### 💡 Exemplos:

* Para atualizar todos os patches:

```
pkg update -y
```

* Para atualizar um patch específico:

```
pkg update --install <nome_do_patch>
```

### 🌳 Diagrama de Árvore:

```
pkg update
├── obter informações de patch mais recentes
└── atualizar sistema
```

### 🌐 Repositórios de Patch:

Os patches são obtidos de repositórios online específicos para o sistema operacional. Alguns repositórios comuns incluem:

* **Oracle Solaris:** https://pkg.oracle.com/solaris
* **Ubuntu:** http://packages.ubuntu.com
* **CentOS:** http://vault.centos.org
* **RHEL:** https://access.redhat.com/downloads

### 📝 Notas:

* `pkg update` buscará informações de patch, mas não instalará automaticamente as atualizações.
* É recomendável revisar a lista de patches e instalar apenas aqueles que são necessários ou recomendados.
* Manter o sistema atualizado com os patches mais recentes é essencial para segurança e estabilidade.