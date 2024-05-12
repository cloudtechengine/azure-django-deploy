from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from blog.models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a User instance
        test_user = User.objects.create_user(username='testuser', password='12345')

        # Create a Post instance
        Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=test_user
        )

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_content = f'{post.content}'
        self.assertEqual(expected_title, 'Test Post')
        self.assertEqual(expected_content, 'This is a test post content.')

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        expected_url = reverse('post_detail', kwargs={'pk': post.pk})
        self.assertEqual(post.get_absolute_url(), expected_url)
from django.test import TestCase

# Create your tests here.
