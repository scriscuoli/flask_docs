-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 31, 2026 at 01:39 AM
-- Server version: 10.11.14-MariaDB-0ubuntu0.24.04.1
-- PHP Version: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `docs`
--

-- --------------------------------------------------------

--
-- Table structure for table `documents`
--

CREATE TABLE `documents` (
  `dID` int(11) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `document_page`
--

CREATE TABLE `document_page` (
  `dpID` int(11) NOT NULL,
  `dID` int(11) NOT NULL,
  `pID` int(11) NOT NULL,
  `dp_page_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `document_tag`
--

CREATE TABLE `document_tag` (
  `dtID` int(11) NOT NULL,
  `dID` int(11) NOT NULL,
  `tID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pages`
--

CREATE TABLE `pages` (
  `pID` int(11) NOT NULL,
  `path` varchar(200) NOT NULL,
  `sf_page_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `scanned_files`
--

CREATE TABLE `scanned_files` (
  `sfID` int(11) NOT NULL,
  `path` varchar(200) NOT NULL,
  `creation_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tags`
--

CREATE TABLE `tags` (
  `tID` int(11) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `uID` int(11) NOT NULL,
  `userName` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `firstName` varchar(50) NOT NULL,
  `lastName` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`uID`, `userName`, `password`, `firstName`, `lastName`) VALUES
(1, 'steve', '$2y$10$3Scb4yDVTTtAhfXyPMgJu.ZHoekaq9MsWtNp3c3FL1hYKZfozBTGm', 'Steve', 'Criscuoli'),
(2, 'admin', '$2y$10$RnnpvftcnRaB60h/.oQq9.JLui062wntcJ6Go251r1DmbW1oySILy', 'admin', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `documents`
--
ALTER TABLE `documents`
  ADD PRIMARY KEY (`dID`);

--
-- Indexes for table `document_page`
--
ALTER TABLE `document_page`
  ADD PRIMARY KEY (`dpID`);

--
-- Indexes for table `document_tag`
--
ALTER TABLE `document_tag`
  ADD PRIMARY KEY (`dtID`);

--
-- Indexes for table `pages`
--
ALTER TABLE `pages`
  ADD PRIMARY KEY (`pID`);

--
-- Indexes for table `scanned_files`
--
ALTER TABLE `scanned_files`
  ADD PRIMARY KEY (`sfID`);

--
-- Indexes for table `tags`
--
ALTER TABLE `tags`
  ADD PRIMARY KEY (`tID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `documents`
--
ALTER TABLE `documents`
  MODIFY `dID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `document_page`
--
ALTER TABLE `document_page`
  MODIFY `dpID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `document_tag`
--
ALTER TABLE `document_tag`
  MODIFY `dtID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pages`
--
ALTER TABLE `pages`
  MODIFY `pID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `scanned_files`
--
ALTER TABLE `scanned_files`
  MODIFY `sfID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tags`
--
ALTER TABLE `tags`
  MODIFY `tID` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
