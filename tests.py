from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_not_uniq_books_error(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        books_rating = collector.get_books_rating()
        assert len(books_rating) == 1
        assert not len(collector.get_books_rating()) == 2

    def test_add_new_book_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 5

    def test_add_new_book_no_rating_no_book(self):
        collector = BooksCollector()
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        assert len(collector.get_books_rating()) == 0

    def test_add_new_book_rating_0(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)
        assert collector.books_rating.get('Гордость и предубеждение и зомби') == 1

    def test_add_new_book_rating_over_10(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)
        assert collector.books_rating.get('Гордость и предубеждение и зомби') == 1

    def test_add_new_book_list_of_books_with_a_certain_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 2)
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 3)
        collector.add_new_book('Metro')
        collector.set_book_rating('Metro', 3)
        assert collector.get_books_with_specific_rating(3) == ['Что делать, если ваш кот хочет вас убить', 'Metro']

    def test_add_new_book_no_rating(self):
        collector = BooksCollector()
        collector.set_book_rating('Гордость и предубеждение и зомби', 1)
        assert collector.books_rating.get('Гордость и предубеждение и зомби') == None

    def test_add_new_book_add_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    def test_add_new_book_add_to_favorotes_no_doubles(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    def test_add_new_book_no_add_to_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_new_book_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 0

