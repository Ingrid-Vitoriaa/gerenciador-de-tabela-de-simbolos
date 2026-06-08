class Simbolo:
    def __init__(self, nome, tipo, valor=None):
        self.nome = nome
        self.tipo = tipo.upper() 
        self.valor = valor

    def __repr__(self):
        return f"({self.tipo}, Valor: {self.valor})"


class SymbolTableManager:
    def __init__(self):
        self.stack = [{}]
        self.tipos_validos = {"INT", "FLOAT", "STRING", "BOOLEAN"}

    def enter_scope(self):
        self.stack.append({})
        print(f"->Entrou no escopo nível {len(self.stack) - 1}.")

    def exit_scope(self):
        if len(self.stack) > 1:
            removed = self.stack.pop()
            print(f"<-Saiu do escopo. Variáveis liberadas: {list(removed.keys())}")
        else:
            print("Violação de escopo. O escopo global não pode ser encerrado.")

    def declarar(self, nome, tipo):
        tipo_UP = tipo.upper()
        if tipo_UP not in self.tipos_validos:
            print(f" Tipo '{tipo}' é inválido. Tipos aceitos: {self.tipos_validos}")
            return False

        escopo_atual = self.stack[-1]
        if nome in escopo_atual:
            print(f"Variável '{nome}' já declarada neste escopo (Redeclaração Inválida).")
            return False
        
        escopo_atual[nome] = Simbolo(nome, tipo_UP)
        print(f" '{nome}' declarada como {tipo_UP} no nível {len(self.stack)-1}.")
        return True

    def atribuir(self, nome, valor):
        simbolo = self._buscar_objeto(nome)
        if not simbolo:
            print(f" Tentativa de atribuir valor à variável '{nome}', mas ela NÃO foi declarada.")
            return False

        tipo_correto = False
        if simbolo.tipo == "INT" and isinstance(valor, int) and not isinstance(valor, bool):
            tipo_correto = True
        elif simbolo.tipo == "FLOAT" and isinstance(valor, (int, float)):
            tipo_correto = True
        elif simbolo.tipo == "STRING" and isinstance(valor, str):
            tipo_correto = True
        elif simbolo.tipo == "BOOLEAN" and isinstance(valor, bool):
            tipo_correto = True

        if not tipo_correto:
            tipo_valor_recebido = type(valor).__name__.upper()
            print(f"Variável '{nome}' é {simbolo.tipo}, mas recebeu valor do tipo {tipo_valor_recebido} ({valor}).")
            return False

        simbolo.valor = valor
        print(f"Variável '{nome}' recebeu o valor: {valor}")
        return True

    def buscar(self, nome):
        simbolo = self._buscar_objeto(nome)
        if simbolo:
            for nivel, escopo in reversed(list(enumerate(self.stack))):
                if nome in escopo:
                    print(f"[BUSCA] '{nome}' ENCONTRADA no nível {nivel} | Tipo: {simbolo.tipo} | Valor Atual: {simbolo.valor}")
                    return simbolo.tipo
        print(f"[BUSCA] '{nome}' NÃO ENCONTRADA em nenhum escopo ativo.")
        return None

    def _buscar_objeto(self, nome):
        for escopo in reversed(self.stack):
            if nome in escopo:
                return escopo[nome]
        return None

    def exibir_estado(self):
        print("\n================== MAPA DA PILHA DE ESCOPOS ==================")
        for i in range(len(self.stack) - 1, -1, -1):
            tipo_escopo = "Global" if i == 0 else f"Local (Nível {i})"
            print(f" [{tipo_escopo}] -> {self.stack[i]}")
        print("==============================================================\n")



if __name__ == "__main__":
    manager = SymbolTableManager()
    
    print("========================================================")
    print("  GERENCIADOR DE ANÁLISE SEMÂNTICA E TABELA DE SÍMBOLOS")
    print("========================================================\n")
    
    print("--- Inicialização do Escopo Global e Atribuição Correta ---")
    manager.declarar("idade", "int")
    manager.atribuir("idade", 21)       
    manager.declarar("salario", "float")
    manager.atribuir("salario", 1500.50)
    manager.buscar("idade")
    manager.exibir_estado()
    
    print("--- Entrada de Escopo, Shadowing e Verificação de Tipos ---")
    manager.enter_scope()
    manager.declarar("nome", "string")
    manager.atribuir("nome", "Ana")
    
    print("\n[Testando Shadowing]")
    manager.declarar("idade", "boolean")
    manager.atribuir("idade", True) 
    manager.buscar("idade")          
    manager.exibir_estado()
    
    print("---Teste Estrito de Erros Semânticos---")
    print("[Erro de Tipo - Type Mismatch]")
    manager.atribuir("nome", 12345)      
    
    print("\n[Erro de Redeclaração]")
    manager.declarar("nome", "float") 
    
    print("\n[Erro de Variável Não Declarada]")
    manager.atribuir("x", 10)          
    
    print("\n--- Destruição do Escopo e Retorno ao Estado Original ---")
    manager.exit_scope()
    manager.buscar("nome")            
    manager.buscar("idade")             
    manager.exibir_estado()