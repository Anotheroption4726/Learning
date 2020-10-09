-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  ven. 26 juil. 2019 à 07:16
-- Version du serveur :  5.7.23
-- Version de PHP :  7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `tech_me_home`
--

-- --------------------------------------------------------

--
-- Structure de la table `messages_table`
--

DROP TABLE IF EXISTS `messages_table`;
CREATE TABLE IF NOT EXISTS `messages_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender` varchar(255) NOT NULL,
  `message` varchar(255) NOT NULL,
  `posting_date_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `messages_table`
--

INSERT INTO `messages_table` (`id`, `sender`, `message`, `posting_date_time`) VALUES
(40, 'Adrien', 'test', '2019-07-20 20:07:33'),
(41, 'Adrien', 'je m\'appelle Adrien', '2019-07-20 20:07:59'),
(42, 'Adrien', 'et oui c\'est moi', '2019-07-20 20:18:25'),
(43, 'Mario', 'Salut c Mario', '2019-07-20 20:18:45'),
(44, 'Mario', 'hahah', '2019-07-20 20:18:50'),
(45, 'Adrien', 'ah?', '2019-07-20 20:20:26'),
(46, 'Mario', 'bah quoi', '2019-07-20 20:20:55'),
(47, 'Jean', 'oi', '2019-07-20 20:26:49');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
