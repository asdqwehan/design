import datetime
from haystack import indexes
from learning_logs.models import Entry

class EntryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    entrytitle = indexes.CharField(model_attr='entrytitle')
    entrytext = indexes.CharField(model_attr='text')

    def get_model(self):
        return Entry
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()