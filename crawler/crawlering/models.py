from django.db import models


class Companies(models.Model):
    CompanyRank = models.CharField(max_length=255)
    CompanyName = models.CharField(max_length=500)
    Industry = models.CharField(max_length=500)
    Country = models.CharField(max_length=500)
    Score = models.CharField(max_length=255)

    def __str__(self):
        return self.CompanyRank


class EsgScore(models.Model):
    Name = models.CharField(max_length=500)
    Score = models.CharField(max_length=500)
    Rank = models.CharField(max_length=500)
    Environment = models.CharField(max_length=500)
    Social = models.CharField(max_length=500)
    Governance = models.CharField(max_length=500)

    def __str__(self):
        return self.Score
