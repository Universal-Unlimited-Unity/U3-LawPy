import joblib
import pandas as pd

def Law_Rules_Types(LAW: list[str]) -> list[str]:
  if not LAW:
    raise Exception("LaW List Is Empty")
  LawClf = joblib.load('LawClf.joblib')
  rules_types = LawClf.predict(LAW)
  return rules_types

def Law_Rules_Ratio(LAW: list[str], percentage=False) -> pd.DataFrame:
  x=1
  if percentage:
    x=100
  law_types_ratio = (pd.DataFrame({'Law': Law_Rules_Types(LAW)}).value_counts(normalize=percentage)*x).reset_index(name='Ratio')
  return law_types_ratio

def Law_Exact_Type(LAW: list[str]) -> str | list[str]:
  law_types_ratio = Law_Rules_Ratio(LAW)
  max = law_types_ratio['Ratio'].max()
  law_types_ratio = law_types_ratio.query('Ratio == @max')
  if len(law_types_ratio) >= 2:
    return list(law_types_ratio['Law'])
  return str(list(law_types_ratio['Law'])[0])
  
