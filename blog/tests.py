from django.test import TestCase
from .models import *
from django.urls import reverse

# Create your tests here.


class TestCase(TestCase):
    def test_index_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_category_page(self):
        response = self.client.get("/category/")
        self.assertEqual(response.status_code, 200)

    def test_all_article_page(self):
        response = self.client.get("/article/all")
        self.assertEqual(response.status_code, 200)


class UserProfileTest(TestCase):
    def test_view_template(self):
        resp = self.client.get(reverse("index"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "index.html")


class ContactPageTest(TestCase):
    def test_view_template(self):
        resp = self.client.get(reverse("contact"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "page-contact.html")


class AboutUsPageTest(TestCase):
    def test_view_template(self):
        resp = self.client.get(reverse("about"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "page-about.html")


class CategoryPageTest(TestCase):
    def test_view_template(self):
        resp = self.client.get(reverse("category"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "category.html")
