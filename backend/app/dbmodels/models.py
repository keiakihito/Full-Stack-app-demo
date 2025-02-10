# -*- coding: utf-8 -*-
"""Contains models related to stats"""
from django.db import models


# Team Model
class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


# Player Model
class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

# Game Model
class Game(models.Model):
    game_id = models.IntegerField(primary_key=True)
    home_team = models.ForeignKey(Team, related_name='home_games', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_games', on_delete=models.CASCADE)
    date = models.DateField()

# Player Stats Model
class PlayerStats(models.Model):
    player_stats_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_starter = models.BooleanField()
    minutes = models.IntegerField()
    points = models.IntegerField()
    assists = models.IntegerField()
    offensive_rebounds = models.IntegerField()
    defensive_rebounds = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    turnovers = models.IntegerField()
    defensive_fouls = models.IntegerField()
    offensive_fouls = models.IntegerField()
    free_throws_made = models.IntegerField()
    free_throws_attempted = models.IntegerField()
    two_pointers_made = models.IntegerField()
    two_pointers_attempted = models.IntegerField()
    three_pointers_made = models.IntegerField()
    three_pointers_attempted = models.IntegerField()

# Shot Model
class Shot(models.Model):
    shot_id = models.AutoField(primary_key=True)
    player_stats = models.ForeignKey(PlayerStats, on_delete=models.CASCADE)
    is_make = models.BooleanField()
    location_x = models.FloatField()
    location_y = models.FloatField()

