# Acme Analytics: plans

> Fetched from https://example.com/pricing and converted to markdown.
> Tables were flattened into lists during conversion.

## Navigation

Home, Plans, Docs, Support, Start free trial

## Compare plans

Billing: Monthly / Annual (soon)

### Basic

01 Collection
- Event Stream

02 Modelling
- Cohort Builder

03 Alerting and export
- (Team only)

[Choose Basic]

### Team (Popular)

01 Collection
- Event Stream

02 Modelling
- Cohort Builder

03 Alerting and export (Team only)
- Threshold Alerts: Watches one metric and fires when it crosses a line you set.
- Anomaly Alerts: Learns the weekly shape of a metric and fires on the unexpected.
- Scheduled Export: Ships a filtered slice to S3 or BigQuery on a cron you choose.
- Webhook Relay

[Choose Team]

Basic covers 2 tools, Team all 5. Pay by card or by invoice today; SSO arrives
later. Cancel anytime from the billing page.

## Tools

Five tools sharing one event schema, so a cohort you build in one place resolves the
same way everywhere else. Each tool has its own page with the long description and a
configuration walkthrough.

- Event Stream: Raw events with a 90-day retention window and a replay endpoint.
- Cohort Builder: Builds cohorts from event sequences, with retention curves.
- Threshold Alerts: Watches one metric and fires when it crosses a line you set.
- Anomaly Alerts: Learns the weekly shape of a metric and fires on the unexpected.
- Scheduled Export: Ships a filtered slice to S3 or BigQuery on a cron you choose.
- Webhook Relay: Forwards any alert to an endpoint you own, with signed payloads
  and retries.

## Questions

**How fast is setup?** Usually under an hour. You drop the snippet in, we backfill
nothing, and the first events arrive immediately.

**Can I change plans later?** Yes, up or down, once per billing period. The change
takes effect at the start of the next period, and we do not prorate.

**What happens to my data if I cancel?** Events stay queryable for 30 days after the
subscription ends, then they are deleted. Export before then if you need them, the
Scheduled Export tool keeps working until the last day.

**Do you support SSO?** Not yet. It is on the roadmap and it will land on the Team
plan first.

## Ready to start?

Get the Team plan for 30 days. Cancel anytime from the billing page.

[Start free trial]
