import uuid
from django.db import models


class IdModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class IdTimeCreatedModel(IdModel):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class IdTimeModifiedModel(IdTimeCreatedModel):
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Grade(IdTimeModifiedModel):
    grade_name = models.CharField('grade_name', max_length=255)
    unit_name = models.CharField('unit_name', max_length=255)
    grade_number = models.IntegerField('grade_number')

    class Meta:
        verbose_name = 'grade'
        verbose_name_plural = 'grades'
        db_table = 'grade'

    def __str__(self):
        return self.grade_name


class Person(IdTimeModifiedModel):
    person_name = models.CharField('person_name', max_length=255)
    grade_id = models.ForeignKey('Grade', on_delete=models.PROTECT, to_field='id', db_column='grade_id')

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'persons'
        db_table = 'person'

    def __str__(self):
        return self.person_name


class Card(IdModel):
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    person_id = models.ForeignKey('Person', on_delete=models.CASCADE, to_field='id', db_column='person_id')

    class Meta:
        verbose_name = 'card'
        verbose_name_plural = 'cards'
        db_table = 'card'

    def __str__(self):
        return f"{self.id}-{self.person_id}"


class Commitments(IdTimeModifiedModel):
    description = models.CharField('description', max_length=1023)
    active = models.BooleanField()
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE, to_field='id', db_column='card_id')

    class Meta:
        verbose_name = 'commitment'
        verbose_name_plural = 'commitments'
        db_table = 'commitments'

    def __str__(self):
        return f"{self.id}-{self.card_id}"


class Domen(IdTimeModifiedModel):
    name = models.CharField('description', max_length=255)

    class Meta:
        verbose_name = 'domen'
        verbose_name_plural = 'domens'
        db_table = 'domen'

    def __str__(self):
        return self.name


class CardDomen(IdTimeModifiedModel):
    active = models.BooleanField()
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE, to_field='id', db_column='card_id')
    domen_id = models.ForeignKey('Domen', on_delete=models.PROTECT, to_field='id', db_column='domen_id')

    class Meta:
        verbose_name = 'card_domen'
        verbose_name_plural = 'card_domens'
        db_table = 'card_domen'

    def __str__(self):
        return f"{self.card_id}-{self.domen_id}"


class CardDomenTasks(IdTimeModifiedModel):
    description = models.CharField('description', max_length=1023)
    tracker_link = models.CharField('description', max_length=1023)
    definition_of_done = models.CharField('description', max_length=1023)
    status = models.CharField('description', max_length=255)
    card_domen_id = models.ForeignKey('CardDomen', on_delete=models.CASCADE, to_field='id', db_column='card_domen_id')

    class Meta:
        verbose_name = 'card_domen_tasks'
        verbose_name_plural = 'card_domen_tasks'
        db_table = 'card_domen_tasks'

    def __str__(self):
        return self.tracker_link
