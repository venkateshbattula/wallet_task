from rest_framework import serializers
from .models import users, userWallet


class usersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = users
        fields = ('user_email', 'password')


class userWalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = userWallet
        fields = ('wallet_id', 'user_email', 'wallet_status')

