create database virtualart_gallery;
go
use virtualart_gallery;
go

-- artist table
create table artist (
    artist_id int primary key identity(1,1),
    name varchar(100),
    biography text,
    birth_date date,
    nationality nvarchar(50),
    website nvarchar(100),
    contact_info nvarchar(100)
);

-- artwork table
create table artwork (
    artwork_id int primary key identity(1,1),
    title nvarchar(255),
    description text,
    creation_date date,
    medium nvarchar(100),
    image_url nvarchar(255),
    artist_id int,
    foreign key (artist_id) references artist(artist_id)
);

-- user_account table (renamed from 'user' because 'user' is a reserved keyword)
create table user_account (
    user_id int primary key identity(1,1),
    username nvarchar(50) unique,
    password nvarchar(100),
    email nvarchar(100),
    first_name nvarchar(50),
    last_name nvarchar(50),
    date_of_birth date,
    profile_picture nvarchar(255)
);

-- gallery table
create table gallery (
    gallery_id int primary key identity(1,1),
    name nvarchar(100),
    description text,
    location nvarchar(100),
    curator_id int, -- foreign key to artist
    opening_hours nvarchar(100),
    foreign key (curator_id) references artist(artist_id)
);

-- user_favorite_artwork junction table (many-to-many)
create table user_favorite_artwork (
    user_id int,
    artwork_id int,
    primary key (user_id, artwork_id),
    foreign key (user_id) references user_account(user_id),
    foreign key (artwork_id) references artwork(artwork_id)
);

-- artwork_gallery junction table (many-to-many)
create table artwork_gallery (
    artwork_id int,
    gallery_id int,
    primary key (artwork_id, gallery_id),
    foreign key (artwork_id) references artwork(artwork_id),
    foreign key (gallery_id) references gallery(gallery_id)
);

select @@ServerName;
select @port;

INSERT INTO artist (name, biography, birth_date, contact_info)
VALUES ('John Doe', 'An amazing artist', '1980-01-01', 'http://example.com/john.jpg');

SELECT * FROM artwork;
