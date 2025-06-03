from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse  # Added import
from articles.models import Article

# Create your tests here.

class ArticleModelTests(TestCase):
    def test_article_creation(self):
        """
        Test that an Article instance can be created with correct attributes
        and that its string representation is its title.
        """
        # Create a User instance
        user = User.objects.create_user(
            username="testuser", password="testpassword123"
        )

        # Define article attributes
        title = "My Test Article"
        slug = "my-test-article"
        body = "This is the body of the test article."
        author = user

        # Create an Article instance
        article = Article.objects.create(
            title=title, slug=slug, body=body, author=author
        )

        # Assert that the created article's attributes match
        self.assertEqual(article.title, title)
        self.assertEqual(article.slug, slug)
        self.assertEqual(article.body, body)
        self.assertEqual(article.author, author)

        # Assert that the string representation is the title
        self.assertEqual(str(article), title)


class ArticleViewTests(TestCase):
    def test_article_list_view_status_code(self):
        """
        Test that the article list view returns a 200 status code.
        """
        response = self.client.get(reverse("articles:list"))
        self.assertEqual(response.status_code, 200)
