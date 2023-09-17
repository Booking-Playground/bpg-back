from rest_framework import serializers

from api.serializers.fields import Base64ImageField
from booking.models import SettingsBooking
from playground.models import Covering, Sport, Playground, ImagePlayground
from playground.models import Inventory


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "sport_name", "sport_slug")
        model = Sport


class CoveringSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "covering_name", "covering_slug")
        model = Covering


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "inventory_name", "inventory_price")
        model = Inventory


class ImageWriteSerializer(serializers.ModelSerializer):
    image = Base64ImageField(
        required=True,
    )

    class Meta:
        fields = (
            "id",
            "image",
            "main_image",
            "description_image",
        )
        model = ImagePlayground


class PlaygroundReadSerializer(serializers.ModelSerializer):
    # owner = UserReadSerializer(
    #     many=False,
    #     read_only=True,
    # )
    images = ImageWriteSerializer(
        read_only=True,
        many=True,
        source="playground_images",
    )
    sports = SportSerializer(
        read_only=True,
        many=True,
    )
    covering = CoveringSerializer(
        read_only=True,
    )
    inventories = InventorySerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        fields = (
            "id",
            "playground_name",
            "playground_type",
            "size",
            "playground_price",
            "address",
            "owner",
            "description",
            "sports",
            "covering",
            "shower",
            "changing_rooms",
            "lighting",
            "parking",
            "stands",
            "playground_slug",
            "images",
            "draft",
            "inventories",
        )
        model = Playground


class PlaygroundWriteSerializer(serializers.ModelSerializer):
    # owner = UserReadSerializer(many=False, read_only=True)
    sports = serializers.PrimaryKeyRelatedField(
        many=True,
        required=True,
        queryset=Sport.objects.all(),
    )
    covering = serializers.PrimaryKeyRelatedField(
        many=False,
        required=True,
        queryset=Covering.objects.all(),
    )
    images = ImageWriteSerializer(
        required=False,
        many=True,
    )
    inventories = InventorySerializer(
        required=False,
        many=True,
    )

    class Meta:
        fields = (
            "id",
            "playground_name",
            "playground_type",
            "size",
            "playground_price",
            "address",
            "owner",
            "description",
            "sports",
            "covering",
            "shower",
            "changing_rooms",
            "lighting",
            "parking",
            "stands",
            "playground_slug",
            "images",
            "draft",
            "inventories",
        )
        model = Playground

    def __add_items(self, playground, data, model):
        data_list = list()
        for values in data:
            data_list.append(
                model(
                    playground=playground,
                    **values,
                )
            )
        model.objects.bulk_create(data_list)

    def create(self, validated_data):
        images = validated_data.pop("images", None)
        inventories = validated_data.pop("inventories", None)
        sports = validated_data.pop("sports", None)
        playground = Playground.objects.create(**validated_data)
        if sports:
            playground.sports.set(sports)
        if images:
            self.__add_items(playground, images, ImagePlayground)
        if inventories:
            self.__add_items(playground, inventories, Inventory)
        SettingsBooking.objects.create(playground=playground)
        playground.save()
        return playground

    def update(self, instance, validated_data):
        images = validated_data.get("images")
        inventories = validated_data.get("inventory")
        sports = validated_data.get("sports")
        if sports:
            instance.sports.set(sports)
        if images:
            ImagePlayground.objects.filter(playground=instance).delete()
            self.__add_items(instance, images, ImagePlayground)
        if inventories:
            Inventory.objects.filter(playground=instance).delete()
            self.__add_items(instance, inventories, Inventory)
        super().update(instance, validated_data)
        return instance

    def to_representation(self, instance):
        return PlaygroundReadSerializer(
            instance, context={"request": self.context.get("request")}
        ).data
