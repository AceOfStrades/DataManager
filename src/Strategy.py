"""
hooks into Ingestion.py using events such as 'OnTrade','OnAggregateBar',etc.
Multiple independent strategies can be registered and run.
Feeding strategies interfaces with events makes BacktestEngine run on same code than the live trading processor.
"""