# Text Deduplicator
Pass a list of string and get a result list of all the duplicates grouped together!

## Requirements
* Python 2.4 or higher
* nltk
* fuzzywuzzy

## Usage

```python
    >>> from txtdedup import groupdups
    >>> groupdups(strings_to_group=[], pp_technique='stem', similarity_ratio=70) where
    * text_list = List of strings to be compares
    * pp_technique = Pre-processing technique which can be either 'stem' or 'lemmatize' defaults to 'stem'
    * similarity_ratio = Defaults to 70
```

#### Simple Example

```python
    >>> titles = [
            "Snapchat changes name to Snap Inc., debuts 'Spectacles'",
            "Samsung delays restart of its Galaxy Note 7 sale",
            "Snapchat debuts recording 'Spectacles,' changes company name'",
            "Microsoft Bets Its Future on a Reprogrammable Computer Chip",
            "Samsung halts sales of Galaxy Note 7 after new troubles"]
            
    >>> groupdups(strings_to_group=titles, pp_technique='stem', similarity_ratio=70)
        [   [   "Snapchat changes name to Snap Inc., debuts 'Spectacles'",
                "Snapchat debuts recording 'Spectacles,' changes company name'"],
            [   'Samsung delays restart of its Galaxy Note 7 sale',
                'Samsung halts sales of Galaxy Note 7 after new troubles'],
            ['Microsoft Bets Its Future on a Reprogrammable Computer Chip']]
```

