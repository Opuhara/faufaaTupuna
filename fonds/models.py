# fonds/models.py

from django.db import models
from markdownx.models import MarkdownxField

from fonds.choices import LevelOfDescription


class ArchiveFonds(models.Model):
	# Section 1: Identity Statement
	title = models.CharField(max_length=255)
	reference = models.CharField(max_length=50, unique=True)
	date = models.CharField(max_length=50, help_text="e.g. 1945-1990")
	level_of_description = models.CharField(
		max_length=20,
		help_text="e.g. 1945-1990",
		choices=LevelOfDescription.choices,
		default=LevelOfDescription.FONDS
	)

	# Section 2: Context
	creator = models.CharField(max_length=255)
	administrative_history = MarkdownxField(blank=True, null=True)

	# Section 3: Content and Structure
	scope_and_content = MarkdownxField
	appraisal_destroy = MarkdownxField(blank=True, null=True)

	# Section 4: Conditions of Access and Use
	conditions_governing_access = MarkdownxField(blank=True, null=True)
	conditions_governing_reproduction = MarkdownxField(blank=True, null=True)
	language_of_material = models.CharField(max_length=100, blank=True, null=True)
	physical_characteristics = MarkdownxField(blank=True, null=True)

	# Section 5: Allied Materials
	location_of_originals = models.CharField(max_length=255, blank=True, null=True)
	related_units_of_description = MarkdownxField(blank=True, null=True)

	# Section 6: Notes
	notes = MarkdownxField(blank=True, null=True)

	# Section 7: Description Control
	archivist_name = models.CharField(max_length=255)
	date_of_description = models.DateField(auto_now_add=True)

	def __str__(self):
		return f'{self.title} ({self.reference})'
