from .data_loader import DataLoader
from .temporal_transformer import TemporalTransformer
from .forecaster import Forecaster
from .explainer import TrendExplainer
class ChronoMindOrchestrator:
    def __init__(self): self.l=DataLoader(); self.t=TemporalTransformer(); self.f=Forecaster(); self.e=TrendExplainer()
    def run(self,s,h,cf,cl): return {'forecast':self.f.forecast(s,h),'trend':self.e.explain(s)}
