CREATE VIEW PlayerMascot AS
SELECT first_name, last_name, mascot
FROM player, team
WHERE player.team_id = team.team_id;