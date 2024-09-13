

from unittest import TestCase

from app import app
from models import db, Blog

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blog_user_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class BlogModelTestCase(TestCase):
    """Tests for model for Pets."""

    def setUp(self):
        """Clean up any existing pets."""

        Blog.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_full_name(self):
        pet = Blog(first_name="TestBlog", last_name="blogger")
        self.assertEquals(Blog.full_name(), "TestBlog blogger")

