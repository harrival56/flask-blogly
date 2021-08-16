from unittest import TestCase
from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE-URI'] ='postgresql://:5433/blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class userModelTestCase(TestCase):
    """test for model for users"""

    def setUp(self):
        """clean up any existing users"""

        User.query.delete()

    def tearDown(self):
        """clean up any after every test"""
        db.session.rollback()

    def test_greet(self):
        user = User(first_name="Jude", last_name="okwu",image_url="https://d3j2s6hdd6a7rg.cloudfront.net/v2/uploads/media/default/0002/15/thumb_114242_default_news_size_5.jpeg")
        self.assertEqual(user.greet(), "Hi, welcome to my profile page, I'm Jude okwu")

    