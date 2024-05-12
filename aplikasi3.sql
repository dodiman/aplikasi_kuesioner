-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 13, 2024 at 01:52 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aplikasi3`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('aea3d30bab4e');

-- --------------------------------------------------------

--
-- Table structure for table `jawaban_responden`
--

CREATE TABLE `jawaban_responden` (
  `id` int(11) NOT NULL,
  `responden_id` int(11) NOT NULL,
  `kuis_id` int(11) NOT NULL,
  `jawaban` varchar(50) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `jawaban_responden`
--

INSERT INTO `jawaban_responden` (`id`, `responden_id`, `kuis_id`, `jawaban`, `date_created`) VALUES
(10, 6, 3, 'salah', '2024-05-12 03:35:33'),
(11, 6, 5, 'salah', '2024-05-12 03:35:33'),
(12, 6, 6, 'Benar', '2024-05-12 03:35:33'),
(13, 6, 8, 'salah', '2024-05-12 03:35:33'),
(14, 7, 3, 'salah', '2024-05-12 03:40:53'),
(15, 7, 6, 'Benar', '2024-05-12 03:41:04'),
(16, 8, 3, 'Benar', '2024-05-12 03:44:43'),
(17, 6, 9, 'salah', '2024-05-13 05:27:30'),
(18, 6, 11, 'salah', '2024-05-13 05:27:30'),
(19, 6, 12, 'Benar', '2024-05-13 05:27:30');

-- --------------------------------------------------------

--
-- Table structure for table `kategori`
--

CREATE TABLE `kategori` (
  `id` int(11) NOT NULL,
  `kategori` varchar(100) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_modified` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `kategori`
--

INSERT INTO `kategori` (`id`, `kategori`, `date_created`, `date_modified`) VALUES
(1, 'UMUM', '2024-05-11 03:21:08', '2024-05-13 07:07:51'),
(2, 'KHUSUS', '2024-05-11 03:21:11', '2024-05-13 07:07:58'),
(3, 'SPESIAL', '2024-05-11 03:21:15', '2024-05-13 07:08:04');

-- --------------------------------------------------------

--
-- Table structure for table `kuis`
--

CREATE TABLE `kuis` (
  `id` int(11) NOT NULL,
  `teks` varchar(200) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `kategori_id` int(11) NOT NULL,
  `date_modified` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `kuis`
--

INSERT INTO `kuis` (`id`, `teks`, `date_created`, `kategori_id`, `date_modified`) VALUES
(3, 'Ikan bernafas dengan paru-paru', '2024-05-11 06:24:14', 1, '2024-05-12 21:44:00'),
(5, 'Indonesia termaksud negara maju', '2024-05-11 06:45:01', 2, '2024-05-13 07:06:29'),
(6, 'Amerika ibu kotanya New York', '2024-05-11 06:51:58', 2, '2024-05-13 04:02:29'),
(8, 'Batu tenggelam dalam air laut', '2024-05-11 15:14:00', 1, '2024-05-12 16:57:36'),
(9, 'Indonesia ibukotanya Jakarta', '2024-05-12 18:09:57', 1, '2024-05-13 07:06:46'),
(11, 'Sorong terletak dipulau Jawa', '2024-05-12 18:30:31', 1, '2024-05-13 07:07:11'),
(12, 'Ikan bernafas dengan paru-paru', '2024-05-12 21:47:18', 1, '2024-05-13 07:07:34');

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE `profile` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `responden`
--

CREATE TABLE `responden` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `responden`
--

INSERT INTO `responden` (`id`, `nama`, `alamat`, `date_created`) VALUES
(6, 'budi', 'takimpo', '2024-05-12 03:24:26'),
(7, 'andi', 'pasarwajo', '2024-05-12 03:40:53'),
(8, 'rudi', 'takimpo', '2024-05-12 03:44:11');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `role`) VALUES
(1, 'admin', 'admin', 'admin'),
(2, 'pimpinan', 'pimpinan', 'pimpinan');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `jawaban_responden`
--
ALTER TABLE `jawaban_responden`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kuis_id` (`kuis_id`),
  ADD KEY `responden_id` (`responden_id`);

--
-- Indexes for table `kategori`
--
ALTER TABLE `kategori`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kuis`
--
ALTER TABLE `kuis`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kategori_id` (`kategori_id`);

--
-- Indexes for table `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `responden`
--
ALTER TABLE `responden`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `jawaban_responden`
--
ALTER TABLE `jawaban_responden`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `kategori`
--
ALTER TABLE `kategori`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `kuis`
--
ALTER TABLE `kuis`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `profile`
--
ALTER TABLE `profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `responden`
--
ALTER TABLE `responden`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `jawaban_responden`
--
ALTER TABLE `jawaban_responden`
  ADD CONSTRAINT `jawaban_responden_ibfk_1` FOREIGN KEY (`kuis_id`) REFERENCES `kuis` (`id`),
  ADD CONSTRAINT `jawaban_responden_ibfk_2` FOREIGN KEY (`responden_id`) REFERENCES `responden` (`id`);

--
-- Constraints for table `kuis`
--
ALTER TABLE `kuis`
  ADD CONSTRAINT `kuis_ibfk_1` FOREIGN KEY (`kategori_id`) REFERENCES `kategori` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `profile`
--
ALTER TABLE `profile`
  ADD CONSTRAINT `profile_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
