from mock import patch
from pysparkling import Context
from jobs.wordcount import run

@patch('jobs.wordcount.WordCountJobContext.initalize_counter')
@patch('jobs.wordcount.WordCountJobContext.inc_counter')
def test_wordcount_run(_, __):
    result = run(Context())
    assert len(result) == 327
    assert result[:6] == [('ut', 17), ('eu', 16), ('vel', 14), ('nec', 14), ('vitae', 12), ('quis', 12)]
