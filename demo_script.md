# Finserv ML Demo - SE Demo Script

## Demo Overview

**Duration**: 20-30 minutes  
**Audience**: Data Science, ML Engineering, Fraud/Risk teams  
**Platform**: Snowflake Notebooks (run live) or pre-run with outputs visible

---

## Opening Discovery Questions

Ask 1-2 of these before starting the demo to tailor your narrative:

- "How many fraud models do you currently have in production?"
- "Do your fraud, AML, and credit risk teams share features, or does each team build their own?"
- "When a model degrades in production, how long does it typically take your team to detect and respond?"
- "Where does your model training pipeline run today - outside Snowflake? What does that handoff look like?"
- "Have you had situations where different teams calculated the same feature differently and got inconsistent results?"

---

## Demo Flow

### 1. Business Context (2 min)

Set the scene before opening any notebooks:

> "Payment fraud is one of the most operationally complex ML problems in finserv. It's not just about building a good model - it's about managing a portfolio of models across fraud, AML, and credit, where every team is doing their own feature engineering, often in silos. The result is you end up with 10 models calculating 'average transaction amount' 10 different ways.
>
> What we're going to show today is how Snowflake gives you a unified ML platform - Feature Store, Model Registry, real-time inference, monitoring - all inside Snowflake, where your data already lives."

### 2. Data and Feature Engineering (5 min)

Open `03_finserv_ml_demo.ipynb`. Run or show:

- **Table check cell**: "We have 10,000 transactions, 2,000 customers, and 500 merchants. This mirrors a real payment environment."

- **Pattern analysis cell**: "Notice the fraud rate by merchant category - e-commerce and travel are highest. This is exactly what we'd see in the real world."

Key talking point:
> "The features we're building here - transaction count, average amount, and the max-to-average ratio - that last one is particularly powerful. A customer whose largest single transaction is 6x their normal average is a very different risk profile than someone whose transactions are all similar in size."

### 3. Feature Store (5 min)

Show the Feature Store creation and entity registration:

> "This is where we centralize all feature definitions. The 'customer' entity with customer_id as the join key is the anchor. Every feature we calculate - transaction velocity, spend patterns, anomaly scores - gets associated with this entity.
>
> The business value: your fraud team, your AML team, and your credit team all pull from the same feature definitions. No more inconsistencies. And when a feature definition changes, you version it - you don't lose history."

Pause point - ask if they have this problem:
> "Does your team today have a single place where feature definitions live, or is it spread across Jupyter notebooks and Git repos on different teams' laptops?"

### 4. Model Training and Registry (5 min)

Show V1 training and registry, then V2:

> "We're training V1 intentionally simple - 10 trees, shallow depth. This is the baseline. Then we'll train V2 with optimized parameters and register both versions side by side.
>
> The Model Registry gives you: version control, metadata, metrics, and a full audit trail. In regulated finserv environments, being able to show a regulator exactly what model was running in production on a specific date, what training data it used, and who approved it - that's not nice to have, that's a compliance requirement."

### 5. Real-time Inference and Evaluation (5 min)

Show the inference cell and evaluation charts:

> "We score customers in real time using the model we just registered. The evaluation chart here shows something important for finserv specifically: precision and recall aren't equal in fraud detection.
>
> A false positive means you blocked a legitimate transaction. That customer calls your fraud hotline, they're frustrated, and some of them churn. A false negative means fraudulent money moves. These have very different business costs, and your model threshold should reflect your business's specific tolerance."

### 6. Cortex Integration (3 min)

Show the Cortex fraud risk assessment cell:

> "This is where things get interesting for your fraud analyst team. The ML model is fast and accurate but it gives you a binary: fraud or not fraud. Cortex adds a layer of explainability - it reads the same signals and writes a human-readable case summary.
>
> Your analysts reviewing the fraud queue now have both: the model's confidence score and an LLM-written explanation of why this transaction looks suspicious. That speeds up case review significantly."

---

## Closing Questions

- "Where does this fit into your current fraud model development workflow?"
- "The Feature Store piece specifically - is that a gap you're feeling today, or do you have something in place?"
- "What would it mean for your team to do this without managing a separate ML infrastructure stack outside Snowflake?"

---

## Common Objections

**"We already use [SageMaker / Databricks / MLflow] for our models."**
> "Totally valid - and you can continue to use those for training if that's where your team lives. The Model Registry accepts models trained anywhere. What Snowflake adds is that your features, your training data, your inference pipeline, and your monitoring all live in the same platform as your data. No data movement, no separate infrastructure to secure and audit."

**"Our fraud team doesn't use Python - they use SQL."**
> "The Feature Store and Model Registry are accessible via SQL. The inference stored procedure we created is callable from SQL. Your SQL-based team can query model predictions the same way they query any other table."

**"We're concerned about model latency for real-time fraud."**
> "The inference stored procedure runs inside Snowflake compute, so you're not moving data across a network boundary. For batch scoring at settlement time, this is very fast. For pure real-time at authorization, we'd talk about Snowpipe Streaming and Snowflake's low-latency options."

---

## Resources

- Snowflake ML Feature Store docs: docs.snowflake.com
- Model Registry guide: docs.snowflake.com
- Model Monitoring: docs.snowflake.com
