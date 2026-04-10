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
## *Project Prerequition*
## *Project Flow*
