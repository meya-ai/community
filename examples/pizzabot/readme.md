# PizzaBot example

Try me here: https://meya.ai/pizzabot

Say 'hi' to start.

**Flows:**

1. `pizza_flow_simple.yaml`: no custom components, uses mustache syntax inline
2. `pizza_flow_custom.yaml`: a custom component that reads from datastore


**Triggers:**

A simple regex filter for the words "order" and "pizza"

    pattern: ^.*(\border\b).*(\bpizza\b).*$

**Components:**

`pizza_confirmation.py`: referenced by  `pizza_flow_custom.yaml` and outputs conditional response based on pizza type.
