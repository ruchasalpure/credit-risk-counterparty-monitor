from crewai import Agent

credit_risk_counterparty_monitor = Agent(
    role="Credit Risk Counterparty Monitor",
    goal="Deliver high-precision autonomous Credit Risk Counterparty Monitor operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
