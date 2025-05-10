from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class UserAPITestCase(APITestCase):
    def test_create_user(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123"
        }
        response = self.client.post("/api/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamAPITestCase(APITestCase):
    def test_create_team(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        data = {
            "name": "Test Team",
            "members": [str(user._id)]
        }
        response = self.client.post("/api/teams/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityAPITestCase(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        data = {
            "user": str(user._id),
            "activity_type": "Running",
            "duration": "00:30:00"
        }
        response = self.client.post("/api/activities/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardAPITestCase(APITestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        data = {
            "user": str(user._id),
            "score": 100,
            "rank": 1
        }
        response = self.client.post("/api/leaderboard/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutAPITestCase(APITestCase):
    def test_create_workout(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        data = {
            "name": "Morning Yoga",
            "description": "A relaxing yoga session to start the day.",
            "duration": "00:45:00",
            "difficulty": "Easy",
            "created_by": str(user._id)
        }
        response = self.client.post("/api/workouts/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
