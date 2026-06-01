import graphene
from django.conf import settings
from api.models import PlayerProgress


class PlayerProgressType(graphene.ObjectType):
    id = graphene.ID()
    wallet = graphene.String()
    actor_id = graphene.Int()
    name = graphene.String()
    level = graphene.Int()
    exp = graphene.Int()
    hp = graphene.Int()
    mp = graphene.Int()
    mhp = graphene.Int()
    mmp = graphene.Int()
    atk = graphene.Int()
    defense = graphene.Int()
    mat = graphene.Int()
    mdf = graphene.Int()
    agi = graphene.Int()
    luk = graphene.Int()
    gold = graphene.Int()
    map_id = graphene.Int()
    x = graphene.Int()
    y = graphene.Int()



class Query(graphene.ObjectType):
    version = graphene.String()

    def resolve_version(self, info, **kwargs):
        return settings.VERSION

    player_progress = graphene.Field(
        PlayerProgressType,
        wallet=graphene.String(required=True)
    )

    def resolve_player_progress(self, info, **kwargs):
        return PlayerProgress.objects.get(**kwargs)


class SavePlayerProgress(graphene.relay.ClientIDMutation):
    ok = graphene.Boolean()
    player_progress = graphene.Field(PlayerProgressType)

    class Input:
        wallet = graphene.String(required=True)
        actor_id = graphene.Int(required=True)
        name = graphene.String(required=True)
        level = graphene.Int(required=True)
        exp = graphene.Int(required=True)
        hp = graphene.Int(required=True)
        mp = graphene.Int(required=True)
        mhp = graphene.Int(required=True)
        mmp = graphene.Int(required=True)
        atk = graphene.Int(required=True)
        defense = graphene.Int(required=True)
        mat = graphene.Int(required=True)
        mdf = graphene.Int(required=True)
        agi = graphene.Int(required=True)
        luk = graphene.Int(required=True)
        gold = graphene.Int(required=True)
        map_id = graphene.Int(required=True)
        x = graphene.Int(required=True)
        y = graphene.Int(required=True)


    def mutate_and_get_payload(self, info, **kwargs):
        wallet = kwargs.pop("wallet").lower()

        player_progress = PlayerProgress.objects.update_or_create(
            wallet=wallet,
            defaults=kwargs
        )

        return SavePlayerProgress(player_progress=player_progress, ok=True)


class Mutation:
    save_player_progress = SavePlayerProgress.Field()
