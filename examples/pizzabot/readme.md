# PizzaBot example

Try me here: https://meya.ai/pizzabot

Responds to:
- hi
- age
- order a pizza
- I want a pepperoni pizza
- age

**Flows:**

1. `simple.yaml`: no custom components, uses mustache syntax inline
2. `custom.yaml`: includes a custom component that reads from datastore
3. `incoming.yaml`: expects pre-parsed data from the intent filter (regex, wit.ai, etc.)
4. `conditional.yaml`: checks the user's age and conditionally traverses states


**Intents:**

1. `order.yaml`: A simple regex filter for the words "order" and "pizza"
2. `entities.yaml`: Extracts pizza type from the text (ie. "hawaiian")


**Components:**

1. `confirmation.py`: outputs response based on pizza type.
2. `age.py`: checks the age (age>=18?) and returns flow control actions ("over", "under")
