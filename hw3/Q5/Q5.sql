alter table player_bios
add column position text;

update player_bios b
set position = n.position
from new_table as n
where b.id = n.player;

select firstname, lastname, position from player_bios limit 5;