-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 11-Out-2024 às 23:45
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
-- Banco de dados: `maternidade`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `bebe`
--

CREATE TABLE `bebe` (
  `Codigo` int(11) NOT NULL,
  `Codigo_EQ` int(11) NOT NULL,
  `CPF` int(11) NOT NULL,
  `nome` varchar(60) NOT NULL,
  `data` varchar(11) NOT NULL,
  `peso` int(11) NOT NULL,
  `altura` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `equipe_médica`
--

CREATE TABLE `equipe_médica` (
  `nome` varchar(60) NOT NULL,
  `Codigo_EQ` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `mãe`
--

CREATE TABLE `mãe` (
  `CPF` int(11) NOT NULL,
  `nome` varchar(60) NOT NULL,
  `endereço` varchar(60) NOT NULL,
  `telefone` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `profissional`
--

CREATE TABLE `profissional` (
  `CRM` int(11) NOT NULL,
  `nome` varchar(60) NOT NULL,
  `telefone` varchar(60) NOT NULL,
  `especialidade` varchar(60) NOT NULL,
  `Codigo_EQ` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `bebe`
--
ALTER TABLE `bebe`
  ADD PRIMARY KEY (`Codigo`),
  ADD KEY `CPF` (`CPF`);

--
-- Índices para tabela `equipe_médica`
--
ALTER TABLE `equipe_médica`
  ADD PRIMARY KEY (`Codigo_EQ`);

--
-- Índices para tabela `mãe`
--
ALTER TABLE `mãe`
  ADD PRIMARY KEY (`CPF`);

--
-- Índices para tabela `profissional`
--
ALTER TABLE `profissional`
  ADD PRIMARY KEY (`CRM`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `bebe`
--
ALTER TABLE `bebe`
  ADD CONSTRAINT `bebe_ibfk_1` FOREIGN KEY (`CPF`) REFERENCES `maternidade` (`CPF`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
