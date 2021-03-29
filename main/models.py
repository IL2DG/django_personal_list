from django.db import models


class Workers(models.Model):
    CODDER = 'Программист'
    CLEANER = 'Уборщик'
    LOW_SPEC = 'Младший специалист'
    HIGHT_SPEC = 'Старший специалист'
    MANAGER = 'Менеджер'
    OWNER = 'Владелец'
    MID_ED = 'Среднее профессиональное'
    HIGHT_ED = 'Высшее'
    NO_ED = 'Без образования'

    POSITION_GROUP = {
        (CODDER, 'Программист'),
        (CLEANER, 'Уборщик'),
        (LOW_SPEC, 'Младший специалист'),
        (HIGHT_SPEC, 'Старший специалист'),
        (MANAGER, 'Менеджер'),
        (OWNER, 'Владелец'),
    }

    EDUCATION_GROUP = {
        (MID_ED, 'Среднее профессиональное'),
        (HIGHT_ED, 'Высшее'),
        (NO_ED, 'Без образования')
    }

    name = models.CharField('ФИО', max_length=100)
    age = models.IntegerField('Возраст')
    position = models.CharField('Должность', max_length=20, choices=POSITION_GROUP, default=CODDER)
    education = models.CharField('Образование', max_length=30, choices=EDUCATION_GROUP, default=NO_ED)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'