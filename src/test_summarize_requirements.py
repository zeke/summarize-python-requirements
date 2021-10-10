from summarize_requirements import summarize

def test_summarize():
  results = []
  for line in summarize('requirements.txt'):
      results.append(line)
  assert(len(results) == 4) 
  assert '# The uncompromising code formatter' in results[0]