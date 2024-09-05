# fonds/choices.py

from django.db import models


class LevelOfDescription(models.TextChoices):
	FONDS = 'Fonds', 'Fonds'
	SERIES = 'Series', 'Series'
	FILE = 'File', 'File'
	ITEM = 'Item', 'Item'


class Language(models.TextChoices):
	ENGLISH = 'EN', 'English'
	FRENCH = 'FR', 'French'
	REO_TAHITI = 'TA', 'Tahitian'
	PAUMOTU = 'PA', 'Paumotu'


class AccessConditions(models.TextChoices):
	OPEN = 'Open', 'Open'
	RESTRICTED = 'Restricted', 'Restricted'
	CLOSED = 'Closed', 'Closed'
