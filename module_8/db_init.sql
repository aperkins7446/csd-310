DROP USER IF EXISTS 'pysports_user'@'localhost';

CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Angel@84';

DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;

CREATE TABLE team (
	team_id		INT		NOT NULL		AUTO_INCREMENT,
	team_name	VARCHAR(75)	NOT NULL,
	mascot		VARCHAR(75)	NOT NULL,
	PRIMARY KEY(team_id)
);

CREATE TABLE player (
	player_id		INT		NOT NULL	AUTO_INCREMENT,
	first_name		VARCHAR(75)	NOT NULL,
	last_name		VARCHAR(75)	NOT NULL,
	team_id			INT		NOT NULL,
	PRIMARY KEY (player_id),
	CONSTRAINT fk_team
	FOREIGN KEY (team_id)
		REFERENCES team(team_id)
);

INSERT INTO team(team_name, mascot)
	VALUES('Alliance', 'Noble Gnomes');

INSERT INTO team(team_name, mascot)
	VALUES('Horde', 'Terrifying Taurens');

INSERT INTO player(first_name, last_name, team_id)
	VALUES('Trixie', 'Tinker', (SELECT team_id FROM team WHERE team_name = 'Alliance'));

INSERT INTO player(first_name, last_name, team_id)
	VALUES('Tommy', 'Gnoneman', (SELECT team_id FROM team WHERE team_name = 'Alliance'));

INSERT INTO player(first_name, last_name, team_id)
	VALUES('Piru', 'Buzzincup', (SELECT team_id FROM team WHERE team_name = 'Alliance'));

INSERT INTO player(first_name, last_name, team_id)
	VALUES('Vikka', 'Fulltail', (SELECT team_id FROM team WHERE team_name = 'Horde'));

INSERT INTO player(first_name, last_name, team_id)
	VALUES('Etu', 'Sharpsoar', (SELECT team_id FROM team WHERE team_name = 'Horde'));

INSERT INTO player(first_name, last_name, team_id)
	VALUES('Kitwit', 'Clawsinger', (SELECT team_id FROM team WHERE team_name = 'Horde'));
