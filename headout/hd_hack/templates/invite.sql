-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Feb 07, 2016 at 10:51 AM
-- Server version: 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `invite`
--

-- --------------------------------------------------------

--
-- Table structure for table `hd_hack_event_table`
--

CREATE TABLE IF NOT EXISTS `hd_hack_event_table` (
  `event_id` int(250) NOT NULL,
  `event_name` varchar(500) NOT NULL,
  `event_desc` varchar(500) NOT NULL,
  `event_location` varchar(500) NOT NULL,
  `event_start_date` varchar(500) NOT NULL,
  `event_end_date` varchar(500) NOT NULL,
  `event_created_at` varchar(500) NOT NULL,
  `event_updated_at` varchar(500) NOT NULL,
  `created_by_id` varchar(500) NOT NULL,
  `updated_by_id` varchar(500) NOT NULL,
  `delivery_boys` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `hd_hack_user_location`
--

CREATE TABLE IF NOT EXISTS `hd_hack_user_location` (
`id` int(250) NOT NULL,
  `current_location` varchar(250) NOT NULL,
  `last_updated` varchar(250) NOT NULL,
  `user_iden_id` varchar(250) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hd_hack_user_location`
--

INSERT INTO `hd_hack_user_location` (`id`, `current_location`, `last_updated`, `user_iden_id`) VALUES
(1, 'dfsd', '1454783239', 'zr5hx4nn9o42qb3fc6xo7794u'),
(2, 'dfsd', '1454783454', 'zr5hx4nn9o42qb3fc6xo7794u'),
(3, 'dfsd', '1454783460', 'zr5hx4nn9o42qb3fc6xo7794u'),
(4, 'dfsd', '1454783461', 'zr5hx4nn9o42qb3fc6xo7794u'),
(5, 'dfsd', '1454783462', 'zr5hx4nn9o42qb3fc6xo7794u'),
(6, 'dfsd', '1454783463', 'zr5hx4nn9o42qb3fc6xo7794u'),
(7, 'dfsd', '1454783464', 'zr5hx4nn9o42qb3fc6xo7794u'),
(8, 'dfsd', '1454783464', 'zr5hx4nn9o42qb3fc6xo7794u'),
(9, 'dfsd', '1454783465', 'zr5hx4nn9o42qb3fc6xo7794u'),
(10, 'dfsd', '1454783466', 'zr5hx4nn9o42qb3fc6xo7794u'),
(11, 'dfsd', '1454783498', 'zr5hx4nn9o42qb3fc6xo7794u'),
(12, 'dfsd', '1454783498', 'zr5hx4nn9o42qb3fc6xo7794u'),
(13, 'dfsd', '1454783499', 'zr5hx4nn9o42qb3fc6xo7794u'),
(14, 'dfsd', '1454783499', 'zr5hx4nn9o42qb3fc6xo7794u'),
(15, 'dfsd', '1454783500', 'zr5hx4nn9o42qb3fc6xo7794u'),
(16, 'dfsd', '1454783500', 'zr5hx4nn9o42qb3fc6xo7794u'),
(17, 'dfsd', '1454783500', 'zr5hx4nn9o42qb3fc6xo7794u'),
(18, 'dfsd', '1454783501', 'zr5hx4nn9o42qb3fc6xo7794u'),
(19, 'dfsd', '1454783501', 'zr5hx4nn9o42qb3fc6xo7794u'),
(20, 'dfsd', '1454783501', 'zr5hx4nn9o42qb3fc6xo7794u'),
(21, 'dfsd', '1454783502', 'zr5hx4nn9o42qb3fc6xo7794u');

-- --------------------------------------------------------

--
-- Table structure for table `hd_hack_user_table`
--

CREATE TABLE IF NOT EXISTS `hd_hack_user_table` (
  `user_iden` varchar(500) NOT NULL,
  `f_name` varchar(500) NOT NULL,
  `l_name` varchar(500) NOT NULL,
  `email` varchar(500) NOT NULL,
  `phone` varchar(500) NOT NULL,
  `password` varchar(500) NOT NULL,
  `created_at` varchar(500) NOT NULL,
  `updated_at` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hd_hack_user_table`
--

INSERT INTO `hd_hack_user_table` (`user_iden`, `f_name`, `l_name`, `email`, `phone`, `password`, `created_at`, `updated_at`) VALUES
('0nv0e5568vuzh10vf13mrqfqx', 'dhfj', 'ufuf', 'ydhfj', '86868688', 'xbxbc', '0000-00-00', '0000-00-00'),
('3967', 'Sanjay', 'T', 'thillaivasan.sanjay@gmail.com', '9952491480', 'Headout123', 'Sun, 07 Feb 16 06:33:30 +0500', 'Sun, 07 Feb 16 06:33:30 +0500'),
('984zbviqs81ddpnvxo1froo50', 'chhh', 'jcjc', 'hxh', '76686', 'hxh', '0000-00-00', '0000-00-00'),
('btox5f0tyk08xhutuu1s3bu42', 'uffi', 'duf', 'ydfu', '0', 'dxh', '0000-00-00', '0000-00-00'),
('cldfvm6wtgz0iqx4khq253xrk', 'hji', 'hi', 'uoyi', '36566', 'gjii', '0000-00-00', '0000-00-00'),
('k7t7lpp0y3zrc24litwsnwfga', 'hji', 'hi', 'uoyhdjjs', '12345', '1234', '0000-00-00', '0000-00-00'),
('n73ir8p5uowp23t6ja89h0zxy', 'vuv', 'ugu', 'guguhihih', '9573602861', 'vuvj ', '0000-00-00', '0000-00-00'),
('zemaffizpvq1hrn89zot6adzh', 'hji', 'hi', 'uoyhdjjsgh', '123', '123', '0000-00-00', '0000-00-00'),
('zr5hx4nn9o42qb3fc6xo7794u', '2121', 'dsds', '123@gm', '5454', '123', '0000-00-00', '0000-00-00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hd_hack_event_table`
--
ALTER TABLE `hd_hack_event_table`
 ADD PRIMARY KEY (`event_id`);

--
-- Indexes for table `hd_hack_user_location`
--
ALTER TABLE `hd_hack_user_location`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hd_hack_user_table`
--
ALTER TABLE `hd_hack_user_table`
 ADD PRIMARY KEY (`user_iden`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hd_hack_user_location`
--
ALTER TABLE `hd_hack_user_location`
MODIFY `id` int(250) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=22;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
