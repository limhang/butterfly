DROP TABLE IF EXISTS `lagou`;
CREATE TABLE `lagou` (
  `lg_id` int(11) NOT NULL AUTO_INCREMENT,
  `lg_location` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `lg_job` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `lg_count` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `lg_time` varchar(20) NOT NULL,
  `la_md5` varchar(50) NOT NULL,
  PRIMARY KEY (`lg_id`),
  UNIQUE KEY `lg_md5` (`la_md5`)
);

DROP TABLE IF EXISTS `zhaopingou`;
CREATE TABLE `zhaopingou` (
  `zh_id` int(11) NOT NULL AUTO_INCREMENT,
  `zh_location` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `zh_job` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `zh_count` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `zh_time` varchar(20) NOT NULL,
  `zhao_md5` varchar(50) NOT NULL,
  PRIMARY KEY (`zh_id`),
  UNIQUE KEY `zh_md5` (`zhao_md5`)
);