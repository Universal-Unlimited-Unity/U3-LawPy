import joblib
import pandas as pd

class Law:
  def __init__(self, law: list[str] | None):
    self.law = law
  
  def rules_types(self) -> pd.DataFrame:
    if not self.law:
      raise Exception("Law List Is Empty")
    LawClf = joblib.load('LawClf.joblib')
    probs = LawClf.predict_proba(self.law)
    df = pd.DataFrame(probs, columns=LawClf.classes_)
    df.insert(0, 'sents', self.law)
    return df

  def types_ratio(self, normalize: bool = False) -> pd.DataFrame:
    x=1
    if normalize:
      x=100
    df = self.rules_types()
    df.drop('sents', axis=1, inplace=True)
    df = df.mean().reset_index()
    df.columns = ['Law Type', 'Percentage']
    df['Percentage'] = df['Percentage']*x
    return df.sort_values(by='Percentage', ascending=False).reset_index(drop=True)


  def type(self, margin: float | None = None) -> str | pd.DataFrame:
    if margin is None:
      margin = 0.01
    df = self.types_ratio(self.law)
    maxv = df['Percentage'].max()
    df = df[df['Percentage'] > maxv - margin]
    if len(df) == 1:
      return df['Law Type'].iloc[0]
    else:
      return df[['Law Type', 'Percentage']].sort_values(by=['Percentage'], ascending=False).reset_index(drop=True)



