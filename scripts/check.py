from pathlib import Path
import json
p = Path(__file__).resolve().parents[1]
s = p / 'skills' / 'ai-film-prompt-director'
for name in ['SKILL.md','agents/openai.yaml','references/quality.md','references/director-methods.md','references/diagnosis.md','references/records.md']:
    assert (s/name).is_file(), name
cases=json.loads((p/'tests'/'fixtures.json').read_text(encoding='utf-8'))
assert len(cases)>=3 and all(x['input'] and x['expected'] for x in cases)
print('Public structure and fixtures: PASS; not a model behavior test')
