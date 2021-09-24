Drop table rdata;

create table rdata(
id serial primary key,
a text unique not null check(char_length(a)<=5),
b text unique not null check(char_length(b)<=5),
moment date default  ('2020-01-01'),
x decimal(5,2) check(x>0)
);

