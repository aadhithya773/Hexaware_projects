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
EXEC sp_rename 'Artworks.Year', 'art_Year', 'COLUMN';
select aw.Title, aw.art_Year,a.nationality
from Artworks aw
join Artists a on aw.ArtistID = a.ArtistID
where a.Nationality in('spanish','dutch')
order by aw.art_Year asc;

/*3.Find the names of all artists who have artworks in the 'Painting' category, and the number of 
artworks they have in this category. */	
EXEC sp_rename 'Categories.Name', 'cat_name', 'COLUMN';
select a.artist_name , count(aw.ArtworkID)as totalARTWORKS
from Artists a
join Artworks aw on a.ArtistID=aw.ArtistID
join Categories c on aw.Category_id=c.Category_id
where c.cat_name='painting'
group by a.ArtistID,a.artist_name;

--4. List the names of artworks from the 'Modern Art Masterpieces' exhibition, along with their artists and categories. 
select aw.Title,a.artist_name,c.cat_name
from ExhibitionArtworks ea
join Exhibitions e on ea.ExhibitionID=e.ExhibitionID
join Artworks aw on ea.ArtworkId=aw.ArtworkID
join Artists a on aw.ArtistID=a.ArtistID
join Categories c on aw.Category_id=c.Category_id
where e.Title='Modern Art Masterpieces';

--5.Find the artists who have more than two artworks in the gallery.
select a.artist_name 
from Artworks aw
join Artists a on aw.ArtistID=a.ArtistID
group by a.ArtistID,a.artist_name
having count(aw.ArtistID)>2;

--6. Find the titles of artworks that were exhibited in both 'Modern Art Masterpieces' and 'Renaissance Art' exhibitions 
select aw.Title
from ExhibitionArtworks ea
join Exhibitions e on ea.ExhibitionID=e.ExhibitionID		
join Artworks aw on ea.ArtworkID=aw.ArtworkID
where e.Title in ('Modern Art Masterpieces','Renaissance Art')
group by aw.ArtworkID,aw.Title
having count(distinct e.title)=2;

--7.Find the total number of artworks in each category 
select c.cat_name,count(aw.ArtworkID)as total_count
from Artworks aw
left join Categories c on c.Category_id=aw.Category_id
group by c.Category_id,c.cat_name;

--8.List artists who have more than 3 artworks in the gallery. 
select a.artist_name , 
count(aw.ArtworkID)as total_arts
from Artists a
join Artworks aw on a.ArtistID=aw.ArtistID
group by a.ArtistID,a.artist_name
having count(aw.ArtistID)>3;

--9. Find the artworks created by artists from a specific nationality (e.g., Spanish). 
select aw.Title, a.artist_name
from Artists a
join Artworks aw on a.ArtistID=aw.ArtistID
where a.Nationality in('spanish');

--10. List exhibitions that feature artwork by both Vincent van Gogh and Leonardo da Vinci. 
select*from Exhibitions;
select*from ExhibitionArtworks;
select *from Artworks;

select e.Title
from Exhibitions e
join ExhibitionArtworks ea on e.ExhibitionID=ea.ExhibitionID
join Artworks aw on ea.ArtworkId=aw.ArtworkID
join Artists a on a.ArtistID=aw.ArtistID
where a.artist_name in ('Vincent van Gogh', 'Leonardo da Vinci')
group by e.ExhibitionID,e.Title
having count(distinct a.ArtistID)=2;

--11.Find all the artworks that have not been included in any exhibition.
select aw.ArtworkID,aw.Title
from Artworks aw
left join ExhibitionArtworks ea on aw.ArtworkID= ea.ArtworkId
where aw.ArtworkID not in(
         select ea.ArtworkId from ExhibitionArtworks);

--12.List artists who have created artworks in all available categories. 
select a.ArtistID,a.artist_name
from Artists a
join Artworks aw on a.ArtistID=aw.ArtistID
group by a.ArtistID,a.artist_name
having count(distinct aw.Category_id)=(select count(*) from Categories);

--13.List the total number of artworks in each category. 
select c.cat_name,count (aw.ArtworkId)as total_arts
from Artworks aw
left join Categories c on c.Category_id=aw.Category_id
group by c.Category_id,c.cat_name;

--14.Find the artists who have more than 2 artworks in the gallery. 
select a.artist_name , 
count(aw.ArtworkID)as total_arts
from Artists a
join Artworks aw on a.ArtistID=aw.ArtistID
group by a.ArtistID,a.artist_name
having count(aw.ArtistID)>2;

--15.List the categories with the average year of artworks they contain, only for categories with more than 1 artwork. 

select c.cat_name ,avg(aw.art_Year)as avg_year
from Categories c
join Artworks aw on c.Category_id=aw.Category_id
group by c.Category_id,c.cat_name
having count(aw.ArtworkID)>1;

--16.Find the artworks that were exhibited in the 'Modern Art Masterpieces' exhibition.
select aw.ArtworkID,aw.Title
from Artworks aw
join ExhibitionArtworks ea on aw.ArtworkID = ea.ArtworkId
join Exhibitions e on ea.ExhibitionID=e.ExhibitionID
where e.Title = 'Modern Art Masterpieces';

--17. Find the categories where the average year of artworks is greater than the average year of all artworks.
select c.cat_name as category_name,avg(aw.art_year) as AvgYear
from Categories c
join Artworks aw on c.Category_id=aw.Category_id
group by c.Category_id,c.cat_name
having avg(aw.art_year)> (select avg(art_Year) from Artworks);\

--18.List the artworks that were not exhibited in any exhibition
select aw.ArtworkID, aw.Title
from Artworks aw
left join ExhibitionArtworks ea on aw.ArtworkID = ea.ArtworkID
where ea.ArtworkID is null;

--19.Show artists who have artworks in the same category as "Mona Lisa"
select distinct a.artist_name
FROM Artists a
join Artworks aw on a.ArtistID = aw.ArtistID
where aw.Category_id = (
select Category_id
from Artworks
where Title = 'Mona Lisa');

--20. List the names of artists and the number of artworks they have in the gallery
select a.artist_name, count(aw.ArtworkID)as total_count
from Artists a 
left join Artworks aw on a.ArtistID=aw.ArtworkID
group by a.artist_name;
