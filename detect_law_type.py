import joblib
import pandas as pd

class Law:
  def __init__(self, law: list[str] | None):
    self.law = law
    self.ready = False
    
  def __prepare():
    RuleClf = joblib.load('Rule.Clf')
    rule_soft_type = RuleClf.predict_probs(self.law)
    rule_soft_type = pd.DataFrame(rule_soft_type, columns=RuleClf.classes_)
    rule_soft_type.insert(0, 'sents', self.law)
    self.rule_soft_type = rule_soft_type
    rule_hard_type = RuleClf.predict(self.law)
    rule_hard_type = pd.DataFrame({'sents': self.law, 'label': rule_hard_type})
    self.rule_hard_type = rule_hard_type
    self.defs = self.rule_hard_type[rules_hard_type['label'] == 'Definition']['sents']
    self.oblgs = self.rule_hard_type[rules_hard_type['label'] == 'Obligation']['sents']
    self.prohs = self.rule_hard_type[rules_hard_type['label'] == 'Prohibition']['sents']
    self.sancs = self.rule_hard_type[rules_hard_type['label'] == 'Sanction']['sents']
    self.exceps = self.rule_hard_type[rules_hard_type['label'] == 'Exception']['sents']
    
    # prepared
    
    self.ready = True

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

  def legal_function():
    if self.ready:
      return self.rule_hard_type
    self.__prepare()
    return self.rule_hard_type

  def legal_function_probs():
    if self.ready:
      return self.rule_soft_type
    self.__prepare()
    return self.rule_soft_type

  def definitions():
    if self.ready:
      return self.defs
    self.__prepare()
    return self.defs

  def obligations():
    if self.ready:
      return self.oblgs
    self.__prepare()
    return self.oblgs

  def prohibitions():
    if self.ready:
      return self.prohs
    self.__prepare()
    return self.prohs
    
  def sanctions():
    if self.ready:
      return self.sancs
    self.__prepare()
    return self.sancs
    
  def exceptions():
    if self.ready:
      return self.exceps
    self.__prepare()
    return self.exceps
    
    
    


