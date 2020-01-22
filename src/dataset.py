# Load datasets

from torchnlp.datasets import iwslt_dataset

## ATTENTION IL FAUT TELECHARGER LES DATASETS SUR
#  LES LIENS QUE J'AI MIS DANS LE README
# ENSUITE CREE UN DOSSIER data/iwslt_2014_2015 ET Y PLACER
# LES DOSSIERS de-en et en-vi


train_en_to_vi = iwslt_dataset(
        directory='data/iwslt_2014_2015/',
        train=True,
        dev=False,
        test=False,
        language_extensions=['en', 'vi'],
        train_filename='{source}-{target}/train.{source}-{target}.{lang}',
        test_filename='{source}-{target}/IWSLT15.TED.tst2013.{source}-{target}.{lang}',
        check_files=['{source}-{target}/train.tags.{source}-{target}.{source}'],
        )

test_en_to_vi = iwslt_dataset(
        directory='data/iwslt_2014_2015/',
        train=False,
        dev=False,
        test=True,
        language_extensions=['en', 'vi'],
        train_filename='{source}-{target}/train.{source}-{target}.{lang}',
        test_filename='{source}-{target}/IWSLT15.TED.tst2013.{source}-{target}.{lang}',
        check_files=['{source}-{target}/train.tags.{source}-{target}.{source}'],
        )

train_de_to_en = iwslt_dataset(
        directory='data/iwslt_2014_2015/',
        train=True,
        dev=False,
        test=False,
        language_extensions=['de', 'en'],
        train_filename='{source}-{target}/train.{source}-{target}.{lang}',
        test_filename='{source}-{target}/IWSLT14.TED.tst2012.{source}-{target}.{lang}',
        check_files=['{source}-{target}/train.tags.{source}-{target}.{source}'],
        )

test_de_to_en = iwslt_dataset(
        directory='data/iwslt_2014_2015/',
        train=False,
        dev=False,
        test=True,
        language_extensions=['de', 'en'],
        train_filename='{source}-{target}/train.{source}-{target}.{lang}',
        test_filename='{source}-{target}/IWSLT14.TED.tst2012.{source}-{target}.{lang}',
        check_files=['{source}-{target}/train.tags.{source}-{target}.{source}'],
        )

print('train english to vietnamise examples :')
print(train_en_to_vi[:2])
print('test english to vietnamise examples :') #Décommentez pour voir si ça marche bien 
print(test_en_to_vi[:2])
print('train german to english :')
print(train_de_to_en[:2]) #Décommentez pour voir si ça marche bien 
print('test german to english :')
print(test_de_to_en[:2])

