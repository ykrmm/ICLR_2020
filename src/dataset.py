# Load datasets

from torchnlp.datasets import iwslt_dataset


train_en_to_de = iwslt_dataset(train=True)
test_en_to_de = iwslt_dataset(test=True)

train_it_to_en = iwslt_dataset(train=True,\
    language_extensions=['it', 'en'],\
        url='https://wit3.fbk.eu/archive/2016-01/texts/it/en/it-en.tgz')

test_it_to_en = iwslt_dataset(test=True,\
    language_extensions=['it','en'],\
    url='https://wit3.fbk.eu/archive/2016-01/texts/it/en/it-en.tgz')

print(train_en_to_de[:2])
print(train_it_to_en[:2])
