overall_category_id = '0x02E00000FFFFFFFF'

hero_category_ids = {
    'reaper': '0x02E0000000000002',
    'tracer': '0x02E0000000000003',
    'mercy': '0x02E0000000000004',
    'hanzo': '0x02E0000000000005',
    'torbjorn': '0x02E0000000000006',
    'reinhardt': '0x02E0000000000007',
    'pharah': '0x02E0000000000008',
    'winston': '0x02E0000000000009',
    'widowmaker': '0x02E000000000000A',
    'bastion': '0x02E0000000000015',
    'symmetra': '0x02E0000000000016',
    'zenyatta': '0x02E0000000000020',
    'genji': '0x02E0000000000029',
    'roadhog': '0x02E0000000000040',
    'mccree': '0x02E0000000000042',
    'junkrat': '0x02E0000000000065',
    'zarya': '0x02E0000000000068',
    'soldier76': '0x02E000000000006E',
    'lucio': '0x02E0000000000079',
    'dva': '0x02E000000000007A',
    'mei': '0x02E00000000000DD',
    'ana': '0x02E000000000013B',
}
inverted_hero_category_ids = { category_id: hero for hero, category_id in hero_category_ids.items() }

# Brought from https://github.com/SunDwarf/OWAPI/blob/master/owapi/prestige.py
level_ids = {
    # Bronze
    '0x0250000000000918': 0,
    '0x0250000000000919': 0,
    '0x025000000000091A': 0,
    '0x025000000000091B': 0,
    '0x025000000000091C': 0,
    '0x025000000000091D': 0,
    '0x025000000000091E': 0,
    '0x025000000000091F': 0,
    '0x0250000000000920': 0,
    '0x0250000000000921': 0,
    '0x0250000000000922': 100,
    '0x0250000000000924': 100,
    '0x0250000000000925': 100,
    '0x0250000000000926': 100,
    '0x025000000000094C': 100,
    '0x0250000000000927': 100,
    '0x0250000000000928': 100,
    '0x0250000000000929': 100,
    '0x025000000000092B': 100,
    '0x0250000000000950': 100,
    '0x025000000000092A': 200,
    '0x025000000000092C': 200,
    '0x0250000000000937': 200,
    '0x025000000000093B': 200,
    '0x0250000000000933': 200,
    '0x0250000000000923': 200,
    '0x0250000000000944': 200,
    '0x0250000000000948': 200,
    '0x025000000000093F': 200,
    '0x0250000000000951': 200,
    '0x025000000000092D': 300,
    '0x0250000000000930': 300,
    '0x0250000000000934': 300,
    '0x0250000000000938': 300,
    '0x0250000000000940': 300,
    '0x0250000000000949': 300,
    '0x0250000000000952': 300,
    '0x025000000000094D': 300,
    '0x0250000000000945': 300,
    '0x025000000000093C': 300,
    '0x025000000000092E': 400,
    '0x0250000000000931': 400,
    '0x0250000000000935': 400,
    '0x025000000000093D': 400,
    '0x0250000000000946': 400,
    '0x025000000000094A': 400,
    '0x0250000000000953': 400,
    '0x025000000000094E': 400,
    '0x0250000000000939': 400,
    '0x0250000000000941': 400,
    '0x025000000000092F': 500,
    '0x0250000000000932': 500,
    '0x025000000000093E': 500,
    '0x0250000000000936': 500,
    '0x025000000000093A': 500,
    '0x0250000000000942': 500,
    '0x0250000000000947': 500,
    '0x025000000000094F': 500,
    '0x025000000000094B': 500,
    '0x0250000000000954': 500,
    # Silver
    '0x0250000000000956': 600,
    '0x025000000000095C': 600,
    '0x025000000000095D': 600,
    '0x025000000000095E': 600,
    '0x025000000000095F': 600,
    '0x0250000000000960': 600,
    '0x0250000000000961': 600,
    '0x0250000000000962': 600,
    '0x0250000000000963': 600,
    '0x0250000000000964': 600,
    '0x0250000000000957': 700,
    '0x0250000000000965': 700,
    '0x0250000000000966': 700,
    '0x0250000000000967': 700,
    '0x0250000000000968': 700,
    '0x0250000000000969': 700,
    '0x025000000000096A': 700,
    '0x025000000000096B': 700,
    '0x025000000000096C': 700,
    '0x025000000000096D': 700,
    '0x0250000000000958': 800,
    '0x025000000000096E': 800,
    '0x025000000000096F': 800,
    '0x0250000000000970': 800,
    '0x0250000000000971': 800,
    '0x0250000000000972': 800,
    '0x0250000000000973': 800,
    '0x0250000000000974': 800,
    '0x0250000000000975': 800,
    '0x0250000000000976': 800,
    '0x0250000000000959': 900,
    '0x0250000000000977': 900,
    '0x0250000000000978': 900,
    '0x0250000000000979': 900,
    '0x025000000000097A': 900,
    '0x025000000000097B': 900,
    '0x025000000000097C': 900,
    '0x025000000000097D': 900,
    '0x025000000000097E': 900,
    '0x025000000000097F': 900,
    '0x025000000000095A': 1000,
    '0x0250000000000980': 1000,
    '0x0250000000000981': 1000,
    '0x0250000000000982': 1000,
    '0x0250000000000983': 1000,
    '0x0250000000000984': 1000,
    '0x0250000000000985': 1000,
    '0x0250000000000986': 1000,
    '0x0250000000000987': 1000,
    '0x0250000000000988': 1000,
    '0x025000000000095B': 1100,
    '0x0250000000000989': 1100,
    '0x025000000000098A': 1100,
    '0x025000000000098B': 1100,
    '0x025000000000098C': 1100,
    '0x025000000000098D': 1100,
    '0x025000000000098E': 1100,
    '0x025000000000098F': 1100,
    '0x0250000000000991': 1100,
    '0x0250000000000990': 1100,
    # Gold
    '0x0250000000000992': 1200,
    '0x0250000000000993': 1200,
    '0x0250000000000994': 1200,
    '0x0250000000000995': 1200,
    '0x0250000000000996': 1200,
    '0x0250000000000997': 1200,
    '0x0250000000000998': 1200,
    '0x0250000000000999': 1200,
    '0x025000000000099A': 1200,
    '0x025000000000099B': 1002
}