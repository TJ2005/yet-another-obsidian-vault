---

Title: "(ISA) LAB 3 Incident-Based Information Systems Audit"

Status:

marker:

tags:

Date: "2026.08.03"

Time: "12:20"

---
# Experiment 3

## Title

**Incident-Based Information Systems Audit of AWS Cloud Cost Escalation using COBIT 2019**

---

# Aim

To investigate the unexpected AWS cloud cost escalation experienced by ShopEase E-Commerce Pvt. Ltd., identify the underlying control failures, analyze the root cause of the incident, map the findings to COBIT 2019 governance objectives, and prepare an Information Systems Audit report.

---

# Scenario

ShopEase E-Commerce Pvt. Ltd. experienced an unexpected increase of approximately **USD 45,000** in AWS cloud expenditure during a single weekend.

The Chief Financial Officer (CFO) suspected financial negligence because no such expenditure had been approved. The Engineering Lead claimed the spike resulted from an unavoidable deployment issue.

As independent Information Systems Auditors, our responsibility is to analyze the available evidence, determine the actual cause of the incident, evaluate whether appropriate controls were operating effectively, identify governance failures, and recommend corrective actions.

---

# Task 1 – Review of Audit Evidence

## Nature of Audit

This investigation is **not limited to a single audit domain**. It combines several audit disciplines.

| Audit Area                     | Reason                                                            |
| ------------------------------ | ----------------------------------------------------------------- |
| Cloud Financial Audit (FinOps) | Investigates abnormal AWS expenditure and budget management.      |
| Cybersecurity Audit            | Reviews IAM privileges, authentication and access controls.       |
| Change Management Audit        | Examines deployment approvals, CAB records and rollback planning. |
| IT Operations Audit            | Reviews cloud operations, monitoring and incident response.       |
| Governance Audit               | Evaluates management oversight and compliance with COBIT 2019.    |

---

## Review of Exhibits

| Exhibit | Evidence                 | Audit Category             | Purpose                                                                   |
| ------- | ------------------------ | -------------------------- | ------------------------------------------------------------------------- |
| A       | AWS Cost Explorer        | Financial Audit            | Confirms abnormal AWS billing spike.                                      |
| B       | AWS CloudTrail Logs      | Cybersecurity / Operations | Shows 20 GPU instances were launched and remained running.                |
| C       | IAM Policy               | Cybersecurity              | Shows excessive Administrator privileges assigned to a developer account. |
| D       | AWS Budgets              | Financial Governance       | Confirms budget alerts were disabled.                                     |
| E       | CAB Approval Record      | Change Management          | Shows missing approvals and rollback documentation.                       |
| F       | CloudWatch Configuration | Operations Audit           | Confirms monitoring and billing alerts were disabled.                     |
| G       | CFO Email                | Financial Evidence         | Documents discovery of unauthorized expenditure.                          |
| H       | Engineering Lead Email   | Management Representation  | Provides management explanation but not technical evidence.               |
| I       | AWS Cost Breakdown       | Financial Analysis         | Identifies EC2 GPU instances as the major contributor to the cost spike.  |

---

# Task 2 – Assets, Threats and Vulnerabilities

| Asset                       | Threat                              | Vulnerability                                                                        | Business Risk               |
| --------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------ | --------------------------- |
| AWS Infrastructure          | Excessive cloud resource deployment | No budget monitoring, No Limits on API keys                                          | Unexpected financial loss   |
| EC2 GPU Instances           | Unauthorized provisioning           | Unlimited Administrator privileges, No Limits set, No policies and notifications set | Excessive operational cost  |
| AWS IAM Accounts            | Privilege misuse                    | AdministratorAccess assigned to developer, 2FA and Authorization                     | Security compromise         |
| AWS Budget Service          | Cost escalation                     | Budget alerts disabled,                                                              | Delayed financial detection |
| CloudWatch Monitoring       | Incident goes unnoticed             | Monitoring alarms disabled, No requirement for changing setting                      | Delayed response            |
| Production Environment      | Unauthorized deployment             | No CAB approval                                                                      | Service disruption          |
| Change Management Process   | Failed deployments                  | No rollback plan                                                                     | Extended outages            |
| Company Financial Resources | Budget overrun                      | Weak governance                                                                      | Financial impact            |

---

# Risk Assessment Matrix

| Risk | Likelihood | Impact | Overall Risk |
|------|------------|--------|--------------|
| Unauthorized GPU deployment | Very High | Very High | **Critical** |
| Excessive AWS expenditure | Very High | Very High | **Critical** |
| Privilege misuse | High | Very High | **High** |
| Missing monitoring | Very High | High | **Critical** |
| Unauthorized production change | Very High | High | **Critical** |
| Delayed incident response | High | High | **High** |

---

# Task 3 – Root Cause Analysis (5 Whys)

## Problem Statement

AWS costs increased by approximately **USD 45,000** over one weekend.

---

### Why 1

**Why did the AWS bill increase?**

Twenty high-performance GPU EC2 instances (p5.48xlarge) were launched and continued running.

**Evidence:** Exhibit B, Exhibit I

---

### Why 2

**Why did the instances remain active?**

The Auto Scaling group was configured to maintain twenty running instances and termination protection was enabled.

**Evidence:** Exhibit B

---

### Why 3

**Why was the developer able to launch these resources?**

The developer account had unrestricted **AdministratorAccess**, while Multi-Factor Authentication (MFA) and password rotation were disabled.

**Evidence:** Exhibit C

---

### Why 4

**Why was this deployment permitted?**

The deployment bypassed the Change Advisory Board (CAB), lacked security review, business approval, risk assessment and rollback planning.

**Evidence:** Exhibit E

---

### Why 5

**Why was the issue not detected earlier?**

AWS Budget alerts and CloudWatch billing alarms had been disabled, preventing early notification of abnormal cloud spending.

**Evidence:** Exhibit D, Exhibit F

---

## Root Cause

The incident resulted from **multiple governance failures**, not from a single technical error.

Major root causes include:

- Excessive privileged access
- Weak Identity and Access Management
- Failure of change management procedures
- Disabled financial monitoring
- Disabled operational monitoring
- Lack of cloud governance
- Absence of preventive and detective controls

---

# Failed Controls

| Control                     | Expected State                         | Actual State                | Status   |
| --------------------------- | -------------------------------------- | --------------------------- | -------- |
| Least Privilege             | Developers receive minimum permissions | AdministratorAccess granted | ❌ Failed |
| Multi-Factor Authentication | Enabled                                | Disabled                    | ❌ Failed |
| Password Rotation           | Enabled                                | Disabled                    | ❌ Failed |
| AWS Budget Alerts           | Enabled                                | Disabled                    | ❌ Failed |
| CloudWatch Billing Alerts   | Enabled                                | Disabled                    | ❌ Failed |
| CAB Approval                | Mandatory                              | Missing                     | ❌ Failed |
| Risk Assessment             | Required                               | Missing                     | ❌ Failed |
| Rollback Plan               | Mandatory                              | Missing                     | ❌ Failed |
| Monitoring Dashboard        | Active                                 | Disabled                    | ❌ Failed |
| Cost Monitoring             | Continuous                             | Disabled                    | ❌ Failed |

---

# Recommended Corrective Controls

## Identity and Access Management

- Remove AdministratorAccess from developer accounts.
- Apply Principle of Least Privilege.
- Enforce Multi-Factor Authentication.
- Enable periodic access reviews.

---

## Cloud Cost Governance

- Enable AWS Budgets.
- Configure budget thresholds (50%, 75%, 90%, 100%).
- Configure SNS and email notifications.
- Enable AWS Cost Anomaly Detection.

---

## Change Management

- Require CAB approval before production deployment.
- Conduct security and business impact assessments.
- Document rollback procedures.
- Perform post-implementation reviews.

---

## Operational Monitoring

- Enable CloudWatch Billing Alarms.
- Enable EC2 monitoring.
- Monitor Auto Scaling Groups.
- Configure idle instance detection.

---

## Governance Improvements

- Define cloud governance policies.
- Assign resource ownership.
- Perform quarterly control reviews.
- Conduct periodic IS audits.

---

# Task 4 – COBIT 2019 Mapping

| Finding                            | COBIT Objective | Description                                    |
| ---------------------------------- | --------------- | ---------------------------------------------- |
| Weak enterprise risk management    | **EDM03**       | Ensure Risk Optimization                       |
| Weak governance framework          | **APO01**       | Managed I&T Management Framework               |
| Budget management failure          | **APO06**       | Managed Budget and Costs                       |
| Missing risk assessment            | **APO12**       | Managed Risk                                   |
| Weak IAM controls                  | **APO13**       | Managed Security                               |
| Unauthorized production deployment | **BAI06**       | Managed IT Changes                             |
| Missing rollback planning          | **BAI07**       | Managed Change Acceptance and Transitioning    |
| Poor operational management        | **DSS01**       | Managed Operations                             |
| Weak incident handling             | **DSS02**       | Managed Service Requests and Incidents         |
| Weak security monitoring           | **DSS05**       | Managed Security Services                      |
| Disabled performance monitoring    | **MEA01**       | Managed Performance and Conformance Monitoring |
| Weak internal controls             | **MEA02**       | Managed System of Internal Control             |

---

# Executive Audit Report

## Audit Opinion

**Overall Opinion: Unsatisfactory (High Risk)**

The audit concludes that the AWS cost escalation was **preventable**.

The incident occurred because several preventive, detective and governance controls failed simultaneously.

The investigation found no evidence supporting the claim that the incident was solely an unavoidable deployment glitch. Instead, the evidence demonstrates failures in access control, change management, monitoring, financial governance and operational oversight.

---

## Key Findings

- Approximately **USD 45,000** of unexpected AWS expenditure occurred over one weekend.
- Twenty GPU instances were launched and remained active.
- Administrator privileges were assigned to a developer account.
- MFA and password rotation were disabled.
- CAB approval and rollback planning were absent.
- AWS Budgets and CloudWatch billing alerts were disabled.
- Finance detected the issue only after the expenditure had already occurred.

---

## Business Impact

- Significant unplanned cloud expenditure.
- Weak governance over cloud infrastructure.
- Increased operational and financial risk.
- Reduced accountability for production changes.
- Delayed incident detection and response.

---

## Recommendations

1. Implement least privilege access across AWS.
2. Enforce Multi-Factor Authentication.
3. Enable AWS Budgets and billing alerts.
4. Configure CloudWatch monitoring and cost anomaly detection.
5. Require CAB approval for all production deployments.
6. Document risk assessments and rollback plans.
7. Perform regular IAM reviews and control audits.
8. Conduct periodic COBIT-based governance assessments.

---

# Conclusion
The failure in the entire event is completely a management failure and can be **easily prevented** by having structured whilst following basic suggestive principles as per COBIT
The audit concludes that the AWS billing incident resulted from a combination of **governance failures, weak security controls, inadequate change management and ineffective operational monitoring**.

The organization lacked both preventive controls (least privilege, change approval and rollback planning) and detective controls (budget alerts, CloudWatch monitoring and incident detection). These weaknesses allowed excessive cloud resources to remain operational without timely intervention, resulting in substantial financial loss.

Implementing the recommended controls and aligning governance practices with **COBIT 2019** will significantly improve risk management, operational resilience and cloud cost governance while reducing the likelihood of similar incidents in the future.