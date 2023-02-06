from django.db import models
from common.models import CommonModel

# DONE: project_room table
class Room(commonModel):
    """Project_Room Model Definition"""

    class ActiveTimeChoices(models.IntegerChoices):
        ALL_TIME  = 0
        MORNING = 9
        AFTERNOON = 12
        EVENING = 18

    name = models.CharField(
        max_length=180,
        default="",
    )
    introduce = models.TextField()
    recruitment_period = models.DateTimeField(
        null=True, blank=True,
    )
    active_time = models.IntegerChoices(
        choices=ActiveTimeChoices.choices,
    )
    main_file_key = models.CharField(
        max_length=256,
        null=True, blank=True,
    )  # project_image
    founder_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )