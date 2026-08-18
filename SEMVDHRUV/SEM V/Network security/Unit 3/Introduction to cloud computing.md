# Cloud Computing 

## Overview

Cloud computing enables **on-demand network access** to a shared pool of configurable resources (networks, servers, storage, applications, and services). These can be rapidly provisioned and released with minimal management effort or provider interaction.

## Essential Characteristics

* **Broad Network Access** – Services available over standard networks, accessible by various clients (e.g., phones, laptops, thin clients).
* **Rapid Elasticity** – Resources can scale up or down automatically based on demand.
* **Measured Service** – Resource usage is monitored, controlled, and reported for transparency.
* **On-Demand Self-Service** – Consumers can provision computing resources automatically without human intervention.
* **Resource Pooling** – Shared resources serve multiple customers using a multi-tenant model with location abstraction.

## Service Models

* **Software as a Service (SaaS)** – Consumers use provider’s applications via web interfaces. The provider manages installation, updates, and maintenance.
  *Examples: Gmail, Salesforce.*
* **Platform as a Service (PaaS)** – Consumers deploy applications using tools and languages supported by the provider. Offers middleware and runtime environments.
* **Infrastructure as a Service (IaaS)** – Consumers provision basic computing resources (processing, storage, networking) and install their own OS and apps.

## Deployment Models

* **Public Cloud** – Infrastructure owned and managed by a third-party provider, available to the public or large industry groups.
* **Private Cloud** – Exclusive use by a single organization, managed internally or by a third party.
* **Community Cloud** – Shared by organizations with common concerns (e.g., security, compliance).
* **Hybrid Cloud** – Combination of two or more clouds (public, private, community) enabling data and app portability.

## Cloud Computing Context

Enterprises connect their internal LANs to cloud providers via the Internet. The provider manages large server farms (often blade servers) offering storage, compute, and applications as services.

## NIST Cloud Computing Reference Architecture

Defines the roles and relationships among cloud entities to standardize understanding and comparison of services.

### Key Actors

* **Cloud Consumer** – Uses cloud services.
* **Cloud Provider** – Makes services available (SaaS, PaaS, IaaS).
* **Cloud Auditor** – Independently assesses security, performance, and compliance.
* **Cloud Broker** – Manages use and delivery of services between consumers and providers.
* **Cloud Carrier** – Provides network connectivity and transport for cloud services.

### Broker Functions

* **Service Intermediation** – Adds value through performance monitoring, identity management, or security.
* **Service Aggregation** – Combines multiple services for performance or cost optimization.
* **Service Arbitrage** – Buy from one source Sell at another.

### Auditor Role

Assesses cloud providers for security, privacy, and performance compliance. Acts as an independent assurance entity.
