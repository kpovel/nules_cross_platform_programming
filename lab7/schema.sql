-- Клієнти[Код клієнта, Тип клієнта(відомство, фізична особа), Адреса, Прізвище, Ім’я, По батькові],
-- Телефони[номер телефону абонента, Код клієнта]
-- Розмови[Код розмови, дата розмови, номер телефону, кількість хвилин розмови, код тарифу]
-- Тарифи[Код тарифу, тип дзвінка, вартість 1 хвилини розмови].

create type client_type as enum ('agency', 'individual');

create table client (
    id          serial primary key,
    type        client_type  not null,
    address     varchar(255) not null,
    first_name  varchar(255) not null,
    last_name   varchar(255) not null,
    middle_name varchar(255) not null
);

create table phone (
    id           serial primary key,
    phone_number varchar(15) not null,
    client_id    integer references client (id)
);

create table tariff (
    id                    serial primary key,
    call_type             varchar(255) not null,
    price_per_minute_cent integer      not null
);

create table conversation (
    id               serial primary key,
    duration_minutes integer not null,
    phone_id         integer references phone (id),
    tariff_id        integer references tariff (id)
);
