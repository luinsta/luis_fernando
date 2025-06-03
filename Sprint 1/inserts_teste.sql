-- Inserções para a tabela Cliente
INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
VALUES 
(1, 'Larissa Matos', 'Fortaleza', 'Ceará', 'Brasil'),
(2, 'Eduardo Lima', 'Recife', 'Pernambuco', 'Brasil'),
(3, 'Sofia Almeida', 'Salvador', 'Bahia', 'Brasil');

-- Inserções para a tabela Combustivel
INSERT INTO Combustivel (idCombustivel, tipoCombustivel)
VALUES 
(1, 'GNV'),
(2, 'Elétrico'),
(3, 'Gasolina');

-- Inserções para a tabela Carro
INSERT INTO Carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
VALUES 
(1, 12000, 'SUV', 'Jeep', 'Renegade', 2021, 1),
(2, 8000, 'Sedan', 'Tesla', 'Model 3', 2023, 2),
(3, 25000, 'Hatch', 'Volkswagen', 'Polo', 2020, 3);

-- Inserções para a tabela Vendedor
INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
VALUES 
(1, 'Roberta', 2, 'Ceará'),
(2, 'Felipe', 1, 'Pernambuco'),
(3, 'Camila', 2, 'Bahia');

-- Inserções para a tabela Locacao
INSERT INTO Locacao (idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
VALUES 
(1, 1, 2, 1, '2023-04-20', '08:30:00', 4, 180.00, '2023-04-24', '08:30:00'),
(2, 2, 1, 2, '2023-05-10', '11:00:00', 2, 220.00, '2023-05-12', '11:00:00'),
(3, 3, 3, 3, '2023-06-01', '15:45:00', 6, 150.00, '2023-06-07', '15:45:00');
