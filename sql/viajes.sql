BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "viajes" (
	"id"	INTEGER,
	"nombre"	TEXT,
	"fecha_inicio"	TEXT,
	"fecha_fin"	TEXT,
	"min_participantes"	INTEGER,
	"max_participantes"	INTEGER,
	"destino_id"	INTEGER,
	PRIMARY KEY("id")
);
INSERT INTO "viajes" VALUES (1,'Baldour´s Calilewa
','15/04/2024','20/04/2024',5,10,NULL);
INSERT INTO "viajes" VALUES (2,'Saint Lucas','25/04/2024','30/04/2024',3,8,NULL);
INSERT INTO "viajes" VALUES (3,'Paiconen','12/04/2024','16/04/2024',3,6,NULL);
COMMIT;
