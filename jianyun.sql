/*
 Navicat Premium Data Transfer

 Source Server         : try
 Source Server Type    : MySQL
 Source Server Version : 80032 (8.0.32)
 Source Host           : localhost:3306
 Source Schema         : jianyun

 Target Server Type    : MySQL
 Target Server Version : 80032 (8.0.32)
 File Encoding         : 65001

 Date: 20/02/2023 16:00:56
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Lesson
-- ----------------------------
DROP TABLE IF EXISTS `Lesson`;
CREATE TABLE `Lesson` (
  `lessonName` varchar(255) DEFAULT NULL,
  `startWeek` int DEFAULT NULL,
  `endWeek` int DEFAULT NULL,
  `lessonId` int NOT NULL AUTO_INCREMENT,
  `classroom` varchar(255) DEFAULT NULL,
  KEY `lessonId` (`lessonId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Lesson
-- ----------------------------
BEGIN;
INSERT INTO `Lesson` (`lessonName`, `startWeek`, `endWeek`, `lessonId`, `classroom`) VALUES ('形势与政策', 3, 9, 1, '1号楼1311');
COMMIT;

-- ----------------------------
-- Table structure for User
-- ----------------------------
DROP TABLE IF EXISTS `User`;
CREATE TABLE `User` (
  `userName` varchar(255) DEFAULT NULL,
  `userId` int NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `school` varchar(255) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `userType` int DEFAULT NULL,
  KEY `userId` (`userId`,`userType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of User
-- ----------------------------
BEGIN;
INSERT INTO `User` (`userName`, `userId`, `password`, `school`, `avatar`, `userType`) VALUES ('张鸿', 0, '..,as4793552', '浙江万里学院', NULL, 1);
COMMIT;

-- ----------------------------
-- Table structure for UserToLesson
-- ----------------------------
DROP TABLE IF EXISTS `UserToLesson`;
CREATE TABLE `UserToLesson` (
  `userId` int DEFAULT NULL,
  `userType` int DEFAULT NULL,
  `lessonId` int DEFAULT NULL,
  KEY `s_user` (`userId`,`userType`),
  KEY `s_lesson` (`lessonId`),
  CONSTRAINT `s_lesson` FOREIGN KEY (`lessonId`) REFERENCES `Lesson` (`lessonId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `s_user` FOREIGN KEY (`userId`, `userType`) REFERENCES `User` (`userId`, `userType`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of UserToLesson
-- ----------------------------
BEGIN;
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
