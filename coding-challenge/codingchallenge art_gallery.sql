create database art_gallery;
go
use art_gallery;
go

create table Artists ( 
ArtistID int identity(1,1) primary key,
artist_name varchar(255) not null, 
Biography text, 
Nationality varchar(100)); 

create table Categories ( 
Category_id int primary key , 
Name varchar(100) not null );

create table Artworks ( 
ArtworkID int primary key, 
Title varchar(255) not null, 
ArtistID int, 
Category_id int, 
art_Year int, 
art_Description text, 
ImageURL varchar(255), 
foreign key (ArtistID) references Artists (ArtistID), 
foreign key (Category_id) references Categories (Category_id));

create table Exhibitions ( 
ExhibitionID int primary key, 
Title varchar(255) not null, 
StartDate date, 
EndDate date, 
Desscription text); 

-- Create a table to associate artworks with exhibitions
create table ExhibitionArtworks(
ExhibitionID int,
ArtworkId int,
primary key(ExhibitionID,ArtworkId),
foreign key(exhibitionID) references Exhibitions(ExhibitionID),
foreign key(ArtworkId) references Artworks (ArtworkID)); 

insert into Artists (artist_name, Biography, Nationality) values
( 'Pablo Picasso', 'Renowned Spanish painter and sculptor.', 'Spanish'), 
( 'Vincent van Gogh', 'Dutch post-impressionist painter.', 'Dutch'), 
( 'Leonardo da Vinci', 'Italian polymath of the Renaissance.', 'Italian');

 insert into Categories(Category_id, Name) values
(1, 'Painting'), 
(2, 'Sculpture'), 
(3, 'Photography');

insert into Artworks (ArtworkID, Title, ArtistID, Category_id, art_Year, art_Description, ImageURL) values
(1, 'Starry Night', 2, 1, 1889, 'A famous painting by Vincent van Gogh.', 'starry_night.jpg'), 
(2, 'Mona Lisa', 3, 1, 1503, 'The iconic portrait by Leonardo da Vinci.', 'mona_lisa.jpg'), 
(3, 'Guernica', 1, 1, 1937, 'Pablo Picasso\s powerful anti-war mural.', 'guernica.jpg'); 

insert into Exhibitions (ExhibitionID, Title, StartDate, EndDate, Desscription) values
(1, 'Modern Art Masterpieces', '2023-01-01', '2023-03-01', 'A collection of modern art masterpieces.'), 
(2, 'Renaissance Art', '2023-04-01', '2023-06-01', 'A showcase of Renaissance art treasures.');

insert into ExhibitionArtworks (ExhibitionID, ArtworkId	) values 
(1, 1), 
(1, 2), 
(1, 3), 
(2, 2); 

-------solving queries----------------------------
--1. retrieve name of all artist with count of their paintings
select a.artist_name, count(aw.artworkId)as total_arts
from Artists a
join Artworks aw on a.ArtistID =aw.ArtistID
group by a.ArtistID,a.artist_name
order by total_arts desc;

--2.List the title of artworks
select aw.Title, aw.art_Year,a.nationality
from Artworks aw
join Artists a on aw.ArtistID = a.ArtistID
where a.Nationality in('spanish','dutch')
order by aw.art_Year asc;
