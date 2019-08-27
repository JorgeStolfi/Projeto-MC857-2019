Problemas no módulo `produto`

Interface `produto.py`:

Implementação `produto_IMP.py`:

* O efeito de um método ou função definido na interface deve ser documentada apenas na interface, não na implementação.
* O campo `_id` da classe `Usuario_IMP` pode se chamar só `id`.
* Os atributos devem ser armazenados num único campo `atrs`, cujo valor é um dicionário Python, em vez de campos separados do objeto.  Isso deixa a imlementação mais limpa.
* A função `cria` é uma função do módulo, e não um método da classe.
* A classe deve ser um método `__init__(self)` define `self.id` e `self.atrs` como `None`.
* A função `cria` deve criar um novo objeto da classe {Produto_IMP}, definir seu campo `atrs` como uma *cópia* do dicionário `atrs` passado como parâmetro, e chamar a função `base_produto.acrescenta` para definir o campo `id`.
* O método `muda_atributos` deve chamar `base_produtos.altera` para alterar também na base de dados.
