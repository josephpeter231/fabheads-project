from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_post_creation_and_slug_generation(self):
        post = Post.objects.create(title='My First Post', content='This is a test post', author=self.user)
        self.assertEqual(post.title, 'My First Post')
        self.assertEqual(post.slug, 'my-first-post')  # Assuming your model auto-generates the slug
        self.assertEqual(post.author, self.user)

class PostDeletePermissionTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='author1', password='password123')
        self.user2 = User.objects.create_user(username='author2', password='password456')
        self.post = Post.objects.create(title='Post by author1', content='Content by author1', author=self.user1)

    def test_author_can_delete_own_post(self):
        self.client.login(username='author1', password='password123')
        response = self.client.post(f'/posts/{self.post.slug}/delete/')
        self.assertEqual(response.status_code, 302)  # Assuming redirection after successful deletion
        self.assertFalse(Post.objects.filter(slug=self.post.slug).exists())

    def test_non_author_cannot_delete_post(self):
        self.client.login(username='author2', password='password456')
        response = self.client.post(f'/posts/{self.post.slug}/delete/')
        self.assertEqual(response.status_code, 403)  # Assuming you return a 403 Forbidden status
        self.assertTrue(Post.objects.filter(slug=self.post.slug).exists())
