-- Dimensão de Pessoas (Clientes)
CREATE TABLE DimPessoa (
    codDimPessoa INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    cidade VARCHAR(50),
    estado VARCHAR(50),
    pais VARCHAR(50)
);

-- Dimensão de Tipos de Combustível
CREATE TABLE DimTipoEnergia (
    codDimTipoEnergia INTEGER PRIMARY KEY,
    descricaoTipo VARCHAR(25)
);

-- Dimensão de Veículos
CREATE TABLE DimVeiculo (
    codDimVeiculo INTEGER PRIMARY KEY,
    quilometragem INTEGER,
    categoria VARCHAR(50),
    fabricante VARCHAR(80),
    modelo VARCHAR(80),
    anoFabricacao INTEGER,
    codDimTipoEnergia INTEGER,
    CONSTRAINT fk_tipo_energia FOREIGN KEY (codDimTipoEnergia) 
        REFERENCES DimTipoEnergia(codDimTipoEnergia)
);

-- Dimensão de Funcionários (Vendedores)
CREATE TABLE DimFuncionario (
    codDimFuncionario INTEGER PRIMARY KEY,
    nome VARCHAR(30),
    genero CHAR(1), -- 'M' ou 'F'
    regiao VARCHAR(40)
);

-- Dimensão Temporal
CREATE TABLE DimCalendario (
    codCalendario INTEGER PRIMARY KEY,
    dataCompleta DATE,
    horario TIME,
    diaMes INTEGER,
    numeroMes INTEGER,
    anoCompleto INTEGER,
    nomeDiaSemana VARCHAR(15)
);

-- Tabela Fato: Aluguel de Veículos
CREATE TABLE FatoAluguel (
    codFatoAluguel INTEGER PRIMARY KEY,
    codDimPessoa INTEGER,
    codDimVeiculo INTEGER,
    codDimFuncionario INTEGER,
    codTempoInicio INTEGER,
    codTempoFim INTEGER,
    quantidadeDias INTEGER,
    precoPorDia DECIMAL(10, 2),
    CONSTRAINT fk_pessoa_fato FOREIGN KEY (codDimPessoa) REFERENCES DimPessoa(codDimPessoa),
    CONSTRAINT fk_veiculo_fato FOREIGN KEY (codDimVeiculo) REFERENCES DimVeiculo(codDimVeiculo),
    CONSTRAINT fk_funcionario_fato FOREIGN KEY (codDimFuncionario) REFERENCES DimFuncionario(codDimFuncionario),
    CONSTRAINT fk_tempo_inicio FOREIGN KEY (codTempoInicio) REFERENCES DimCalendario(codCalendario),
    CONSTRAINT fk_tempo_fim FOREIGN KEY (codTempoFim) REFERENCES DimCalendario(codCalendario)
);
