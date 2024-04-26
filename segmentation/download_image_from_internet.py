from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

# give me all animals name you want to download
keywords=['cat', 'dog', 'elephant', 'lion', 'tiger', 'bear', 'wolf', 'fox', 'deer', 'rabbit', 'squirrel', 'giraffe', 'zebra', 'hippopotamus', 'rhinoceros', 'kangaroo', 'koala', 'panda', 'monkey', 'gorilla', 'chimpanzee', 'lemur', 'sloth', 'bat', 'rat', 'mouse', 'hamster', 'guinea pig', 'rabbit', 'hedgehog', 'ferret', 'chinchilla', 'gerbil', 'parrot', 'cockatoo', 'macaw', 'budgerigar', 'canary', 'finch', 'lovebird', 'parakeet', 'cockatiel', 'conure', 'amazon', 'african grey', 'pigeon', 'dove', 'quail', 'peacock', 'ostrich', 'emu', 'rhea', 'kiwi', 'penguin', 'flamingo', 'swan', 'goose', 'duck', 'pelican', 'heron', 'stork', 'ibis', 'crane', 'egret', 'albatross', 'petrel', 'gull', 'tern', 'skua', 'puffin', 'auk', 'kingfisher', 'woodpecker', 'toucan', 'hornbill', 'barbet', 'jacamar', 'puffbird', 'motmot', 'bee-eater', 'roller', 'hoopoe', 'lark', 'swallow', 'swift', 'nightjar', 'hummingbird', 'tody', 'kinglet', 'nuthatch', 'creeper', 'wren', 'dipper', 'bulbul', 'thrush', 'robin', 'nightingale', 'redstart', 'wheatear', 'stonechat', 'chat', 'whip-poor-will', 'vireo', 'shrike', 'jay', 'magpie', 'crow', 'raven', 'starling', 'oriole', 'blackbird', 'grackle', 'cowbird', 'meadowlark', 'oriole', 'blackbird', 'grackle', 'cowbird', 'meadowlark', 'finch', 'sparrow', 'weaver', 'bunting', 'cardinal', 'tanager', 'warbler', 'blackcap', 'chiffchaff', ]

for keyword in keywords:
    response().download(keyword, 50)