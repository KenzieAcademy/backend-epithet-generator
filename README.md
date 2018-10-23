# Epithet Generator

Create a Flask API to serve random epithets from the [Shakespeare Insult Kit](http://www.pangloss.com/seidel/shake_rule.html).
Each sprint is an assignment with its own deliverables. Please create a pull request to the appropriate branch to submit
assignments. 

## Instructions
Sprint|Description|Commit
---|---|---|
[a](https://github.com/KenzieAcademy/backend-epithet-generator/blob/master/instructions/sprint_a.md)|minimal flask applications|
| |larger applications|
| |unit testing|
| |integration testing|
| |design patterns|

##Expected payloads
@app.get("/")
    Thou fawning weather-bitten strumpet
@app.get("/vocabulary")
    Column 1: ['artless', 'bawdy', 'beslubbering', 'bootless', 'churlish', 'cockered', 'clouted', 'craven', 'currish', 'dankish', 'dissembling', 'droning', 'errant', 'fawning', 'fobbing', 'froward', 'frothy', 'gleeking', 'goatish', 'gorbellied', 'impertinent', 'infectious', 'jarring', 'loggerheaded', 'lumpish', 'mammering', 'mangled', 'mewling', 'paunchy', 'pribbling', 'puking', 'puny', 'qualling', 'rank', 'reeky', 'roguish', 'ruttish', 'saucy', 'spleeny', 'spongy', 'surly', 'tottering', 'unmuzzled', 'vain', 'venomed', 'villainous', 'warped', 'wayward', 'weedy', 'yeasty', 'cullionly', 'fusty', 'caluminous', 'wimpled', 'burly-boned', 'misbegotten', 'odiferous', 'poisonous', 'fishified', 'Wart-necked']<br/><br/>Column 2: ['base-court', 'bat-fowling', 'beef-witted', 'beetle-headed', 'boil-brained', 'clapper-clawed', 'clay-brained', 'common-kissing', 'crook-pated', 'dismal-dreaming', 'dizzy-eyed', 'doghearted', 'dread-bolted', 'earth-vexing', 'elf-skinned', 'fat-kidneyed', 'fen-sucked', 'flap-mouthed', 'fly-bitten', 'folly-fallen', 'fool-born', 'full-gorged', 'guts-griping', 'half-faced', 'hasty-witted', 'hedge-born', 'hell-hated', 'idle-headed', 'ill-breeding', 'ill-nurtured', 'knotty-pated', 'milk-livered', 'motley-minded', 'onion-eyed', 'plume-plucked', 'pottle-deep', 'pox-marked', 'reeling-ripe', 'rough-hewn', 'rude-growing', 'rump-fed', 'shard-borne', 'sheep-biting', 'spur-galled', 'swag-bellied', 'tardy-gaited', 'tickle-brained', 'toad-spotted', 'unchin-snouted', 'weather-bitten', 'whoreson', 'malmsey-nosed', 'rampallian', 'lily-livered', 'scurvy-valiant', 'brazen-faced', "unwash'd", "bunch-back'd", 'leaden-footed', 'muddy-mettled', "pigeon-liver'd", 'scale-sided']<br/><br/>Column 3: ['apple-john', 'baggage', 'barnacle', 'bladder', 'boar-pig', 'bugbear', 'bum-bailey', 'canker-blossom', 'clack-dish', 'clotpole', 'coxcomb', 'codpiece', 'death-token', 'dewberry', 'flap-dragon', 'flax-wench', 'flirt-gill', 'foot-licker', 'fustilarian', 'giglet', 'gudgeon', 'haggard', 'harpy', 'hedge-pig', 'horn-beast', 'hugger-mugger', 'joithead', 'lewdster', 'lout', 'maggot-pie', 'malt-worm', 'mammet', 'measle', 'minnow', 'miscreant', 'moldwarp', 'mumble-news', 'nut-hook', 'pigeon-egg', 'pignut', 'puttock', 'pumpion', 'ratsbane', 'scut', 'skainsmate', 'strumpet', 'varlot', 'vassal', 'whey-face', 'wagtail', 'knave', 'blind-worm', 'popinjay', 'scullian', 'jolt-head', 'malcontent', 'devil-monk', 'toad', 'rascal', 'Basket-Cockle']
@app.get("/epithets/4)
    Thou dissembling reeling-ripe pigeon-egg<br/>Thou puking hell-hated ratsbane<br/>Thou Wart-necked weather-bitten bladder<br/>Thou roguish folly-fallen lewdster<br/>