USE TP_TICKER;
CREATE TABLE ticker (
id_ticker INTEGER PRIMARY KEY AUTO_INCREMENT,
tipo_ticker VARCHAR (50) not null,
fecha_inicio DATETIME not null,
fecha_fin DATETIME not null );

CREATE TABLE valor_ticker (
id_valor INTEGER PRIMARY KEY AUTO_INCREMENT,
id_valor_ticker INTEGER not null,
v FLOAT not null,
vw FLOAT,
o FLOAT,
c FLOAT, 
h FLOAT,
l FLOAT,
t FLOAT,
n FLOAT,
CONSTRAINT FK_ValorTicker_Ticker FOREIGN KEY (id_valor_ticker) REFERENCES ticker(id_ticker));
