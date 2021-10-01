alter table player_bios
add column inch_height numeric;

update player_bios
set inch_height = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer;

alter table player_bios
drop column height;

alter table player_bios
rename column inch_height to height;

select firstname, lastname, height from player_bios limit 5;