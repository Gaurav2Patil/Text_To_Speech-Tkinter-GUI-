-- Active: 1680431457239@@127.0.0.1@3306@audiodb
CREATE DATABASE audiodb;
use audiodb;
CREATE TABLE audiofiles(AF_NAme varchar(900));
insert into audiofiles (AF_NAme)values('Audio1');
select * from audiofiles;
insert into audiofiles (AF_NAme)values('audio.mp3');