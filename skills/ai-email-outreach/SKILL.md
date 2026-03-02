---
name: ai-email-outreach
description: |
  AI agent email outreach with verified email finding, ICP targeting, and personalized messaging.
  Use when building agents that need to: (1) Find verified business emails for outreach,
  (2) Identify decision makers at target companies, (3) Research prospects for personalization,
  (4) Write contextual cold emails, (5) Avoid email bounces and protect sender reputation.
  Triggers: email outreach, find emails, cold email, lead generation, prospect research,
  email finder, verified emails, ICP targeting, decision makers, sales automation, SDR agent.
---

# AI Email Outreach

Build agents that find the right people, get verified emails, and send personalized outreach.

## Core Workflow

```
1. Define ICP → 2. Find Companies → 3. Find Decision Makers → 4. Verify Email → 5. Research Context → 6. Write Email → 7. Send
```

## Step 1: Find Verified Emails (Never Web Scrape)

Web scraping for emails fails 40-70% of the time. Use dedicated APIs:

```python
# Apollo.io API example
import requests

response = requests.post("https://api.apollo.io/v1/mixed_people/search",
    headers={"x-api-key": APOLLO_API_KEY},
    json={
        "organization_domains": ["targetcompany.com"],
        "person_titles": ["VP Engineering", "CTO", "Head of Engineering"],
        "email_status": ["verified"],
        "per_page": 10
    }
)
leads = response.json()["people"]
```

### Email Finder APIs (Cheapest to Premium)

| Tool | Cost | API | Accuracy | Notes |
|------|------|-----|----------|-------|
| Icypeas | ~$7/1000 | Yes | Good | Cheapest bulk option |
| Apollo.io | Free tier | Yes | Good | 4k requests/day limit |
| Snov.io | $30/mo | Yes | ~90% | Includes CRM |
| Findymail | $49/mo | Yes | >95% | Only charges for valid, <2% bounce |
| Skrapp | $49/mo | Yes | 92% | No charge for invalid |

See [references/email-apis.md](references/email-apis.md) for full API details.

## Step 2: Always Verify Before Sending

Never send without verification. Keep bounce rate under 2%.

```python
# NeverBounce verification
import requests

response = requests.post("https://api.neverbounce.com/v4/single/check",
    json={
        "key": NEVERBOUNCE_API_KEY,
        "email": "person@company.com"
    }
)
result = response.json()["result"]  # "valid", "invalid", "disposable", "catchall"

if result == "valid":
    send_email()
```

### Verification APIs

- **NeverBounce** - 20+ step cleaning, verifies up to 75 times
- **ZeroBounce** - Real-time validation, catches disposable emails
- **Verifalia** - AI-powered, 99% accuracy, 30+ verification steps

## Step 3: Find the Right People (ICP Targeting)

Define clear criteria, then use APIs to filter:

```python
# ICP filtering with Apollo
icp_criteria = {
    "organization_num_employees_ranges": ["11,50", "51,200"],
    "person_seniorities": ["director", "vp", "c_suite"],
    "organization_industry_tag_ids": ["software", "saas"],
    "person_departments": ["engineering", "product"]
}
```

### Decision Maker Identification

- Filter by title: VP, Head of, Director, Manager, C-suite
- Filter by department: Engineering, Marketing, Sales, Product
- Seniority mapping: IC → Manager → Director → VP → C-Suite

## Step 4: Research Before Writing

72% of people only engage with personalized outreach.

### What to Research

**Company Context:**
- Recent news (funding, launches, hiring) - Google News API, Crunchbase
- Tech stack - BuiltWith API, Wappalyzer
- Company size changes - LinkedIn, Apollo

**Person Context:**
- LinkedIn activity - Proxycurl API
- Job tenure (new role = different approach)
- Content they've published

```python
# Proxycurl for LinkedIn data
response = requests.get("https://nubela.co/proxycurl/api/v2/linkedin",
    headers={"Authorization": f"Bearer {PROXYCURL_API_KEY}"},
    params={"linkedin_profile_url": "https://linkedin.com/in/person"}
)
profile = response.json()
```

## Step 5: Write Contextual Emails

### Bad (Generic)
```
Hi John, I noticed you work at Acme Corp.
We help companies like yours improve efficiency...
```

### Good (Contextual)
```
Hi John, saw your post about scaling the engineering
team after the Series B. When [similar company] hit
that stage, they ran into [specific problem].

[One sentence on how you help]

Worth a quick chat?
```

### Email Structure

1. **Opening** - Reference something specific from research (1 line)
2. **Problem** - Pain point relevant to their role (1-2 lines)
3. **Solution** - Brief mention of how you help (1 line)
4. **CTA** - Simple, low-commitment ask (1 line)

**Rules:**
- Keep under 100 words
- One specific detail from research required
- No generic templates
- Simple CTA (quick call, not "30 min demo")

## Micro-Campaign Strategy

The 1,000-recipient blast is dead. Use micro-campaigns:

- **List size**: 10-20 hyper-personalized leads
- **Sequence**: 3-5 steps (intro, follow-up, reminder)
- **Test first**: Soft launch to 50 leads
- **Protect reputation**: One high-bounce campaign damages domain for months

## Key Metrics

- **Bounce rate**: Keep under 2%
- **Spam complaints**: Keep under 0.3%
- **Reply rate**: 32-64% achievable with personalization
- **Open rate**: 92% achievable with good targeting

## Agent System Prompt Template

```markdown
## Role
You are a sales outreach agent.

## Step 1: Qualify Lead
- Check company matches ICP: [criteria]
- Find decision maker via Apollo/Snov.io API
- Verify email via NeverBounce/ZeroBounce
- STOP if email not verified

## Step 2: Research Context
1. Company website → what they do, recent news
2. LinkedIn profile → recent activity, job tenure
3. News API → announcements, funding

## Step 3: Write Personalized Email
- Opening: Reference specific research finding
- Problem: Pain point for their role
- Solution: One line on how you help
- CTA: Low-commitment ask

## Rules
- NEVER send without verified email
- NEVER use generic templates
- ALWAYS include specific detail from research
- Keep under 100 words
```
