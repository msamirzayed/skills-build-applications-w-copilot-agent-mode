from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create Users
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

        # Create additional Users
        user3 = User.objects.create(username='alice_smith', email='alice@example.com', password='password123')
        user4 = User.objects.create(username='bob_brown', email='bob@example.com', password='password123')

        # Create Teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Create additional Teams
        team2 = Team.objects.create(name='Team Beta')
        team2.members.add(user3, user4)

        # Create Activities
        Activity.objects.create(user=user1, activity_type='Running', duration=timedelta(minutes=30))
        Activity.objects.create(user=user2, activity_type='Cycling', duration=timedelta(hours=1))

        # Add more Activities
        Activity.objects.create(user=user3, activity_type='Swimming', duration=timedelta(minutes=45))
        Activity.objects.create(user=user4, activity_type='Hiking', duration=timedelta(hours=2))

        # Create Leaderboard Entries
        Leaderboard.objects.create(user=user1, score=150, rank=1)
        Leaderboard.objects.create(user=user2, score=120, rank=2)

        # Add more Leaderboard Entries
        Leaderboard.objects.create(user=user3, score=200, rank=1)
        Leaderboard.objects.create(user=user4, score=180, rank=2)

        # Create Workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session.', duration=timedelta(minutes=45), difficulty='Easy', created_by=user1)
        Workout.objects.create(name='HIIT Training', description='High-intensity interval training.', duration=timedelta(minutes=30), difficulty='Hard', created_by=user2)

        # Add more Workouts
        Workout.objects.create(name='Evening Pilates', description='A calming pilates session.', duration=timedelta(minutes=60), difficulty='Medium', created_by=user3)
        Workout.objects.create(name='Strength Training', description='Weightlifting and resistance exercises.', duration=timedelta(minutes=90), difficulty='Hard', created_by=user4)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
