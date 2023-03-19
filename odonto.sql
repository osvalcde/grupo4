-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema odonto
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `odonto` ;

-- -----------------------------------------------------
-- Schema odonto
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `odonto` DEFAULT CHARACTER SET utf8 ;
USE `odonto` ;

-- -----------------------------------------------------
-- Table `odonto`.`doctores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `odonto`.`doctores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `ruc` VARCHAR(45) NULL DEFAULT NULL,
  `telefono` VARCHAR(45) NULL DEFAULT NULL,
  `observacion` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `odonto`.`pacientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `odonto`.`pacientes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `ci_ruc` VARCHAR(20) NULL DEFAULT NULL,
  `direccion` VARCHAR(150) NULL DEFAULT NULL,
  `nro_telefono` VARCHAR(45) NULL DEFAULT NULL,
  `fecha_nacimiento` DATE NULL DEFAULT NULL,
  `sexo` VARCHAR(10) NULL DEFAULT NULL,
  `patologia` VARCHAR(150) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
  `id_doctor` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pacientes_doctores1_idx` (`id_doctor` ASC) VISIBLE,
  CONSTRAINT `fk_pacientes_doctores1`
    FOREIGN KEY (`id_doctor`)
    REFERENCES `odonto`.`doctores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `odonto`.`consultas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `odonto`.`consultas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fecha_hora` DATETIME NULL DEFAULT NULL,
  `comentario` VARCHAR(255) NULL DEFAULT NULL,
  `pago_consulta` INT NULL DEFAULT NULL,
  `pago_tratamiento` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
  `id_paciente` INT NOT NULL,
  `id_doctor` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_consultas_pacientes_idx` (`id_paciente` ASC) VISIBLE,
  INDEX `fk_consultas_doctores1_idx` (`id_doctor` ASC) VISIBLE,
  CONSTRAINT `fk_consultas_pacientes`
    FOREIGN KEY (`id_paciente`)
    REFERENCES `odonto`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_consultas_doctores1`
    FOREIGN KEY (`id_doctor`)
    REFERENCES `odonto`.`doctores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `odonto`.`tratamientos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `odonto`.`tratamientos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `observacion` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `odonto`.`paciente_trata`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `odonto`.`paciente_trata` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `costo_total` INT NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
  `id_paciente` INT NOT NULL,
  `id_tratamiento` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_paciente_trata_pacientes1_idx` (`id_paciente` ASC) VISIBLE,
  INDEX `fk_paciente_trata_tratamiento1_idx` (`id_tratamiento` ASC) VISIBLE,
  CONSTRAINT `fk_paciente_trata_pacientes1`
    FOREIGN KEY (`id_paciente`)
    REFERENCES `odonto`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_paciente_trata_tratamiento1`
    FOREIGN KEY (`id_tratamiento`)
    REFERENCES `odonto`.`tratamientos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `odonto`.`gastos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `odonto`.`gastos` (
  `id` INT NOT NULL,
  `concepto` VARCHAR(45) NULL DEFAULT NULL,
  `monto` INT NULL DEFAULT NULL,
  `fecha` DATE NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
  `id_doctor` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_gastos_doctores1_idx` (`id_doctor` ASC) VISIBLE,
  CONSTRAINT `fk_gastos_doctores1`
    FOREIGN KEY (`id_doctor`)
    REFERENCES `odonto`.`doctores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
