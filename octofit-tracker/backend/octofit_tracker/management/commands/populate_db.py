from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], int(settings.DATABASES['default']['PORT']))
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {'username': 'thundergod', 'email': 'thundergod@mhigh.edu', 'password': 'thundergodpassword'},
            {'username': 'metalgeek', 'email': 'metalgeek@mhigh.edu', 'password': 'metalgeekpassword'},
            {'username': 'zerocool', 'email': 'zerocool@mhigh.edu', 'password': 'zerocoolpassword'},
            {'username': 'crashoverride', 'email': 'crashoverride@mhigh.edu', 'password': 'crashoverridepassword'},
            {'username': 'sleeptoken', 'email': 'sleeptoken@mhigh.edu', 'password': 'sleeptokenpassword'},
        ]
        db.users.insert_many(users)

        # Create teams
        teams = [
            {'name': 'Blue Team', 'members': [user['username'] for user in users[:3]]},
            {'name': 'Gold Team', 'members': [user['username'] for user in users[3:]]},
        ]
        db.teams.insert_many(teams)

        # Create activities
        activities = [
            {'user': users[0]['username'], 'activity_type': 'Cycling', 'duration': 60, 'date': '2025-04-18'},
            {'user': users[1]['username'], 'activity_type': 'Crossfit', 'duration': 120, 'date': '2025-04-18'},
            {'user': users[2]['username'], 'activity_type': 'Running', 'duration': 90, 'date': '2025-04-18'},
            {'user': users[3]['username'], 'activity_type': 'Strength', 'duration': 30, 'date': '2025-04-18'},
            {'user': users[4]['username'], 'activity_type': 'Swimming', 'duration': 75, 'date': '2025-04-18'},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard entries
        leaderboard = [
            {'team': teams[0]['name'], 'points': 100},
            {'team': teams[1]['name'], 'points': 90},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts
        workouts = [
            {'name': 'Cycling Training', 'description': 'Training for a road cycling event', 'duration': 60},
            {'name': 'Crossfit', 'description': 'Training for a crossfit competition', 'duration': 120},
            {'name': 'Running Training', 'description': 'Training for a marathon', 'duration': 90},
            {'name': 'Strength Training', 'description': 'Training for strength', 'duration': 30},
            {'name': 'Swimming Training', 'description': 'Training for a swimming competition', 'duration': 75},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))