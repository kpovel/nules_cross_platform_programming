insert into phone(phone_number, client_id) values ('+18009000000', 1);
insert into phone(phone_number, client_id) values ('+18009000001', 2);
insert into phone(phone_number, client_id) values ('+18009000002', 3);
insert into phone(phone_number, client_id) values ('+18009000003', 4);
insert into phone(phone_number, client_id) values ('+18009000004', 5);
insert into phone(phone_number, client_id) values ('+18009000005', 1);
insert into phone(phone_number, client_id) values ('+18009000006', 2);

insert into tariff(call_type, price_per_minute_cent) values ('внутрішній', 100);
insert into tariff(call_type, price_per_minute_cent) values ('міжміський', 150);
insert into tariff(call_type, price_per_minute_cent) values ('мобільний', 80);

insert into conversation(duration_minutes, phone_id, tariff_id) values (4, 1, 1);
insert into conversation(duration_minutes, phone_id, tariff_id) values (3, 1, 2);
insert into conversation(duration_minutes, phone_id, tariff_id) values (5, 1, 3);
insert into conversation(duration_minutes, phone_id, tariff_id) values (6, 2, 1);
insert into conversation(duration_minutes, phone_id, tariff_id) values (8, 2, 2);
insert into conversation(duration_minutes, phone_id, tariff_id) values (1, 2, 3);
insert into conversation(duration_minutes, phone_id, tariff_id) values (4, 3, 1);
insert into conversation(duration_minutes, phone_id, tariff_id) values (2, 3, 3);
insert into conversation(duration_minutes, phone_id, tariff_id) values (1, 3, 2);
insert into conversation(duration_minutes, phone_id, tariff_id) values (6, 4, 1);
insert into conversation(duration_minutes, phone_id, tariff_id) values (9, 4, 3);
insert into conversation(duration_minutes, phone_id, tariff_id) values (4, 4, 2);
insert into conversation(duration_minutes, phone_id, tariff_id) values (1, 5, 1);
insert into conversation(duration_minutes, phone_id, tariff_id) values (9, 5, 3);
insert into conversation(duration_minutes, phone_id, tariff_id) values (4, 5, 2);
insert into conversation(duration_minutes, phone_id, tariff_id) values (6, 6, 1);
insert into conversation(duration_minutes, phone_id, tariff_id) values (9, 6, 3);
insert into conversation(duration_minutes, phone_id, tariff_id) values (2, 6, 2);
insert into conversation(duration_minutes, phone_id, tariff_id) values (6, 6, 1);
insert into conversation(duration_minutes, phone_id, tariff_id) values (9, 6, 3);
