-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 11 oct. 2024 à 12:17
-- Version du serveur : 8.3.0
-- Version de PHP : 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `stud_manage`
--

-- --------------------------------------------------------

--
-- Structure de la table `admins`
--

DROP TABLE IF EXISTS `admins`;
CREATE TABLE IF NOT EXISTS `admins` (
  `username` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `admins`
--

INSERT INTO `admins` (`username`, `password`) VALUES
('max', 'max123');

-- --------------------------------------------------------

--
-- Structure de la table `courses`
--

DROP TABLE IF EXISTS `courses`;
CREATE TABLE IF NOT EXISTS `courses` (
  `idcourse` int NOT NULL AUTO_INCREMENT,
  `coursename` varchar(50) NOT NULL,
  `coursecode` varchar(10) NOT NULL,
  `vh` int NOT NULL,
  `lecturer` varchar(50) NOT NULL,
  PRIMARY KEY (`idcourse`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `courses`
--

INSERT INTO `courses` (`idcourse`, `coursename`, `coursecode`, `vh`, `lecturer`) VALUES
(1, 'merise', 'bst/521', 30, '(\'drama T\',)'),
(2, 'poo', 'bst/5455', 45, 'linoG'),
(3, 'biologie', 'bst/12025', 50, 'drama'),
(4, 'python', 'bst/2420', 45, '(\'Alvareze\',)');

-- --------------------------------------------------------

--
-- Structure de la table `grades`
--

DROP TABLE IF EXISTS `grades`;
CREATE TABLE IF NOT EXISTS `grades` (
  `idgrade` int NOT NULL AUTO_INCREMENT,
  `student` varchar(50) NOT NULL,
  `course` varchar(50) NOT NULL,
  `grade` float NOT NULL,
  PRIMARY KEY (`idgrade`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `grades`
--

INSERT INTO `grades` (`idgrade`, `student`, `course`, `grade`) VALUES
(1, 'provi', 'math', 20),
(2, 'max', 'bio', 12),
(3, '002 - ciceron', 'poo - bst/5455', 12),
(4, 'biu-eed-049 - provi', 'poo - bst/5455', 15),
(5, 'biu-eed-049 - provi', 'biologie - bst/12025', 10),
(6, '050 - max', 'poo - bst/5455', 18);

-- --------------------------------------------------------

--
-- Structure de la table `students`
--

DROP TABLE IF EXISTS `students`;
CREATE TABLE IF NOT EXISTS `students` (
  `numero` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(50) NOT NULL,
  `age` int NOT NULL,
  `encourse` int NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `students`
--

INSERT INTO `students` (`numero`, `name`, `age`, `encourse`, `password`) VALUES
('050', 'max', 10, 2, ''),
('060', 'abby', 30, 3, ''),
('biu-eed-049', 'provi', 22, 10, 'azerty');

-- --------------------------------------------------------

--
-- Structure de la table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
CREATE TABLE IF NOT EXISTS `teachers` (
  `idteacher` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `telephone` int NOT NULL,
  `course` varchar(50) NOT NULL,
  PRIMARY KEY (`idteacher`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `teachers`
--

INSERT INTO `teachers` (`idteacher`, `name`, `telephone`, `course`) VALUES
(1, 'drama T', 65185065, 'biologie'),
(2, 'Alvareze', 65100101, 'python');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
