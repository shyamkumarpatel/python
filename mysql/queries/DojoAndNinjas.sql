-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojos_and_ninja_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dojos_and_ninja_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojos_and_ninja_schema` DEFAULT CHARACTER SET utf8 ;
USE `dojos_and_ninja_schema` ;

-- -----------------------------------------------------
-- Table `dojos_and_ninja_schema`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_and_ninja_schema`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojos_and_ninja_schema`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_and_ninja_schema`.`ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `age` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dojo_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ninjas_dojos_idx` (`dojo_id` ASC) VISIBLE,
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `dojos_and_ninja_schema`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


/* *************************************************
Practice using MySQL workbench to run SQL commands to manipulate our database
************************************************* */

INSERT INTO dojos_and_ninja_schema.dojos (name, created_at)
VALUES ('Online', NOW());

/* ***********
Query: Create 3 new dojos
************** */
INSERT INTO dojos_and_ninja_schema.dojos (name, created_at)
VALUES ('Bellevue', NOW()), ('Los Angeles', NOW()), ('Silicon Valley', NOW());

/* ***********
Query: Delete the 3 dojos you just created
************** */
DELETE FROM dojos_and_ninja_schema.dojos WHERE id IN (2,3,4);


/* ***********
Query: Create 3 more dojos
************** */
INSERT INTO dojos_and_ninja_schema.dojos (name, created_at)
VALUES ('Bellevue', NOW()), ('Los Angeles', NOW()), ('Silicon Valley', NOW());


/* ***********
Query: Create 3 ninjas that belong to the first dojo
************** */
INSERT INTO dojos_and_ninja_schema.ninjas (first_name, last_name, age, dojo_id)
VALUES ('Alfredo','Salazar', 35, (select id from dojos_and_ninja_schema.dojos where name = 'Online'));

INSERT INTO dojos_and_ninja_schema.ninjas (first_name, last_name, age, dojo_id)
VALUES ('Winter','Perrone', 30, (select id from dojos_and_ninja_schema.dojos where name = 'Online'));

INSERT INTO dojos_and_ninja_schema.ninjas (first_name, last_name, age, dojo_id)
VALUES ('Pablo','Padilla', 30, (select id from dojos_and_ninja_schema.dojos where name = 'Online'));

/* ***********
Query: Create 3 ninjas that belong to the second dojo
************** */

INSERT INTO dojos_and_ninja_schema.ninjas (first_name, last_name, age, dojo_id)
VALUES ('Imogen','Barber', 21, (select id from dojos_and_ninja_schema.dojos where name = 'Bellevue'));

INSERT INTO dojos_and_ninja_schema.ninjas (first_name, last_name, age, dojo_id)
VALUES ('Lucinda','Salas', 25, (select id from dojos_and_ninja_schema.dojos where name = 'Bellevue'));

INSERT INTO dojos_and_ninja_schema.ninjas (first_name, last_name, age, dojo_id)
VALUES ('Camilla','Daniel', 29, (select id from dojos_and_ninja_schema.dojos where name = 'Bellevue'));


/* ***********
Query: Create 3 ninjas that belong to the third dojo
************** */

INSERT INTO dojos_and_ninja_schema.ninjas (first_name, last_name, age, dojo_id)
VALUES ('Ellise','Findlay', 34, (select id from dojos_and_ninja_schema.dojos where name = 'Los Angeles'));

INSERT INTO dojos_and_ninja_schema.ninjas (first_name, last_name, age, dojo_id)
VALUES ('Lula','Wilkerson', 46, (select id from dojos_and_ninja_schema.dojos where name = 'Los Angeles'));

INSERT INTO dojos_and_ninja_schema.ninjas (first_name, last_name, age, dojo_id)
VALUES ('Bryn','Saunders', 38, (select id from dojos_and_ninja_schema.dojos where name = 'Los Angeles'));


/* ***********
Query: Retrieve all the ninjas from the first dojo
************** */
Select n.* from dojos_and_ninja_schema.ninjas n
LEFT JOIN dojos_and_ninja_schema.dojos  d
ON n.dojo_id = d.id
where d.name = 'Online';
/* ***********
Query: Retrieve all the ninjas from the last dojo
************** */
Select n.* from dojos_and_ninja_schema.ninjas n
LEFT JOIN dojos_and_ninja_schema.dojos  d
ON n.dojo_id = d.id
where d.name = 'Los Angeles';

/* ***********
Query: Retrieve the last ninja's dojo
************** */
Select * from dojos_and_ninja_schema.ninjas
where id = (Select max(id) AS id from dojos_and_ninja_schema.ninjas);