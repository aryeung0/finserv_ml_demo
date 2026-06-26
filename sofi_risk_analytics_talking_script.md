# Snowflake ML -- Talking Script
## SoFi Risk Analytics | First Meeting | June 2026
### Target: ~15 minutes + 5 minutes discovery (~130 wpm)

---

## Slide 1: Title

"Thanks for the time today. I'm Arnold, SE at Snowflake. I want to walk you through how Snowflake approaches ML -- with a focus on what's relevant for a Risk Analytics team doing fraud detection and risk scoring. I'll keep it to 20 minutes and leave room for your questions."

---

## Slide 2: Safe Harbor

"Quick safe harbor -- some of this covers roadmap items, so forward-looking statements are aspirational. Core platform capabilities I'll cover are GA or in active preview."

---

## Slide 3: Where Do ML Practitioners Spend Their Time?

"This stat resonates with every data science team I talk to -- 60% of time goes into data wrangling and feature engineering, not actual modeling. For a Risk Analytics team, that's even more painful because errors in feature computation don't just slow you down, they affect model fairness and compliance. Snowflake ML is built to close that gap."

---

## Slide 4: Agentic ML Is Dramatically Transforming ML Work

"Where the industry is heading: automation takes over the wrangling, and your team shifts to spending 60% of their time on domain expertise -- knowing what signals matter for fraud, interpreting when a model is drifting vs. when customer behavior is genuinely shifting. That irreplaceable judgment is where your team should be spending its time."

---

## Slide 5: Snowflake ML -- Unified Platform for Data and AI

"The blocker for most teams is platform fragmentation -- your ML environment is separate from your data, so every step requires data movement, and every handoff creates a governance gap. Snowflake ML puts everything on one platform: training, model registry, deployment, monitoring, all inside Snowflake with a single RBAC model and audit trail. For Risk Analytics, that matters: when a regulator asks what data trained a credit risk model, you have one place to answer. Does that resonate with your current setup?"

---

## Slide 6: Snowflake CoCo -- Your ML Agent with Full Context

"CoCo -- Cortex Code -- is our AI coding agent inside the Snowflake IDE. It has full awareness of your data, schemas, and existing models, and can build an end-to-end ML pipeline -- data prep, training, evaluation, deployment -- as verified, executable code. For your team, that means bootstrapping a new risk model takes hours instead of days."

---

## Slide 7: Snowflake Notebooks

"Snowflake Notebooks give your data scientists a familiar Jupyter experience that runs directly against Snowflake -- no data exports, no connection management. It's RBAC-controlled, Git-backed, and runs in the Container Runtime with managed GPU and CPU access. If your team is currently pulling data out of Snowflake into SageMaker or local notebooks, this eliminates that step."

---

## Slide 8: Container Runtime -- Flexible and Scalable Development

"The Container Runtime is the compute backbone -- pre-built ML environment, no dependency conflicts, elastic GPU and CPU scale. It's optimized for data ingestion from Snowflake tables, so training a fraud model on billions of transaction records doesn't bottleneck on data loading. We support Ray for distributed training when you need horizontal scale."

---

## Slide 9: ML Experiment Tracking

"When your team is iterating on a risk model -- testing different feature sets, architectures, training windows -- you need to know exactly which run produced which result. Experiment tracking logs parameters, metrics, and artifacts for every run, and lets you compare model versions side by side. Because it's inside Snowflake, there's no separate MLflow server to manage."

---

## Slide 10: Snowflake Model Registry

"The Model Registry is where models live after training -- versioned, with full metadata on who trained it, on what data, and with what evaluation metrics. You can register models trained in Snowflake, imported from SageMaker, or pulled from public hubs, and call `predict()` directly from SQL or Python. For model governance and audit certification, this is the system of record."

---

## Slide 11: Real-Time Feature and Model Serving

"This one is directly relevant to fraud detection. Real-time inference means serving a fraud score in under 100ms at the point of a transaction -- features served in under 30ms, consistent latency, managed REST API endpoint. Snowflake ML provides this as a fully managed service, with the same governance model as your batch workloads. Quick question: are you running real-time fraud scoring today, and is it on a separate stack from your data?"

---

## Slide 12: Snowflake Feature Store

"Snowflake now has a built-in Feature Store that supports both batch and real-time serving. You define features once -- they're automatically computed and refreshed from batch or streaming sources, and the same features used for training are served at inference time, so there's no skew. It's also a shared layer for the whole team: features are discoverable and reusable across models, so if one data scientist builds rolling transaction velocity or behavioral anomaly scores, everyone benefits."

---

## Slide 13: ML Observability

"Once a model is in production, you need to know when it's drifting. Snowflake ML Observability gives you out-of-the-box drift metrics plus custom alerting -- 'notify me when precision drops below X.' We also compute Shapley explainability values automatically, which is increasingly important for regulatory compliance: if a model is flagging fraud or influencing credit decisions, you need to explain why."

---

## Slide 14: Snowflake Governance Extends to ML

"What sets Snowflake ML apart from a standalone ML platform is that Snowflake's existing governance extends natively to your ML artifacts. ML Lineage traces end-to-end from raw source tables through features to model versions -- a full audit trail. Data Quality Monitoring catches data issues before they corrupt a model. Synthetic Datasets lets you build models on PII-sensitive data without exposing the raw records."

---

## Slide 15: End-to-End Workflow -- Wrap Up

"To close: data prep, training, model registry, and inference all on one platform. No data movement, no separate ML infrastructure, one audit trail. 

This is all One platform, one governance layer, one set of credentials. That's the core of what differentiates Snowflake from a stitched-together stack. 

Before we wrap up -- what does your current ML workflow look like for risk scoring? Understanding where your biggest pain points are will help me figure out whether a deep-dive on a specific capability or a hands-on proof of concept is the right next step.
"

---

## Notes for Delivery

**Key SoFi context:**
- Heavy ML workloads for fraud detection, risk scoring, and customer engagement
- ML platform team standardized on SageMaker -- position as consolidation, not replacement
- $135K Cortex AI Functions spend in Q1 -- already using Snowflake AI, not ML end-to-end
- First meeting with Risk Analytics specifically -- discovery matters as much as pitching

**Discovery questions to weave in:**
- "Where does your data live vs. where do you train today?"
- "How do you handle feature consistency between training and inference?"
- "Do you have model monitoring in place for production risk models?"
- "How long does it take to go from a trained model to production today?"
- "What does model governance look like for your risk models?"
