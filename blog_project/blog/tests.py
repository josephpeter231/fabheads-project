from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class PostModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='This is a test post' ,slug="test-post",author=self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'This is a test post')
        self.assertEqual(self.post.author.username, 'testuser')

    def test_slug_generation(self):
        self.assertEqual(self.post.slug, 'test-post')  

class PostDeleteTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='author1', password='password1')
        self.user2 = User.objects.create_user(username='author2', password='password2')
        self.post = Post.objects.create(title='Author1 Post', content='Content', slug='blog-post', author=self.user1)

    def test_only_author_can_delete_post(self):
        self.client.login(username='author2', password='password2')
        response = self.client.delete(f'/posts/{self.post.slug}/delete/')
        self.assertEqual(response.status_code, 302)  # Expect redirect, not forbidden

        # Verify that the post still exists
        self.assertTrue(Post.objects.filter(slug=self.post.slug).exists())

        self.client.logout()
        self.client.login(username='author1', password='password1')
        response = self.client.delete(f'/posts/{self.post.slug}/delete/')
        self.assertEqual(response.status_code, 302)  #after successfull deletion

        # To Verify that the post no longer exists
        self.assertFalse(Post.objects.filter(slug=self.post.slug).exists())
