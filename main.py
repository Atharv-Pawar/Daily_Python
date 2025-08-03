import random 
from collections import Counter

anyword_fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
    "pineapple", "mango", "papaya", "orange", "blueberry", "raspberry", "strawberry", "guava", "lychee", "plum",
    "peach", "apricot", "blackberry", "coconut", "pomegranate", "nectarine", "tangerine", "watermelon", "canteloupe", "dragonfruit",
    "jackfruit", "durian", "passionfruit", "starfruit", "mulberry", "currant", "kumquat", "soursop", "loganberry", "rambutan",
    "persimmon", "quince", "medlar", "feijoa", "boysenberry", "cloudberry", "gooseberry", "ackee", "miraclefruit", "salak", "pear", "custardapple",
    "sapodilla", "longan", "tamarind", "clementine", "bloodorange", "clementine", "calamondin", "bergamot", "citron", "fingerlime", "blackcurrant",
    "whitecurrant", "redcurrant", "jostaberry", "huckleberry", "serviceberry", "barberry", "sea buckthorn", "bilberry", "lingonberry", "cranberry", "cloudberry",
    "salalberry", "chokeberry", "mayhaw", "medlar", "saskatoonberry", "chokecherry", "hawthornberry", "wintermelon", "bittermelon", "balsamapple", "balsampear", "bittergourd", "bittercucumber",
    "bittermelon", "bitterorange", "bitterlemon", "bitterlime", "bittermelon", "bitterapple", "bittercucumber", "bittergourd", "bittermelon"]

anyword_flowers = ["rose", "tulip", "daisy", "sunflower", "lily", "orchid", "daffodil", "marigold", "peony", "hydrangea",
    "lavender", "chrysanthemum", "carnation", "iris", "poppy", "violet", "zinnia", "geranium", "begonia", "snapdragon", "freesia",
    "lilac", "azalea", "camellia", "rhododendron", "hibiscus", "petunia", "gladiolus", "crocus", "hyacinth", "anemone",
    "dahlia", "fuchsia", "foxglove", "larkspur", "delphinium", "scabiosa", "statice", "sweet pea", "cosmos", "nasturtium",
    "calendula", "borage", "heliotrope", "phlox", "coreopsis", "yarrow", "asters", "monarda", "echinacea", "rudbeckia",
    "tithonia", "zantedeschia", "calla lily", "alstromeria", "gerbera", "strelitzia", "bird of paradise", "kangaroo paw", "leucospermum", "proteaceae",
    "banksia", "waratah", "grevillea", "mimosa", "acacia", "wattle", "gum blossom", "tea tree", "bottlebrush", "paperbark",
    "kangaroo paw", "heath", "heather", "erica", "bellflower", "campanula", "lobelia", "columbine", "aquilegia", "foxglove", "digitalis",
    "lupine", "bluebell", "snowdrop", "winter aconite", "cowslip", "primrose", "oxeye daisy", "buttercup", "wood anemone", "meadow buttercup",
    "wildflower", "wild rose", "wild geranium", "wild violet", "wild daisy", "wild sunflower", "wild iris", "wild lily", "wild orchid", "wild poppy",
    "wild peony", "wild hydrangea", "wild lavender", "wild chrysanthemum", "wild carnation", "wild daffodil", "wild tulip", "wild snapdragon", "wild freesias", "wild zinnia"]  

