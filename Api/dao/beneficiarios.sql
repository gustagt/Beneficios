-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Tempo de geração: 19/10/2022 às 15:03
-- Versão do servidor: 10.3.34-MariaDB-0ubuntu0.20.04.1
-- Versão do PHP: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `beneficiarios`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `beneficiarios`
--

CREATE TABLE `beneficiarios` (
  `cpf` bigint(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `data_nascimento` date NOT NULL,
  `endereco` varchar(50) NOT NULL,
  `telefone` bigint(11) DEFAULT NULL,
  `celular` bigint(11) NOT NULL,
  `rg` varchar(15) NOT NULL,
  `data_obito` date DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `c_documentos` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Despejando dados para a tabela `beneficiarios`
--

INSERT INTO `beneficiarios` (`cpf`, `nome`, `data_nascimento`, `endereco`, `telefone`, `celular`, `rg`, `data_obito`, `email`, `c_documentos`) VALUES
(12235565533, 'gustavo augusto', '2014-10-01', 'rua teste bairro teste', 31956564025, 31975756633, 'MG 25402222', '2022-10-05', 'GUSTAVO@GUSTAVO.COM', 'teste');

-- --------------------------------------------------------

--
-- Estrutura para tabela `deficiente`
--

CREATE TABLE `deficiente` (
  `n_credencial` int(11) NOT NULL,
  `deficiencia` varchar(45) NOT NULL,
  `tipo_deficiencia` varchar(45) NOT NULL,
  `ocupacao` varchar(15) NOT NULL,
  `data_emissao` date DEFAULT NULL,
  `data_validade` date DEFAULT NULL,
  `segunda_via` date DEFAULT NULL,
  `terceira_via` date DEFAULT NULL,
  `primeiro_recadastro` date DEFAULT NULL,
  `segundo_recadastro` date DEFAULT NULL,
  `terceiro_recadastro` date DEFAULT NULL,
  `observacoes` varchar(150) DEFAULT NULL,
  `beneficiarios_cpf` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Despejando dados para a tabela `deficiente`
--

INSERT INTO `deficiente` (`n_credencial`, `deficiencia`, `tipo_deficiencia`, `ocupacao`, `data_emissao`, `data_validade`, `segunda_via`, `terceira_via`, `primeiro_recadastro`, `segundo_recadastro`, `terceiro_recadastro`, `observacoes`, `beneficiarios_cpf`) VALUES
(2154, 'fisica', 'irreversivel', 'motorista', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 12235565533);

-- --------------------------------------------------------

--
-- Estrutura para tabela `idoso`
--

CREATE TABLE `idoso` (
  `n_credencial` int(11) NOT NULL,
  `ocupacao` varchar(15) NOT NULL,
  `data_emissao` date DEFAULT NULL,
  `data_validade` date DEFAULT NULL,
  `segunda_via` date DEFAULT NULL,
  `terceira_via` date DEFAULT NULL,
  `primeiro_recadastro` date DEFAULT NULL,
  `segundo_recadastro` date DEFAULT NULL,
  `terceiro_recadastro` date DEFAULT NULL,
  `observacoes` varchar(150) DEFAULT NULL,
  `beneficiarios_cpf` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Despejando dados para a tabela `idoso`
--

INSERT INTO `idoso` (`n_credencial`, `ocupacao`, `data_emissao`, `data_validade`, `segunda_via`, `terceira_via`, `primeiro_recadastro`, `segundo_recadastro`, `terceiro_recadastro`, `observacoes`, `beneficiarios_cpf`) VALUES
(2154, 'motorista', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'tste', 12235565533);

-- --------------------------------------------------------

--
-- Estrutura para tabela `protocolo`
--

CREATE TABLE `protocolo` (
  `n_protocolo` int(11) NOT NULL,
  `servico` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  `beneficiarios_cpf` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Despejando dados para a tabela `protocolo`
--

INSERT INTO `protocolo` (`n_protocolo`, `servico`, `status`, `beneficiarios_cpf`) VALUES
(2541, 'criar credencial', 'aberto', 12235565533);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `beneficiarios`
--
ALTER TABLE `beneficiarios`
  ADD PRIMARY KEY (`cpf`),
  ADD UNIQUE KEY `email_UNIQUE` (`email`);

--
-- Índices de tabela `deficiente`
--
ALTER TABLE `deficiente`
  ADD PRIMARY KEY (`n_credencial`),
  ADD KEY `fk_deficiente_beneficiarios1_idx` (`beneficiarios_cpf`);

--
-- Índices de tabela `idoso`
--
ALTER TABLE `idoso`
  ADD PRIMARY KEY (`n_credencial`),
  ADD KEY `fk_idoso_beneficiarios_idx` (`beneficiarios_cpf`);

--
-- Índices de tabela `protocolo`
--
ALTER TABLE `protocolo`
  ADD PRIMARY KEY (`n_protocolo`),
  ADD KEY `fk_protocolo_beneficiarios1_idx` (`beneficiarios_cpf`);

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `deficiente`
--
ALTER TABLE `deficiente`
  ADD CONSTRAINT `fk_deficiente_beneficiarios1` FOREIGN KEY (`beneficiarios_cpf`) REFERENCES `beneficiarios` (`cpf`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Restrições para tabelas `idoso`
--
ALTER TABLE `idoso`
  ADD CONSTRAINT `fk_idoso_beneficiarios` FOREIGN KEY (`beneficiarios_cpf`) REFERENCES `beneficiarios` (`cpf`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Restrições para tabelas `protocolo`
--
ALTER TABLE `protocolo`
  ADD CONSTRAINT `fk_protocolo_beneficiarios1` FOREIGN KEY (`beneficiarios_cpf`) REFERENCES `beneficiarios` (`cpf`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
