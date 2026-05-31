from django.db import models


class PlayerProgress(models.Model):
    wallet = models.CharField(max_length=42, unique=True, db_index=True)

    actor_id = models.IntegerField()
    name = models.CharField(max_length=100)

    level = models.IntegerField(default=1)
    exp = models.BigIntegerField(default=0)

    hp = models.IntegerField(default=0)
    mp = models.IntegerField(default=0)
    mhp = models.IntegerField(default=0)
    mmp = models.IntegerField(default=0)

    atk = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    mat = models.IntegerField(default=0)
    mdf = models.IntegerField(default=0)
    agi = models.IntegerField(default=0)
    luk = models.IntegerField(default=0)

    gold = models.BigIntegerField(default=0)

    map_id = models.IntegerField(default=1)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.wallet = self.wallet.lower()
        super().save(*args, **kwargs)
