-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  ven. 26 juil. 2019 à 10:03
-- Version du serveur :  5.7.26
-- Version de PHP :  7.2.18

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
) ENGINE=MyISAM AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;

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
(47, 'Jean', 'oi', '2019-07-20 20:26:49'),
(48, 'Adrien', 'encore un test', '2019-07-26 07:21:18'),
(49, 'Adrien', 'Salut Je sA drie', '2019-07-26 11:34:45'),
(50, 'Mario', 'flisufilsdhgsdklghdlgl', '2019-07-26 11:35:07'),
(51, 'Adrien', 'reztzetre', '2019-07-26 11:58:34');

-- --------------------------------------------------------

--
-- Structure de la table `users_table`
--

DROP TABLE IF EXISTS `users_table`;
CREATE TABLE IF NOT EXISTS `users_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `users_table`
--

INSERT INTO `users_table` (`id`, `username`, `password`) VALUES
(1, 'Adrien', 'test'),
(4, 'Jean', 'test2'),
(9, 'Mario', 'luigi');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
