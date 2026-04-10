# GCP Medallion Architecture
<b>Implementation Medallion Architecture on GCP</b><br>
![GPP-Medallion Archirecture](gcp_medallion_screenshots/gcp_medallion.png)
## *Project Overview*
Implementing Medallion Architecture on Google Cloud Platform (GCP) by using BigQuery as Bronze-Silver-Gold layer, orchestrate the all processes with Apache Airflow, transformation and test proceses using dbt in docker contenerized. The pipeline begins with Airflow DAGs ingesting raw data into BigQuery (Bronze), followed by dbt models that clean and normalize data into a relational format (Silver), and finally aggregate it into business-ready tables (Gold).
## *Problem To Be Solved*
Implementing this specific stack addresses the "Data Swamp" problem — where data is technically available but practically unusable due to inconsistent quality, high latency, and fragile infrastructure.<br>
Without this architecture, data platforms typically suffer from three core failures:
1. <b>The Quality Gap (The "Garbage In, Garbage Out" Problem)</b><br>
   In a flat data warehouse, raw logs and refined business metrics often live in the same space. If a source API changes its schema, downstream dashboards break immediately.
     - <b>The Medallion Solution</b>: By enforcing a Silver layer, you create a mandatory "quality gate" where data is cleaned, typed, and deduplicated before it ever touches a business report.
2. <b>The Dependency Nightmare (Orchestration Friction)</b><br>
  As a data platform grows, managing the order of operations becomes impossible. If you run a transformation before the data has finished loading, your reports show yesterday's numbers.<br>
     - <b>The Airflow/dbt Solution</b>: Airflow handles the "when" (scheduling and cross-system triggers), while dbt handles the "how" (SQL logic and intra-warehouse dependencies). Together, they ensure that a Gold-layer table only updates after its Bronze and Silver parents have successfully refreshed.
3. <b>"It Works on My Machine" (Environment Drift)</b><br>
Infrastructure fragility is a major bottleneck. A data engineer might write a pipeline that works locally but fails in production because of a different Python version or a missing dbt plugin.<br>
     - <b>The Docker Solution</b>: By wrapping the entire stack in Docker, you guarantee that the logic running on your laptop is identical to what runs in GCP. This eliminates deployment "surprises" and allows for easy scaling on Google Kubernetes Engine (GKE).<br>
     - <b>The Bottom Line</b>: You are solving for Trust. By implementing this, you move from a reactive state (fixing broken dashboards) to a proactive state (delivering verified, version-controlled data assets).
## *Business Leverage & Impact*
1. <b>Radically Reduced "Time-to-Insight"</b><br>
By using dbt with Airflow, you replace weeks of manual SQL scripting with a modular, version-controlled framework.<br>
      - <b>The Leverage</b>: When a stakeholder asks for a new metric, you don't build a new silo. You simply add a layer to your existing Gold models. The automated testing ensures that new changes don't break old reports, allowing your team to ship updates daily rather than monthly.
2. <b>Elimination of "Decision Friction"</b><br>
Discrepancies between departments (e.g., Marketing and Finance reporting different "Active User" counts) create organizational paralysis.<br>
      - <b>The Business Impact</b>: The Silver layer acts as the "Universal Translator." It forces a single definition of truth across the company. When everyone trusts the dashboard, meetings move from "where did this number come from?" to "what should we do about this number?"
3. <b>Cost-Efficient Scalability</b><br>
Without this architecture, GCP costs often spiral because inefficient queries scan entire raw datasets repeatedly.<br>
      - <b>The Leverage</b><br>: By "landing" data once in Bronze and refining it into partitioned/clustered Gold tables, you optimize BigQuery compute. Docker ensures your orchestration costs are predictable—you aren't locked into expensive proprietary tools and can scale your infrastructure up or down in minutes without rewriting code.
## *Project Prerequition*
## *Project Flow*
