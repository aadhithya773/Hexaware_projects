import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.artist_dao import ArtistDAO
from dao.artwork_dao import ArtworkDAO
from dao.user_account_dao import UserAccountDAO
from dao.gallery_dao import GalleryDAO
from dao.user_favorite_dao import UserFavoriteArtworkDAO
from dao.artwork_gallery_dao import ArtworkGalleryDAO
from exception.custom_exceptions import ArtworkNotFoundException,UserNotFoundException
def main_menu():
    while True:
        print("\n Welcome to Virtual Art Gallery System")
        print("-------------------------------------")
        print("1. Artist Management")
        print("2. Artwork Management")
        print("3. User Management")
        print("4. Gallery Management")
        print("5. Manage User Favorite Artworks")
        print("6. Manage Artwork-Gallery Linking")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            artist_management()
        elif choice == '2':
            artwork_management()
        elif choice == '3':
            user_management()
        elif choice == '4':
            gallery_management()
        elif choice == '5':
            favorite_management()
        elif choice == '6':
            artwork_gallery_management()
        elif choice == '7':
            print("Thank you for using Virtual Art Gallery System!")
            break
        else:
            print("Invalid choice. Please try again.")

# ----------------------------------------------
# Placeholder Functions 
# ----------------------------------------------

def artist_management():
    artist_dao = ArtistDAO()

    while True:
        print("\n--- Artist Management ---")
        print("1. Add Artist")
        print("2. Update Artist")
        print("3. Delete Artist")
        print("4. View All Artists")
        print("5. View Artist by ID")
        print("6. Go Back")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            try:
                name = input("Enter artist name: ")
                biography = input("Enter biography: ")
                birth_date = input("Enter birth date (YYYY-MM-DD): ")
                nationality = input("Enter nationality: ")
                website = input("Enter website URL: ")
                contact_info = input("Enter contact info: ")

                from entity.artist import Artist
                new_artist = Artist(name=name, biography=biography, birth_date=birth_date,
                                    nationality=nationality, website=website, contact_info=contact_info)
                success = artist_dao.addArtist(new_artist)
                if success:
                    print("Artist added successfully!")
                else:
                    print("Failed to add artist.")
            except Exception as e:
                print("Error:", e)

        elif choice == '2':
            try:
                artist_id = int(input("Enter artist ID to update: "))
                name = input("Enter updated artist name: ")
                biography = input("Enter updated biography: ")
                birth_date = input("Enter updated birth date (YYYY-MM-DD): ")
                nationality = input("Enter updated nationality: ")
                website = input("Enter updated website URL: ")
                contact_info = input("Enter updated contact info: ")

                from entity.artist import Artist
                updated_artist = Artist(name=name, biography=biography, birth_date=birth_date,
                                        nationality=nationality, website=website, contact_info=contact_info)
                updated_artist.set_artist_id(artist_id)

                success = artist_dao.updateArtist(updated_artist)
                if success:
                    print("artist updated successfully!")
                else:
                    print("Failed to update artist.")
            except Exception as e:
                print("Error:", e)

        elif choice == '3':
            try:
                artist_id = int(input("Enter artist ID to delete: "))
                success = artist_dao.deleteArtist(artist_id)
                if success:
                    print("artist deleted successfully!")
                else:
                    print("Failed to delete artist.")
            except Exception as e:
                print("Error:", e)

        elif choice == '4':
            try:
                artists = artist_dao.getAllArtists()
                for artist in artists:
                    print(f"ID: {artist.get_()}, Name: {artist.get_name()}, Nationality: {artist.get_nationality()}")
            except Exception as e:
                print("Error:", e)

        elif choice == '5':
            try:
                artist_id = int(input("Enter artist ID to view: "))
                artist = artist_dao.getArtistById(artist_id)
                if artist:
                    print(f"ID: {artist.get_artist_id()}")
                    print(f"Name: {artist.get_name()}")
                    print(f"Biography: {artist.get_biography()}")
                    print(f"Birth Date: {artist.get_birth_date()}")
                    print(f"Nationality: {artist.get_nationality()}")
                    print(f"Website: {artist.get_website()}")
                    print(f"Contact Info: {artist.get_contact_info()}")
                else:
                    print("Artist not found.")
            except Exception as e:
                print("Error:", e)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")


def artwork_management():
    artwork_dao = ArtworkDAO()

    while True:
        print("\n--- Artwork Management ---")
        print("1. Add Artwork")
        print("2. Update Artwork")
        print("3. Delete Artwork")
        print("4. View All Artworks")
        print("5. View Artwork by ID")
        print("6. Go Back")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            try:
                title = input("Enter artwork title: ")
                description = input("Enter description: ")
                creation_date = input("Enter creation date (YYYY-MM-DD): ")
                medium = input("Enter medium: ")
                image_url = input("Enter image URL: ")
                artist_id = int(input("Enter artist ID: "))

                from entity.artwork import Artwork
                new_artwork = Artwork(title=title, description=description, creation_date=creation_date,
                                      medium=medium, image_url=image_url, artist_id=artist_id)
                success = artwork_dao.addArtwork(new_artwork)
                if success:
                    print("Artwork added successfully!")
                else:
                    print("Failed to add artwork.")
            except Exception as e:
                print("Error:", e)

        elif choice == '2':
            try:
                artwork_id = int(input("Enter artwork ID to update: "))
                title = input("Enter updated title: ")
                description = input("Enter updated description: ")
                creation_date = input("Enter updated creation date (YYYY-MM-DD): ")
                medium = input("Enter updated medium: ")
                image_url = input("Enter updated image URL: ")
                artist_id = int(input("Enter updated artist ID: "))

                from entity.artwork import Artwork
                updated_artwork = Artwork(title=title, description=description, creation_date=creation_date,
                                          medium=medium, image_url=image_url, artist_id=artist_id)
                updated_artwork.set_artwork_id(artwork_id)

                success = artwork_dao.updateArtwork(updated_artwork)
                if success:
                    print("Artwork updated successfully!")
                else:
                    print("Failed to update artwork.")
            except Exception as e:
                print("Error:", e)

        elif choice == '3':
            try:
                artwork_id = int(input("Enter artwork ID to delete: "))
                success = artwork_dao.deleteArtwork(artwork_id)
                if success:
                    print("Artwork deleted successfully!")
                else:
                    print("Failed to delete artwork.")
            except Exception as e:
                print("Error:", e)

        elif choice == '4':
            try:
                artworks = artwork_dao.getAllArtworks()
                for artwork in artworks:
                    print(f"ID: {artwork.get_artwork_id()}, Title: {artwork.get_title()}, Artist ID: {artwork.get_artist_id()}")
            except Exception as e:
                print("Error:", e)

        elif choice == '5':
            try:
                artwork_id = int(input("Enter artwork ID to view: "))
                artwork = artwork_dao.getArtworkById(artwork_id)
                if artwork:
                    print(f"ID: {artwork.get_artwork_id()}")
                    print(f"Title: {artwork.get_title()}")
                    print(f"Description: {artwork.get_description()}")
                    print(f"Creation Date: {artwork.get_creation_date()}")
                    print(f"Medium: {artwork.get_medium()}")
                    print(f"Image URL: {artwork.get_image_url()}")
                    print(f"Artist ID: {artwork.get_artist_id()}")
                else:
                    print("Artwork not found.")
            except ArtworkNotFoundException as e:
                print("Error:", e)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")


def user_management():
    user_dao = UserAccountDAO()

    while True:
        print("\n--- User Account Management ---")
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. View All Users")
        print("5. View User by ID")
        print("6. Go Back")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            try:
                username = input("Enter username: ")
                password = input("Enter password: ")
                email = input("Enter email: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                profile_picture = input("Enter profile picture URL: ")

                from entity.user import UserAccount
                new_user = UserAccount(username=username, password=password, email=email,
                                       first_name=first_name, last_name=last_name,
                                       date_of_birth=date_of_birth, profile_picture=profile_picture)
                success = user_dao.addUser(new_user)
                if success:
                    print("User added successfully!")
                else:
                    print("Failed to add user.")
            except Exception as e:
                print("Error:", e)

        elif choice == '2':
            try:
                user_id = int(input("Enter user ID to update: "))
                username = input("Enter updated username: ")
                password = input("Enter updated password: ")
                email = input("Enter updated email: ")
                first_name = input("Enter updated first name: ")
                last_name = input("Enter updated last name: ")
                date_of_birth = input("Enter updated date of birth (YYYY-MM-DD): ")
                profile_picture = input("Enter updated profile picture URL: ")

                from entity.user import UserAccount
                updated_user = UserAccount(username=username, password=password, email=email,
                                           first_name=first_name, last_name=last_name,
                                           date_of_birth=date_of_birth, profile_picture=profile_picture)
                updated_user.set_user_id(user_id)

                success = UserAccountDAO.updateUser(updated_user)
                if success:
                    print("User updated successfully!")
                else:
                    print("Failed to update user.")
            except Exception as e:
                print("Error:", e)

        elif choice == '3':
            try:
                user_id = int(input("Enter user ID to delete: "))
                success = UserAccountDAO(user_id)
                if success:
                    print("User deleted successfully!")
                else:
                    print("Failed to delete user.")
            except Exception as e:
                print("Error:", e)

        elif choice == '4':
            try:
                users = UserAccountDAO.getAllUsers()
                for user in users:
                    print(f"ID: {user.get_user_id()}, Username: {user.get_username()}, Email: {user.get_email()}")
            except Exception as e:
                print("Error:", e)

        elif choice == '5':
            try:
                user_id = int(input("Enter user ID to view: "))
                user = UserAccountDAO.getUserById(user_id)
                if user:
                    print(f"ID: {user.get_user_id()}")
                    print(f"Username: {user.get_username()}")
                    print(f"Email: {user.get_email()}")
                    print(f"First Name: {user.get_first_name()}")
                    print(f"Last Name: {user.get_last_name()}")
                    print(f"Date of Birth: {user.get_date_of_birth()}")
                    print(f"Profile Picture: {user.get_profile_picture()}")
                else:
                    print("User not found.")
            except UserNotFoundException as e:
                print("Error:", e)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")


def gallery_management():
    gallery_dao = GalleryDAO()

    while True:
        print("\n--- Gallery Management ---")
        print("1. Add Gallery")
        print("2. Update Gallery")
        print("3. Delete Gallery")
        print("4. View All Galleries")
        print("5. View Gallery by ID")
        print("6. Go Back")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            try:
                name = input("Enter gallery name: ")
                description = input("Enter gallery description: ")
                location = input("Enter gallery location: ")
                curator_id = int(input("Enter curator (artist) ID: "))
                opening_hours = input("Enter opening hours: ")

                from entity.gallery import Gallery
                new_gallery = Gallery(name=name, description=description, location=location,
                                      curator_id=curator_id, opening_hours=opening_hours)

                success = gallery_dao.addGallery(new_gallery)
                if success:
                    print("Gallery added successfully!")
                else:
                    print("Failed to add gallery.")
            except Exception as e:
                print("Error:", e)

        elif choice == '2':
            try:
                gallery_id = int(input("Enter gallery ID to update: "))
                name = input("Enter updated gallery name: ")
                description = input("Enter updated description: ")
                location = input("Enter updated location: ")
                curator_id = int(input("Enter updated curator (artist) ID: "))
                opening_hours = input("Enter updated opening hours: ")

                from entity.gallery import Gallery
                updated_gallery = Gallery(name=name, description=description, location=location,
                                          curator_id=curator_id, opening_hours=opening_hours)
                updated_gallery.set_gallery_id(gallery_id)

                success = gallery_dao.updateGallery(updated_gallery)
                if success:
                    print("Gallery updated successfully!")
                else:
                    print("Failed to update gallery.")
            except Exception as e:
                print("Error:", e)

        elif choice == '3':
            try:
                gallery_id = int(input("Enter gallery ID to delete: "))
                success = gallery_dao.deleteGallery(gallery_id)
                if success:
                    print("Gallery deleted successfully!")
                else:
                    print("Failed to delete gallery.")
            except Exception as e:
                print("Error:", e)

        elif choice == '4':
            try:
                galleries = gallery_dao.getAllGalleries()
                for gallery in galleries:
                    print(f"ID: {gallery.get_gallery_id()}, Name: {gallery.get_name()}, Location: {gallery.get_location()}")
            except Exception as e:
                print("Error:", e)

        elif choice == '5':
            try:
                gallery_id = int(input("Enter gallery ID to view: "))
                gallery = gallery_dao.getGalleryById(gallery_id)
                if gallery:
                    print(f"ID: {gallery.get_gallery_id()}")
                    print(f"Name: {gallery.get_name()}")
                    print(f"Description: {gallery.get_description()}")
                    print(f"Location: {gallery.get_location()}")
                    print(f"Curator ID: {gallery.get_curator_id()}")
                    print(f"Opening Hours: {gallery.get_opening_hours()}")
                else:
                    print("Gallery not found.")
            except Exception as e:
                print("Error:", e)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")


def favorite_management():
    favorite_dao = UserFavoriteArtworkDAO()

    while True:
        print("\n--- User Favorite Artwork Management ---")
        print("1. Add Favorite Artwork")
        print("2. Remove Favorite Artwork")
        print("3. View All Favorite Artworks by User")
        print("4. Go Back")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                user_id = int(input("Enter user ID: "))
                artwork_id = int(input("Enter artwork ID to add as favorite: "))

                success = favorite_dao.addFavorite(user_id, artwork_id)
                if success:
                    print("Favorite artwork added successfully!")
                else:
                    print("Failed to add favorite artwork.")
            except Exception as e:
                print("Error:", e)

        elif choice == '2':
            try:
                user_id = int(input("Enter user ID: "))
                artwork_id = int(input("Enter artwork ID to remove from favorites: "))

                success = favorite_dao.removeFavorite(user_id, artwork_id)
                if success:
                    print("Favorite artwork removed successfully!")
                else:
                    print("Failed to remove favorite artwork.")
            except Exception as e:
                print("Error:", e)

        elif choice == '3':
            try:
                user_id = int(input("Enter user ID to view favorite artworks: "))
                favorites = favorite_dao.getFavoritesByUser(user_id)

                if favorites:
                    print(f"Favorite artworks for user {user_id}:")
                    for fav in favorites:
                        print(f"Artwork ID: {fav.get_artwork_id()}, Title: {fav.get_title()}")
                else:
                    print("No favorite artworks found for this user.")
            except Exception as e:
                print("Error:", e)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")


def artwork_gallery_management():
    artwork_gallery_dao = ArtworkGalleryDAO()

    while True:
        print("\n--- Artwork-Gallery Linking Management ---")
        print("1. Link Artwork to Gallery")
        print("2. Unlink Artwork from Gallery")
        print("3. View All Galleries for an Artwork")
        print("4. View All Artworks in a Gallery")
        print("5. Go Back")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                artwork_id = int(input("Enter artwork ID: "))
                gallery_id = int(input("Enter gallery ID to link: "))

                success = artwork_gallery_dao.addArtworkToGallery(artwork_id, gallery_id)
                if success:
                    print("Artwork linked to gallery successfully!")
                else:
                    print("Failed to link artwork to gallery.")
            except Exception as e:
                print("Error:", e)

        elif choice == '2':
            try:
                artwork_id = int(input("Enter artwork ID: "))
                gallery_id = int(input("Enter gallery ID to unlink: "))

                success = artwork_gallery_dao.removeArtworkFromGallery(artwork_id, gallery_id)
                if success:
                    print("Artwork unlinked from gallery successfully!")
                else:
                    print("Failed to unlink artwork from gallery.")
            except Exception as e:
                print("Error:", e)

        elif choice == '3':
            try:
                artwork_id = int(input("Enter artwork ID to view linked galleries: "))
                galleries = artwork_gallery_dao.getGalleriesForArtwork(artwork_id)

                if galleries:
                    print(f"Galleries linked with artwork {artwork_id}:")
                    for gallery in galleries:
                        print(f"Gallery ID: {gallery.get_gallery_id()}, Name: {gallery.get_name()}")
                else:
                    print("No galleries linked with this artwork.")
            except Exception as e:
                print("Error:", e)

        elif choice == '4':
            try:
                gallery_id = int(input("Enter gallery ID to view artworks: "))
                artworks = artwork_gallery_dao.getArtworksByGallery(gallery_id)

                if artworks:
                    print(f"Artworks in gallery {gallery_id}:")
                    for artwork in artworks:
                        print(f"Artwork ID: {artwork.get_artwork_id()}, Title: {artwork.get_title()}")
                else:
                    print("No artworks found in this gallery.")
            except Exception as e:
                print("Error:", e)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")


# ----------------------------------------------
# Start the program
# ----------------------------------------------

if __name__ == "__main__":
    main_menu()
