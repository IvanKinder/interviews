from django.db import models, router
from django.db.models.deletion import Collector
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=16, verbose_name='Название категории')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=16, verbose_name='Название тега')

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название задачи')
    deadline = models.DateField(blank=True, null=True, verbose_name='Крайний срок выполнения')
    description = models.TextField(blank=True, null=True, verbose_name='Описание задачи')
    done = models.BooleanField(default=False, verbose_name='Выполнена')
    created_at = models.DateTimeField(default=now, verbose_name='Создана')
    updated_at = models.DateTimeField(default=now, verbose_name='Изменена')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        for field in self._meta.concrete_fields:
            if field.is_relation and field.is_cached(self):
                obj = getattr(self, field.name, None)
                if not obj:
                    continue
                if obj.pk is None:
                    if not field.remote_field.multiple:
                        field.remote_field.delete_cached_value(obj)
                    raise ValueError(
                        "save() prohibited to prevent data loss due to "
                        "unsaved related object '%s'." % field.name
                    )
                elif getattr(self, field.attname) is None:
                    setattr(self, field.attname, obj.pk)
                if getattr(obj, field.target_field.attname) != getattr(self, field.attname):
                    field.delete_cached_value(self)

        using = using or router.db_for_write(self.__class__, instance=self)
        if force_insert and (force_update or update_fields):
            raise ValueError("Cannot force both insert and updating in model saving.")

        deferred_fields = self.get_deferred_fields()
        if update_fields is not None:
            if not update_fields:
                return

            update_fields = frozenset(update_fields)
            field_names = set()

            for field in self._meta.fields:
                if not field.primary_key:
                    field_names.add(field.name)

                    if field.name != field.attname:
                        field_names.add(field.attname)

            non_model_fields = update_fields.difference(field_names)

            if non_model_fields:
                raise ValueError("The following fields do not exist in this "
                                 "model or are m2m fields: %s"
                                 % ', '.join(non_model_fields))

        elif not force_insert and deferred_fields and using == self._state.db:
            field_names = set()
            for field in self._meta.concrete_fields:
                if not field.primary_key and not hasattr(field, 'through'):
                    field_names.add(field.attname)
            loaded_fields = field_names.difference(deferred_fields)
            if loaded_fields:
                update_fields = frozenset(loaded_fields)

        self.updated_at = now()
        self.save_base(using=using, force_insert=force_insert,
                       force_update=force_update, update_fields=update_fields)

    def _do_update(self, base_qs, using, pk_val, values, update_fields, forced_update):
        for task in base_qs:
            if task.id == pk_val:
                old_values = {'name': task.name, 'deadline': task.deadline, 'description': task.description, 'done': task.done, 'is_active': task.is_active, 'created_at': task.created_at, 'updated_at': task.updated_at}
        new_values = {}
        for new_value in values:
            new_values[new_value[0].name] = new_value[-1]
        for key in new_values.keys():
            if new_values[key] != old_values[key]:
                with open('log.txt', 'a') as log_file:
                    log_file.write(f'{now()} => В задаче с id = {pk_val} поле {key} было изменено со значения "{old_values[key]}" на значение "{new_values[key]}"\n')

        filtered = base_qs.filter(pk=pk_val)

        if not values:
            return update_fields is not None or filtered.exists()
        if self._meta.select_on_save and not forced_update:
            return (
                    filtered.exists() and
                    (filtered._update(values) > 0 or filtered.exists())
            )
        return filtered._update(values) > 0

    def _do_insert(self, manager, using, fields, returning_fields, raw):
        with open('log.txt', 'a') as log_file:
            log_file.write(
                f'{now()} => Добавлена новая задача "{self.name}"\n')
        return manager._insert(
            [self], fields=fields, returning_fields=returning_fields,
            using=using, raw=raw,
        )

    def delete(self, using=None, keep_parents=False):
        with open('log.txt', 'a') as log_file:
            log_file.write(
                f'{now()} => Была удалена задача "{self.name}"\n')

        using = using or router.db_for_write(self.__class__, instance=self)
        assert self.pk is not None, (
                (self._meta.object_name, self._meta.pk.attname)
        )

        collector = Collector(using=using)
        collector.collect([self], keep_parents=keep_parents)
        return collector.delete()


class CategoryTask(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задача')


class TagTask(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тег')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задача')
