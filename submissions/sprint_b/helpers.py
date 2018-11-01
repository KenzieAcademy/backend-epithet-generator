import os
import json
import random
import unittest

class FileManager:
    """Handle local File System IO"""

    @staticmethod
    def get_extension(path):
        """Get extension from file path"""
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode="r", *args, **kwargs):
        with open(path, mode=mode, *args, **kwargs) as handle:
            return json.load(handle)


class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path, *args, **kwargs)

        return representation

    @classmethod
    def from_json(cls, path, fields=True, *args, **kwargs):
        data = cls.files.read_json(path, *args, **kwargs)
        if fields:
            representation = (data, data.keys())
        else:
            representation = data
        print representation
        return representation

    @classmethod
    def strategies(cls, file_extension, intent='read'):
        input_strategies = {"json": cls.from_json}
        if intent is "read":
            return input_strategies[file_extension]

class EpithetGenerator:
    """Pull from the reasources folder to generate the vocabulary and then use the
    vocabulary to generate epithets"""


    @classmethod
    def vocab_generator(cls):
        file_manager = FileManager()
        vocabulary = Vocabulary()
        resources = ['/Users/Ben/Documents/Kenzie/Code/Activities/PYTHON/backend-epithet-generator/resources/data.json']
        for path in resources:
            extension = file_manager.get_extension(path)
            if extension == 'json':
                epi_dict = vocabulary.from_file(path)
                return epi_dict
            else:
                vocabulary.from_file(path)

    @classmethod
    def epi_generator(cls):
        epi_dict = cls.vocab_generator()
        return (random.choice(epi_dict[0]["Column 1"]) + " "
                + random.choice(epi_dict[0]["Column 2"]) + " "
                + random.choice(epi_dict[0]["Column 3"]))


epithet_generator = EpithetGenerator()

class TestFileManager(unittest.TestCase):
    """Test the FileManager class within the helpers file"""

    def test_get_extension_(self):
        self.assertEqual(FileManager.get_extension(
            '/Users/Ben/Documents/Kenzie/Code/Activities/PYTHON/backend-epithet-generator/resources/data.json'),
            'json')

    def test_read_json(self):
        self.assertEqual(FileManager.read_json(
            '/Users/Ben/Documents/Kenzie/Code/Activities/PYTHON/backend-epithet-generator/resources/data.json',
            mode="r"), {u'Column 2': [u'base-court', u'bat-fowling', u'beef-witted',
            u'beetle-headed', u'boil-brained', u'clapper-clawed', u'clay-brained',
            u'common-kissing',u'crook-pated', u'dismal-dreaming', u'dizzy-eyed',
            u'doghearted', u'dread-bolted', u'earth-vexing', u'elf-skinned',
            u'fat-kidneyed', u'fen-sucked', u'flap-mouthed', u'fly-bitten',
            u'folly-fallen', u'fool-born', u'full-gorged', u'guts-griping',
            u'half-faced', u'hasty-witted', u'hedge-born', u'hell-hated',
            u'idle-headed', u'ill-breeding', u'ill-nurtured', u'knotty-pated',
            u'milk-livered', u'motley-minded', u'onion-eyed', u'plume-plucked',
            u'pottle-deep', u'pox-marked', u'reeling-ripe', u'rough-hewn',
            u'rude-growing', u'rump-fed', u'shard-borne', u'sheep-biting',
            u'spur-galled', u'swag-bellied', u'tardy-gaited', u'tickle-brained',
            u'toad-spotted', u'unchin-snouted',u'weather-bitten', u'whoreson',
            u'malmsey-nosed', u'rampallian', u'lily-livered', u'scurvy-valiant',
            u'brazen-faced', u"unwash'd", u"bunch-back'd", u'leaden-footed',
            u'muddy-mettled', u"pigeon-liver'd", u'scale-sided'], u'Column 3':
            [u'apple-john', u'baggage', u'barnacle', u'bladder', u'boar-pig',
            u'bugbear', u'bum-bailey', u'canker-blossom', u'clack-dish',
            u'clotpole', u'coxcomb', u'codpiece', u'death-token', u'dewberry',
            u'flap-dragon', u'flax-wench', u'flirt-gill', u'foot-licker',
            u'fustilarian', u'giglet', u'gudgeon', u'haggard', u'harpy',
            u'hedge-pig', u'horn-beast', u'hugger-mugger', u'joithead',
            u'lewdster', u'lout', u'maggot-pie', u'malt-worm', u'mammet',
            u'measle', u'minnow', u'miscreant', u'moldwarp', u'mumble-news',
            u'nut-hook', u'pigeon-egg', u'pignut', u'puttock', u'pumpion',
            u'ratsbane', u'scut', u'skainsmate', u'strumpet', u'varlot',
            u'vassal', u'whey-face', u'wagtail', u'knave', u'blind-worm',
            u'popinjay', u'scullian', u'jolt-head', u'malcontent', u'devil-monk',
            u'toad', u'rascal', u'Basket-Cockle'], u'Column 1': [u'artless',
            u'bawdy', u'beslubbering', u'bootless', u'churlish', u'cockered',
            u'clouted', u'craven', u'currish', u'dankish', u'dissembling',
            u'droning', u'errant', u'fawning', u'fobbing', u'froward', u'frothy',
            u'gleeking', u'goatish', u'gorbellied', u'impertinent', u'infectious',
            u'jarring', u'loggerheaded', u'lumpish', u'mammering', u'mangled',
            u'mewling', u'paunchy', u'pribbling', u'puking', u'puny', u'qualling',
            u'rank', u'reeky', u'roguish', u'ruttish', u'saucy', u'spleeny',
            u'spongy', u'surly', u'tottering', u'unmuzzled', u'vain', u'venomed',
            u'villainous', u'warped', u'wayward', u'weedy', u'yeasty',
            u'cullionly', u'fusty', u'caluminous', u'wimpled', u'burly-boned',
            u'misbegotten', u'odiferous', u'poisonous', u'fishified',
            u'Wart-necked']})

class TestVocabulary(unittest.TestCase):
    """Test the Vocabulary class within the helpers file"""

    def test_from_json(self):
        self.assertEqual(Vocabulary.from_json('/Users/Ben/Documents/Kenzie/Code/Activities/PYTHON/backend-epithet-generator/resources/data.json',
        fields=True), ({u'Column 2': [u'base-court', u'bat-fowling',
        u'beef-witted', u'beetle-headed', u'boil-brained',
        u'clapper-clawed', u'clay-brained', u'common-kissing',
        u'crook-pated', u'dismal-dreaming', u'dizzy-eyed', u'doghearted',
        u'dread-bolted', u'earth-vexing', u'elf-skinned', u'fat-kidneyed',
        u'fen-sucked', u'flap-mouthed', u'fly-bitten', u'folly-fallen',
        u'fool-born', u'full-gorged', u'guts-griping', u'half-faced',
        u'hasty-witted', u'hedge-born', u'hell-hated', u'idle-headed',
        u'ill-breeding', u'ill-nurtured', u'knotty-pated', u'milk-livered',
        u'motley-minded', u'onion-eyed', u'plume-plucked', u'pottle-deep',
        u'pox-marked', u'reeling-ripe', u'rough-hewn', u'rude-growing',
        u'rump-fed', u'shard-borne', u'sheep-biting', u'spur-galled',
        u'swag-bellied', u'tardy-gaited', u'tickle-brained',
        u'toad-spotted', u'unchin-snouted', u'weather-bitten', u'whoreson',
        u'malmsey-nosed', u'rampallian', u'lily-livered', u'scurvy-valiant',
        u'brazen-faced', u"unwash'd", u"bunch-back'd", u'leaden-footed',
        u'muddy-mettled', u"pigeon-liver'd", u'scale-sided'], u'Column 3':
        [u'apple-john', u'baggage', u'barnacle', u'bladder', u'boar-pig',
        u'bugbear', u'bum-bailey', u'canker-blossom', u'clack-dish', u'clotpole',
        u'coxcomb', u'codpiece', u'death-token', u'dewberry', u'flap-dragon',
        u'flax-wench', u'flirt-gill', u'foot-licker', u'fustilarian', u'giglet',
        u'gudgeon', u'haggard', u'harpy', u'hedge-pig', u'horn-beast',
        u'hugger-mugger', u'joithead', u'lewdster', u'lout', u'maggot-pie',
        u'malt-worm', u'mammet', u'measle', u'minnow', u'miscreant', u'moldwarp',
        u'mumble-news', u'nut-hook', u'pigeon-egg', u'pignut', u'puttock',
        u'pumpion', u'ratsbane', u'scut', u'skainsmate', u'strumpet', u'varlot',
        u'vassal', u'whey-face', u'wagtail', u'knave', u'blind-worm', u'popinjay',
        u'scullian', u'jolt-head', u'malcontent', u'devil-monk', u'toad',
        u'rascal', u'Basket-Cockle'], u'Column 1': [u'artless', u'bawdy',
        u'beslubbering', u'bootless', u'churlish', u'cockered', u'clouted',
        u'craven', u'currish', u'dankish', u'dissembling', u'droning', u'errant',
        u'fawning', u'fobbing', u'froward', u'frothy', u'gleeking', u'goatish',
        u'gorbellied', u'impertinent', u'infectious', u'jarring', u'loggerheaded',
        u'lumpish', u'mammering', u'mangled', u'mewling', u'paunchy', u'pribbling',
        u'puking', u'puny', u'qualling', u'rank', u'reeky', u'roguish', u'ruttish',
        u'saucy', u'spleeny', u'spongy', u'surly', u'tottering', u'unmuzzled',
        u'vain', u'venomed', u'villainous', u'warped', u'wayward', u'weedy',
        u'yeasty', u'cullionly', u'fusty', u'caluminous', u'wimpled',
        u'burly-boned', u'misbegotten', u'odiferous', u'poisonous',
        u'fishified', u'Wart-necked']}, [u'Column 2', u'Column 3', u'Column 1']))

    def test_strategies(self):
        self.assertEquals(Vocabulary.strategies("json", intent='read'),
        input_strategies["json"])

if __name__ == '__main__':
    unittest.main()