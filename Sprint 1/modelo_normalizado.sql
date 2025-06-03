-- Tabela de Pessoas (Clientes)
CREATE TABLE Pessoa (
    codPessoa INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    localidade VARCHAR(120)  -- Exemplo: "São Paulo - SP - Brasil"
);

-- Tabela de Tipos de Combustíveis
CREATE TABLE TipoCombustivel (
    codTipoCombustivel INTEGER PRIMARY KEY,
    descricao VARCHAR(30)
);

-- Tabela de Veículos
CREATE TABLE Veiculo (
    codVeiculo INTEGER PRIMARY KEY,
    quilometragem INTEGER,
    categoria VARCHAR(60),
    fabricante VARCHAR(80),
    modelo VARCHAR(80),
    anoFabricacao INTEGER,
    codTipoCombustivel INTEGER,
    CONSTRAINT fk_combustivel FOREIGN KEY (codTipoCombustivel) 
        REFERENCES TipoCombustivel(codTipoCombustivel)
);

-- Tabela de Funcionários (Vendedores)
CREATE TABLE Funcionario (
    codFuncionario INTEGER PRIMARY KEY,
    nome VARCHAR(50),
    genero CHAR(1), -- 'M' ou 'F'
    estadoAtuacao VARCHAR(40)
);

-- Tabela de Aluguéis (Locações)
CREATE TABLE Aluguel (
    codAluguel INTEGER PRIMARY KEY,
    codPessoa INTEGER,
    codVeiculo INTEGER,
    codFuncionario INTEGER,
    dataInicio DATE,
    horarioInicio TIME,
    diasAluguel INTEGER,
    valorDiaria DECIMAL(10, 2),
    dataFim DATE,
    horarioFim TIME,
    CONSTRAINT fk_pessoa FOREIGN KEY (codPessoa) REFERENCES Pessoa(codPessoa),
    CONSTRAINT fk_veiculo FOREIGN KEY (codVeiculo) REFERENCES Veiculo(codVeiculo),
    CONSTRAINT fk_funcionario FOREIGN KEY (codFuncionario) REFERENCES Funcionario(codFuncionario)
);
