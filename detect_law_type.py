import joblib
import pandas as pd

class Law:
  def __init__(self, law: list[str] | None):
    self.law = law
    self.ready = False
    
  def __isready(self):
    return self.ready
      
  def __ensure_law(self):
    if not self.law:
      raise Exception("Law List Is Empty")
  def __prepare(self):
    self.ensure_law()
    RuleClf = joblib.load('RuleClf.joblib')
    rule_soft_type = RuleClf.predict_proba(self.law)
    rule_soft_type = pd.DataFrame(rule_soft_type, columns=RuleClf.classes_)
    rule_soft_type.insert(0, 'sents', self.law)
    self.rule_soft_type = rule_soft_type
    rule_hard_type = RuleClf.predict(self.law)
    rule_hard_type = pd.DataFrame({'sents': self.law, 'label': rule_hard_type})
    self.rule_hard_type = rule_hard_type
    self.defs = self.rule_hard_type[rule_hard_type['label'] == 'Definition']['sents']
    self.oblgs = self.rule_hard_type[rule_hard_type['label'] == 'Obligation']['sents']
    self.prohs = self.rule_hard_type[rule_hard_type['label'] == 'Prohibition']['sents']
    self.sancs = self.rule_hard_type[rule_hard_type['label'] == 'Sanction']['sents']
    self.exceps = self.rule_hard_type[rule_hard_type['label'] == 'Exception']['sents']
    
    # prepared
    
    self.ready = True

  def rules_types(self) -> pd.DataFrame:
    self.__ensure_law()
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
    df = self.types_ratio()
    maxv = df['Percentage'].max()
    df = df[df['Percentage'] > maxv - margin]
    if len(df) == 1:
      return df['Law Type'].iloc[0]
    else:
      return df[['Law Type', 'Percentage']].sort_values(by=['Percentage'], ascending=False).reset_index(drop=True)

  def legal_function(self):
    if self.__isready():
      return self.rule_hard_type
    self.__prepare()
    return self.rule_hard_type

  def legal_function_probs(self):
    if self.__isready():
      return self.rule_soft_type
    self.__prepare()
    return self.rule_soft_type

  def definitions(self):
    if self.__isready():
      return self.defs
    self.__prepare()
    return self.defs

  def obligations(self):
    if self.__isready():
      return self.oblgs
    self.__prepare()
    return self.oblgs

  def prohibitions(self):
    if self.__isready():
      return self.prohs
    self.__prepare()
    return self.prohs
    
  def sanctions(self):
    if self.__isready():
      return self.sancs
    self.__prepare()
    return self.sancs
    
  def exceptions(self):
    if self.__isready():
      return self.exceps
    self.__prepare()
    return self.exceps
    
    
    


