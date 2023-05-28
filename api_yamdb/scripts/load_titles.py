from api.models import Categories, Title, Genres, TitleGenres
import csv


def run():
    with open('static/data/category.csv') as file:
        reader = csv.reader(file)
        next(reader)

        Categories.objects.all().delete()

        for row in reader:
            print(row)

            category = Categories(id=row[0],
                                  name=row[1],
                                  slug=row[2],
                                  )
            category.save()

    with open('static/data/genre.csv') as file:
        reader = csv.reader(file)
        next(reader)

        Genres.objects.all().delete()

        for row in reader:
            print(row)

            genre = Genres(id=row[0],
                           name=row[1],
                           slug=row[2],)
            genre.save()

    with open('static/data/titles.csv') as file:
        reader = csv.reader(file)
        next(reader)

        Title.objects.all().delete()

        for row in reader:
            print(row)

            title = Title(id=row[0],
                          name=row[1],
                          year=row[2],)
            title.save()

    with open('static/data/genre_title.csv') as file:
        """id,title_id,genre_id"""
        reader = csv.reader(file)
        next(reader)

        TitleGenres.objects.all().delete()

        for row in reader:
            print(row)

            title_genres = TitleGenres(id=row[0],
                                       title_id=row[1],
                                       genre_id=row[2],)
            title_genres.save()