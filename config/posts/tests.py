from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls): # Create user
        testuser1 = User.objects.create_user(username='testuser1', password='qwerty')
        testuser1.save()
        # Creare blog
        test_post = Post.objects.create(author='testuser1', title='testing...', body='qwerty_ytrewq')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'testing...')
        self.assertEqual(body, 'qwerty_ytrewq')