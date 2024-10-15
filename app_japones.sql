-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 15-Out-2024 às 00:23
-- Versão do servidor: 5.7.36
-- versão do PHP: 8.1.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `app_japones`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcionarios`
--

CREATE TABLE `funcionarios` (
  `CPF` int(11) NOT NULL,
  `nome` varchar(60) NOT NULL,
  `função` varchar(60) NOT NULL,
  `RG` int(11) NOT NULL,
  `telefone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `mesas`
--

CREATE TABLE `mesas` (
  `Núm_Mesas` smallint(6) NOT NULL,
  `ID_Setor` int(11) NOT NULL,
  `Qtd_Cadeiras` smallint(6) NOT NULL,
  `CPF_Fun` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `pedidos`
--

CREATE TABLE `pedidos` (
  `Núm_Pedido` int(11) NOT NULL,
  `CPF` int(11) NOT NULL,
  `codigo` int(11) NOT NULL,
  `Núm_Mesas` smallint(6) NOT NULL,
  `data` float NOT NULL,
  `hora` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `produtos`
--

CREATE TABLE `produtos` (
  `codigo` int(11) NOT NULL,
  `descrição` varchar(60) NOT NULL,
  `preço` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `setor`
--

CREATE TABLE `setor` (
  `ID_Setor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `funcionarios`
--
ALTER TABLE `funcionarios`
  ADD PRIMARY KEY (`CPF`);

--
-- Índices para tabela `mesas`
--
ALTER TABLE `mesas`
  ADD PRIMARY KEY (`Núm_Mesas`),
  ADD KEY `ID_Setor` (`ID_Setor`);

--
-- Índices para tabela `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`Núm_Pedido`),
  ADD KEY `CPF` (`CPF`),
  ADD KEY `codigo` (`codigo`),
  ADD KEY `Núm_Mesas` (`Núm_Mesas`);

--
-- Índices para tabela `produtos`
--
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`codigo`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `mesas`
--
ALTER TABLE `mesas`
  ADD CONSTRAINT `mesas_ibfk_1` FOREIGN KEY (`ID_Setor`) REFERENCES `área` (`ID_Setor`);

--
-- Limitadores para a tabela `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`CPF`) REFERENCES `funcionarios` (`CPF`),
  ADD CONSTRAINT `pedidos_ibfk_2` FOREIGN KEY (`codigo`) REFERENCES `produtos` (`codigo`),
  ADD CONSTRAINT `pedidos_ibfk_3` FOREIGN KEY (`Núm_Mesas`) REFERENCES `mesas` (`Núm_Mesas`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
