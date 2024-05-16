-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 17, 2024 at 01:04 AM
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
('852d672e8871');

-- --------------------------------------------------------

--
-- Table structure for table `jawaban_responden`
--

CREATE TABLE `jawaban_responden` (
  `id` int(11) NOT NULL,
  `responden_id` int(11) NOT NULL,
  `kuis_id` int(11) NOT NULL,
  `jawaban` varchar(50) DEFAULT NULL,
  `bukti_pelaksanaan` varchar(50) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `jawaban_responden`
--

INSERT INTO `jawaban_responden` (`id`, `responden_id`, `kuis_id`, `jawaban`, `bukti_pelaksanaan`, `date_created`) VALUES
(1, 1, 7, 'salah', '', '2024-05-16 12:32:06'),
(2, 1, 8, 'Benar', 'https://www.google.com/', '2024-05-16 12:32:06'),
(3, 1, 9, 'salah', '', '2024-05-16 12:32:06'),
(4, 2, 7, 'Benar', 'https://www.google.com', '2024-05-16 18:19:16'),
(5, 2, 8, 'salah', '', '2024-05-16 18:19:16'),
(6, 2, 9, 'Benar', 'https://www.youtube.com', '2024-05-16 18:19:16'),
(7, 3, 7, 'Benar', 'https://www.google.com', '2024-05-16 18:22:20'),
(8, 3, 8, 'Benar', 'https://www.youtube.com', '2024-05-16 18:22:20'),
(9, 3, 9, 'Benar', 'https://www.youtube.com', '2024-05-16 18:22:20'),
(10, 4, 7, 'salah', '', '2024-05-17 06:54:31'),
(11, 4, 8, 'Benar', 'https://www.youtube.com', '2024-05-17 06:54:31'),
(12, 4, 9, 'salah', '', '2024-05-17 06:54:31'),
(13, 5, 7, 'salah', '', '2024-05-17 06:59:20'),
(14, 5, 8, 'Benar', 'https://www.youtube.com', '2024-05-17 06:59:20'),
(15, 5, 9, 'Benar', 'https://www.youtube.com', '2024-05-17 06:59:20');

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
(1, 'UMUM', '2024-05-16 12:25:27', '2024-05-16 12:25:27'),
(2, 'KHUSUS', '2024-05-16 12:25:31', '2024-05-16 12:25:31'),
(3, 'SPESIAL', '2024-05-16 12:25:37', '2024-05-16 12:25:37'),
(5, 'ANEH', '2024-05-16 12:25:50', '2024-05-16 12:25:50'),
(6, 'AMAZING', '2024-05-16 12:27:35', '2024-05-16 12:27:35');

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
(7, 'Pulau Terbesar di Indonesia adalah Pulau Jawa', '2024-05-16 12:30:51', 1, '2024-05-16 12:30:51'),
(8, 'Presiden Indoensia pertama adalah SBY', '2024-05-16 12:31:10', 1, '2024-05-16 12:31:10'),
(9, 'Manusia bernafas dengan paru-paru', '2024-05-16 12:31:24', 2, '2024-05-16 12:31:24');

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
  `nip` varchar(50) NOT NULL,
  `jabatan` varchar(50) NOT NULL,
  `asal_instansi` varchar(50) NOT NULL,
  `no_hp` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `responden`
--

INSERT INTO `responden` (`id`, `nama`, `nip`, `jabatan`, `asal_instansi`, `no_hp`, `email`, `date_created`) VALUES
(1, 'Budi', '1324', 'Kepala Dinas', 'Dinas Pendidikan', '234', 'budi@gmail.com', '2024-05-16 12:32:06'),
(2, 'Andi', '123', 'staf', 'Dinas Pendidikan', '1234', 'andi@gmail.com', '2024-05-16 18:19:16'),
(3, 'abc', '123', 'ad', 'df', 'sdf', 'a@gmail.com', '2024-05-16 18:22:20'),
(4, 'Hasim', '11111', 'staf', 'Dinas Perikanan', '1324', 'a@dian', '2024-05-17 06:54:31'),
(5, 'Mila', '1234', 'staf', 'Dinas Sosial', '234', 'm@gmail.com', '2024-05-17 06:59:20');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `kategori`
--
ALTER TABLE `kategori`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `kuis`
--
ALTER TABLE `kuis`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `profile`
--
ALTER TABLE `profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `responden`
--
ALTER TABLE `responden`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
